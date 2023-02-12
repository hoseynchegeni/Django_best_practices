from locust import HttpUser, task

class QuickStartUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/blog")
        
