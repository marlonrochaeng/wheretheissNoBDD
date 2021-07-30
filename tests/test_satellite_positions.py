from entities.satellites import Satellites
import pytest
import json


@pytest.mark.parametrize("id,timestamp,unit", [(25544, [1436029892, 1436029902, 1446019305, 1448019409], 'miles')])
def test_satellite_positions(id, timestamp, unit):
    s = Satellites()
    data_under_test = json.load(open('data/satellite_positions.json'))

    response = s.get_positions(id, timestamp, unit)
    assert data_under_test['code'] == response['code']
    assert data_under_test['request_info'] == response['request_info']


@pytest.mark.parametrize("id,timestamp,unit,request_info", [(13512, [1436029892, 1436029902, 1446019305, 1448019409], 'miles', {'error': 'satellite not found', 'status': 404})])
def test_satellite_positions_wrong_id(id, timestamp, unit, request_info):
    s = Satellites()
    response = s.get_positions(id, timestamp, unit)

    assert response['code'] == 404
    assert response['request_info'] == request_info

@pytest.mark.parametrize("id,timestamp,unit,quantity", [(25544, [1436029892, 1436029902, 1446019305, 1448019409], 'miles',4),(25544, [1436029892, 1436029902], 'miles',2)])
def test_satellite_positions_correct_quantity(id, timestamp, unit, quantity):
    s = Satellites()

    response = s.get_positions(id, timestamp, unit)
    assert len(response['request_info']) == quantity