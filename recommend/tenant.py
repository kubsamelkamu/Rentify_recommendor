def recommend_properties_for_tenant(user_id, data):
    # TODO: Implement recommendation logic
    # Example: Return top 5 properties (stub)
    properties = data['properties']
    return properties.head(5).to_dict(orient='records')

