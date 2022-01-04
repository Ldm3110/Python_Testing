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
