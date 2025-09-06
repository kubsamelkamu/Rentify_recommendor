def recommend_tenants_for_property(property_id, data):
    # TODO: Implement matching logic
    # Example: Return top 5 tenants (stub)
    users = data['users']
    tenants = users[users['role'] == 'TENANT']
    return tenants.head(5).to_dict(orient='records')
