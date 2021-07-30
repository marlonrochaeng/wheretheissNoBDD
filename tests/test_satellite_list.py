from entities.satellites import Satellites
import pytest

@pytest.mark.parametrize("code, list_size, request_info", [(200, 1, {'name': 'iss', 'id': 25544})])
def test_satellite_list(code, list_size, request_info):
    s = Satellites()
    
    resposne = s.get_satellites()

    assert resposne['code'] == code
    assert len(resposne['request_info']) == list_size
    assert resposne['request_info'][0] == request_info
