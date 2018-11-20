from orders.validators import validate_product

class ProductController:
    def __init__(self, db):
        self.collection = db["products"]

    async def save_product(self, product_data):
        product = validate_product(product_data)

        result = await self.collection.create_one(product)
        return str(result.inserted_id)
