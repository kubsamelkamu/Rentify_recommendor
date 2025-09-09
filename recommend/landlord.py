def recommend_tenants_for_property(property_id, data):
    
    users = data['users']
    bookings = data['bookings']
    likes = data['likes']
    reviews = data.get('reviews', None)

    booked_tenants = bookings[bookings['propertyId'] == property_id]['tenantId'].tolist()
    liked_tenants = likes[likes['propertyId'] == property_id]['userId'].tolist()
    reviewed_tenants = []
    if reviews is not None:
        reviewed_tenants = reviews[reviews['propertyId'] == property_id]['tenantId'].tolist()

    tenant_ids = set(booked_tenants + liked_tenants + reviewed_tenants)
    tenants = users[(users['id'].isin(tenant_ids)) & (users['role'] == 'TENANT')]

    if reviews is not None and not tenants.empty:
        tenant_reviews = reviews.groupby('tenantId')['rating'].mean().reset_index()
        tenants = tenants.merge(tenant_reviews, left_on='id', right_on='tenantId', how='left')
        tenants['rating'] = tenants['rating'].fillna(0)
        tenants = tenants.sort_values('rating', ascending=False)

    return tenants.head(3).to_dict(orient='records')