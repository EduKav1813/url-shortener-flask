class TestRegister:

    headers = {
        "Content-type": "application/json",
        "Accept": "application/json",
    }

    def test_register_url(self, client):
        response = client.post(
            "register/",
            headers=self.headers,
            json={"url": "https://www.google.com/search/"},
        )
        assert response.status_code == 200, "Response should return code 200"
