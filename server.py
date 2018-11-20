import asyncio

from orders.application import make_application

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    make_application()

    loop.run_forever()
