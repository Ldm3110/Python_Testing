class TestLogin:
    def test_connection_should_return_status_200(self, client):
        response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
        assert response.status_code == 200

    def test_connection_with_bad_mail_return_status_500(self, client):
        response = client.post('/showSummary', data={'email': 'test@test.com'})
        assert response.status_code == 500

    def test_connection_with_bad_mail_return_message(self, client):
        message_expected = "This email is invalid or does not exist ! Please try again"
        response = client.post('/showSummary', data={'email': 'test@test.com'})
        data = response.data.decode()
        assert message_expected in data
