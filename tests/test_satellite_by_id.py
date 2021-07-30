from entities.satellites import Satellites
import pytest
import json

@pytest.mark.parametrize("id", [(25544)])
def test_satellite_by_correct_id(id):
    s = Satellites()
    data_under_test = json.load(open('data/satellite_by_id.json'))
    
    response = s.get_by_id(id)

    assert data_under_test['code'] == response['code']
    assert data_under_test['request_info']['name'] == response['request_info']['name']
    assert data_under_test['request_info']['units'] == response['request_info']['units']
    for _, value in response['request_info'].items():
        if value is None:
            assert False



@pytest.mark.parametrize("id,code,request_info", [(101, 404, {'error': 'satellite not found', 'status': 404})])
def test_satellite_by_incorrect_id(id, code, request_info):
    s = Satellites()
    
    response = s.get_by_id(id)
    assert code == response['code']
    assert request_info == response['request_info']
