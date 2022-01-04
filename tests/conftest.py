import pytest

import server


@pytest.fixture
def client():
    """
    Create a basic client for test
    :return: basic client
    """
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def test_clubs():
    """
    Define a club by default for tests
    :return: default club
    """
    data = [
        {
            "name": "Club Test",
            "email": "test@test.com",
            "points": "13"
        },
    ]
    return data


@pytest.fixture
def test_competitions():
    """
    Define a competition by default for tests
    :return: default competition
    """
    data = [
        {
            "name": "Compet Test",
            "date": "2021-12-23 10:00:00",
            "numberOfPlaces": "15"
        },
    ]
    return data


@pytest.fixture
def testing_config(mocker, test_clubs, test_competitions):
    """
    Configuration of clubs and competitions json for tests
    """
    mocker.patch.object(server, 'clubs', test_clubs)
    mocker.patch.object(server, 'competitions', test_competitions)
