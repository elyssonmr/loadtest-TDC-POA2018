import json

from tornado.web import RequestHandler

from orders.controllers import OrderController, ProductController


class ProductHandler(RequestHandler):
    @property
    def db(self):
        return self.settings["db"]

    async def post(self):
        try:
            product_data = json.loads(self.request.body)
        except json.JSONDecodeError:
            self.write({"message": "Invalid Json Request"})
            self.set_status(400)
            return

        try:
            controller = ProductController(self.db)
            created_id = await controller.save_product(product_data)
            product_data["id"] = created_id
            self.write({"createdId": created_id})
            self.set_status(201)
        except ValueError as ex:
            self.write({"message": str(ex)})
            self.set_status(400)


class OrderHandler(RequestHandler):
    @property
    def db(self):
        return self.settings["db"]

    async def post(self):
        try:
            order_data = json.loads(self.request.body)
        except json.JSONDecodeError:
            self.write({"message": "Invalid Json Request"})
            self.set_status(400)
            return

        try:
            controller = OrderController(self.db)
            created_order = await controller.save_order(order_data)
            self.write({"createdId": created_order["id"]})
            self.set_status(201)
        except ValueError as ex:
            self.write({"message": str(ex)})
            self.set_status(400)
