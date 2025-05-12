from locust import HttpUser, task

class TriviaUser(HttpUser):
    @task(10)
    def play_trivia(self):
        self.client.get("/")
