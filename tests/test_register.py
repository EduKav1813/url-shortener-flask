class TestRegister:

    headers = {
        "Content-type": "application/json",
        "Accept": "application/json",
    }

    def _register_url(self, client, url: str):
        return client.post(
            "register/",
            headers=self.headers,
            json={"url": url},
        )

    def test_register_url(self, client):
        response = self._register_url(
            client, url="https://www.google.com/search/"
        )
        assert response.status_code == 200, "Response should return code 200"
        assert (
            response.json["code"] != ""
        ), "Generated short code should NOT be empty"

    def test_register_no_url(self, client):
        response = client.post("register/", headers=self.headers)
        assert response.status_code == 400, "Response should return code 400"

    def test_register_url_twice(self, client):
        # Register the url for the first time
        first_response = self._register_url(
            client, url="https://www.google.com/search/"
        )
        assert (
            first_response.status_code == 200
        ), "Response should return code 200"
        short_code = first_response.json["code"]

        # Try to register the same url
        second_response = self._register_url(
            client, url="https://www.google.com/search/"
        )
        assert (
            second_response.json["code"] == short_code
        ), "Generated short code for the same url should be the same"

    def test_register_two_urls(self, client):
        first_response = self._register_url(
            client, url="https://www.google.com/search/"
        )
        assert (
            first_response.status_code == 200
        ), "Response should return code 200"
        first_code = first_response.json["code"]

        second_response = self._register_url(client, url="https://medium.com")
        assert (
            second_response.json["code"] != first_code
        ), "Code for the second url should be different from the first one"
