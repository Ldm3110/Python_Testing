class TestBooking:

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

    def test_user_cannot_reserve_more_than_he_has_points(self, client, test_clubs,
                                                         test_competitions, testing_config):
        test_clubs[0]['points'] = 4
        data = {
            "club": test_clubs[0]["name"],
            "competition": test_competitions[0]["name"],
            "places": 10,
        }
        response = client.post('/purchasePlaces', data=data, follow_redirects=True)
        response_decode = response.data.decode()
        assert "have enough points" in response_decode

    def test_user_cannot_reserve_more_than_available_in_tournament(self, client, test_clubs,
                                                                   test_competitions, testing_config):
        test_competitions[0]['numberOfPlaces'] = 2
        data = {
            "club": test_clubs[0]["name"],
            "competition": test_competitions[0]["name"],
            "places": 4,
        }
        response = client.post('/purchasePlaces', data=data, follow_redirects=True)
        response_decode = response.data.decode()
        assert "enough places !" in response_decode

    def test_user_reserve_places(self, client, test_clubs, test_competitions, testing_config):
        expected_number_of_points = 10
        expected_places_remaining = 12
        data = {
            "club": test_clubs[0]["name"],
            "competition": test_competitions[0]["name"],
            "places": 3,
        }
        client.post('/purchasePlaces', data=data, follow_redirects=True)
        assert test_clubs[0]['points'] == expected_number_of_points
        assert test_competitions[0]['numberOfPlaces'] == expected_places_remaining

    def test_cannot_book_because_tournament_is_ending(self, client, test_clubs, test_competitions, testing_config):
        expected_message = "Tournament Finished"
        data = {
            "email": test_clubs[0]['email'],
            "competition": test_competitions[0]["name"],
        }
        response = client.post("/showSummary", data=data, follow_redirects=True)
        response_decode = response.data.decode()
        print(response_decode)
        assert expected_message in response_decode
