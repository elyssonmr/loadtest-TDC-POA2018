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
