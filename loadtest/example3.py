from random import randint
import os

from locust import HttpLocust, TaskSet, task


MAX_TIME = int(os.environ.get("MAX_TIME", 2000))

class APITasks(TaskSet):
    def on_start(self):
        for i in range(1, 6):
            book = {
                "Title": f"My Little Book {i}",
                "ID": f"{i}"
            }
            self.client.post("/api/books", json=book)

    def _check_response_time(self, resp):
        elapsed = resp.elapsed.microseconds / 1000
        if resp.status_code == 200 and elapsed > MAX_TIME:
            resp.failure(
                "Response time is bigger than expected."
                f"Got: {resp.elapsed}, expected: {MAX_TIME}")

    @task(10)
    def allBooks(self):
        with self.client.get("/api/books") as resp:
            self._check_response_time(resp)

    @task(5)
    def especificBook(self):
        seed = randint(1, 5)
        with self.client.get(
                f"/api/books/{seed}", name="/api/books/ID") as resp:
            self._check_response_time(resp)

class APIUser(HttpLocust):
    task_set = APITasks
    min_wait = 5000
    max_wait = 15000
    host = "https://fakerestapi.azurewebsites.net"
