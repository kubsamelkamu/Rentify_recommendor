def recommend_properties_for_tenant(user_id, data):
    
    users = data['users']
    properties = data['properties']
    bookings = data['bookings']
    likes = data['likes']
    reviews = data.get('reviews', None)

    tenant = users[users['id'] == user_id]
    if tenant.empty:
        return []

    booked_ids = bookings[bookings['tenantId'] == user_id]['propertyId'].tolist()
    liked_ids = likes[likes['userId'] == user_id]['propertyId'].tolist()
    reviewed_ids = []
    if reviews is not None:
        reviewed_ids = reviews[reviews['userId'] == user_id]['propertyId'].tolist()

    exclude_ids = set(booked_ids + liked_ids + reviewed_ids)
    available_props = properties[~properties['id'].isin(exclude_ids)]
    
    if booked_ids:
        last_booking = bookings[(bookings['tenantId'] == user_id)].sort_values('createdAt').iloc[-1]
        city = properties[properties['id'] == last_booking['propertyId']]['city'].values[0]
        available_props = available_props[available_props['city'] == city]

    if reviews is not None and not available_props.empty:
        prop_reviews = reviews.groupby('propertyId')['rating'].mean().reset_index()
        available_props = available_props.merge(prop_reviews, left_on='id', right_on='propertyId', how='left')
        available_props['rating'] = available_props['rating'].fillna(0)
        available_props = available_props.sort_values(['rating', 'rentPerMonth'], ascending=[False, True])
    else:
        available_props = available_props.sort_values('rentPerMonth')

    return available_props.head(5).to_dict(orient='records')