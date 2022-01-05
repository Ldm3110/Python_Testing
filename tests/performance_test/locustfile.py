from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def index(self):
        self.client.get('/')

    @task
    def show_summary(self):
        self.client.post('/showSummary', data={'email': 'admin@irontemple.com'})

    @task
    def book(self):
        self.client.get("/book/Spring%20Festival/Iron%20Temple")

    @task
    def purchase_place(self):
        data = {
            'club': 'Iron Temple',
            'competition': 'Spring Festival',
            'places': 1
        }
        self.client.post("/purchasePlaces", data=data)

    @task
    def logout(self):
        self.client.get("/logout")