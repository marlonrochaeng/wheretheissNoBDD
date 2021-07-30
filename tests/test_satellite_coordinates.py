from entities.satellites import Satellites
import pytest
import json

@pytest.mark.parametrize("coordinate", [([37.795517,-122.393693])])
def test_coordinates(coordinate):
    s = Satellites()
    data_under_test = json.load(open('data/satellite_coordinate.json'))

    response = s.get_position_info(coordinate)

    assert data_under_test['code'] == response['code']
    assert data_under_test['request_info'] == response['request_info']
