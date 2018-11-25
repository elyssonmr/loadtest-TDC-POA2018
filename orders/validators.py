from bson import ObjectId


def validate_order(order_data):
    items = order_data.get("items")

    if not items and not isinstance(items, list):
        raise ValueError("Items mus be a list of strings")
    
    for item in items:
        if not item and isinstance(item, str):
            raise ValueError("All items must be string")

    name = order_data.get("name")
    if not name and not isinstance(name, str):
        raise ValueError("Name is a required string")

    email = order_data.get("email")
    if not email and not isinstance(email, str):
        raise ValueError("Email is a required string")

    if '@' not in email:
        raise ValueError("Email should follow the pattern: exemple@email.com")

    return {
        "items": [ObjectId(item) for item in items],
        "name": name,
        "email": email
    }


def validate_product(product_data):
    name = product_data.get("name")
    if not name and not isinstance(name, str):
        raise ValueError("Name is a required string")
    
    description = product_data.get("description")
    if not description and isinstance(description, str):
        raise ValueError("Description is a required string")

    price = product_data.get("price")
    if not price and not isinstance(price, (float, int)):
        raise ValueError("Price is a required number")

    return {
        "name": name,
        "description": description,
        "price": price
    }
