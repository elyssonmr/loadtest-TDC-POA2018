import datetime

from bson import Timestamp

from orders.validators import validate_order, validate_product


class ProductController:
    def __init__(self, db):
        self._collection = db["products"]

    async def save_product(self, product_data):
        product = validate_product(product_data)

        result = await self._collection.insert_one(product)
        return str(result.inserted_id)
    
    async def get_itens_by_ids(self, products_id):
        products = await self._collection.find(
            {"_id": {"$in": products_id}}).to_list(None)

        return products


class OrderController:
    def __init__(self, db):
        self._collection = db["orders"]
        self._product_controller = ProductController(db)

    async def _get_items(self, items_ids):
        return await self._product_controller.get_itens_by_ids(items_ids)
    
    def _calculate_total_price(self, items):
        total = 0.0
        print(items)
        for item in items:
            total += item["price"]

        return total

    async def save_order(self, order_data):
        order = validate_order(order_data)

        order["items"] = await self._get_items(order["items"])
        order["price"] = self._calculate_total_price(order["items"])
        order["datetime"] = datetime.datetime.utcnow()
        print(order)

        result = await self._collection.insert_one(order)
        order["id"] = str(result.inserted_id)
        return order
