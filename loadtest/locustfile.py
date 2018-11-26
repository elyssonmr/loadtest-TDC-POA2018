from random import randint, choice
import os

from locust import TaskSet, task, HttpLocust


MAX_TIME = int(os.environ.get("MAX_TIME", 2000))


class CreateOrderProductsTestSet(TaskSet):
    def on_start(self):
        self._created_products = []
        for i in range(5):
            product = {
                "name": f"Product{i}",
                "description": f"Product{i} description",
                "price": 2.0 + float(i)
            }
            resp = self.client.post("/products", json=product)
            self._created_products.append(resp.json()["createdId"])


    def _check_response_time(self, resp):
        elapsed = resp.elapsed.microseconds / 1000
        if resp.status_code == 201 and elapsed > MAX_TIME:
            resp.failure(
                "Response time is bigger than expected."
                f"Got: {resp.elapsed}, expected: {MAX_TIME}")

    @task(10)
    def create_order(self):
        seed = randint(1, 100)
        itens = (choice(self._created_products) for i in range(randint(1, 5)))
        order = {
            "name": f"Locust{seed}",
            "email": f"email{seed}@email.com",
            "items": list(itens)
        }
        with self.client.post(
                "/orders", json=order, catch_response=True) as resp:
            self._check_response_time(resp)

    @task(5)
    def create_new_product(self):
        seed = randint(1, 100)
        product = {
            "name": f"New Product{seed}",
            "description": f"Product{seed} description",
            "price": 2.0 + float(seed)
        }
        with self.client.post(
                "/products", json=product, catch_response=True) as resp:
            self._check_response_time(resp)


class ApiLoadTest(HttpLocust):
    task_set = CreateOrderProductsTestSet
    min_wait = 200
    max_wait = 500
