from locust import HttpUser, task


class User(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
