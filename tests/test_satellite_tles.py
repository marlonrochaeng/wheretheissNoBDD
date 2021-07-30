from entities.satellites import Satellites
import pytest


@pytest.mark.parametrize("id", [(25544)])
def test_satellite_tle(id):
    s = Satellites()
    response = s.get_tles(id)

    assert response['code'] == 200
    for _, value in response['request_info'].items():
        if value is None:
            assert False


@pytest.mark.parametrize("id,format", [(25544,'text')])
def test_satellite_tles_text(id, format):
    s = Satellites()
    response = s.get_tles(id, format)

    assert response['code'] == 200
    assert 'ISS (ZARYA)' in response['request_info']