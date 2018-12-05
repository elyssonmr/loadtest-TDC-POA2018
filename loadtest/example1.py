from locust import HttpLocust, TaskSet, task

class APITasks(TaskSet):
    @task
    def authors(self):
        self.client.get("/api/authors")

    @task
    def books(self):
        self.client.get("/api/books")

    @task
    def users(self):
        self.client.get("/api/users")

class APIUser(HttpLocust):
    task_set = APITasks
    min_wait = 5000
    max_wait = 15000
    host = "https://fakerestapi.azurewebsites.net"
