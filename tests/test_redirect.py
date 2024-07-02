class TestRedirect:

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

    def test_redirect(self, client):
        response = self._register_url(
            client, url="https://www.google.com/search/"
        )
        assert response.status_code == 200, "Response should return code 200"
        code = response.json["code"]

        response = client.get(f"redirect/{code}", headers=self.headers)
        assert (
            response.status_code == 302
        ), "Response should return code 302 (Redirect)"
        redirected_url = response.headers["Location"]
        assert redirected_url == "https://www.google.com/search/"

    def test_redirect_nonexistent(self, client):
        response = client.get("redirect/ABCD1234", headers=self.headers)
        assert response.status_code == 404, "Response should return code 404"
