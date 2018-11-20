from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient
from tornado.web import Application


from orders.handlers import ProductHandler, OrderHandler



def make_application():
    db = AsyncIOMotorClient(config("MONGO_URI"))["orders"]
    handlers = [
        (r"/products", ProductHandler),
        (r"/orders", OrderHandler)
    ]
    settings = {
        "db": db
    }

    app = Application(handlers, **settings)
    app.listen(8000)
    return app
