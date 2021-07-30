from typing import Dict
import requests
from utils.utils import Utils


class Satellites():
    def __init__(self) -> None:
        self.base_uri = 'https://api.wheretheiss.at/v1/satellites'
        self.pos_uri = 'https://api.wheretheiss.at/v1/coordinates'

    def get_satellites(self) -> Dict:
        request = requests.get(self.base_uri)
        return {'code': request.status_code, 'request_info': request.json()}

    def get_by_id(self, id) -> Dict:
        request = requests.get(f'{self.base_uri}/{id}')
        return {'code': request.status_code, 'request_info': request.json()}

    def get_positions(self, id, timestamp, unit) -> Dict:
        timestamp = Utils.convert_list_to_string(timestamp)

        request = requests.get(
            f'{self.base_uri}/{id}/positions?timestamps={timestamp}&units={unit}')
        return {'code': request.status_code, 'request_info': request.json()}

    def get_tles(self, id, response_format=None) -> Dict:
        uri = f'{self.base_uri}/{id}/tles' if response_format is None else f'{self.base_uri}/{id}/tles?format=text'

        request = requests.get(uri)
        return {'code': request.status_code, 'request_info': request.json() if response_format is None else request.text}

    def get_position_info(self, coordinates):
        coordinates = Utils.convert_list_to_string(coordinates)
        print(f'{self.pos_uri}/{coordinates}')
        request = requests.get(f'{self.pos_uri}/{coordinates}')
        return {'code': request.status_code, 'request_info': request.json()}
