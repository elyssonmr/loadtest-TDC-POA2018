from random import randint
from locust import HttpLocust, TaskSet, task

class APITasks(TaskSet):
    def on_start(self):
        for i in range(1, 6):
            book = {
                "Title": f"My Little Book {i}",
                "ID": f"{i}"
            }
            self.client.post("/api/books", json=book)

    @task(10)
    def allBooks(self):
        self.client.get("/api/books")

    @task(5)
    def especificBook(self):
        seed = randint(1, 5)
        self.client.get(f"/api/books/{seed}", name="/api/books/ID")

class APIUser(HttpLocust):
    task_set = APITasks
    min_wait = 5000
    max_wait = 15000
    host = "https://fakerestapi.azurewebsites.net"
