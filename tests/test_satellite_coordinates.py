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

@pytest.mark.parametrize("coordinate, request_info", [([91.795517,-192.393693],{'error': 'application error', 'status': 500})])
def test_wrong_coordinates(coordinate, request_info):
    s = Satellites()

    response = s.get_position_info(coordinate)

    assert response['code'] == 500
    assert response['request_info'] == request_info