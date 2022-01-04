class TestPurchase:

    def test_user_cannot_reserve_more_than_12_places(self, client, test_clubs,
                                                     test_competitions, testing_config):
        data = {
            "club": test_clubs[0]["name"],
            "competition": test_competitions[0]["name"],
            "places": test_clubs[0]["points"],
        }
        response = client.post('/purchasePlaces', data=data, follow_redirects=True)
        response_decode = response.data.decode()
        assert "You cannot reserve more than 12 places sorry !!" in response_decode
