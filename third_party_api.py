import requests
from enum import Enum
from django.conf import settings

class KakaoApi():
    def __init__(self):
        self.kakao_rest_app_key = settings.KAKAO_REST_APP_KEY

    def kakao_get_region_code(self, x, y):
        headers = {'Authorization':'KakaoAK ' + self.kakao_rest_app_key}
        params = {'x':x, 'y':y}
        url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json'
        res = requests.get(url, headers=headers, params=params)
        return res

class KhoaApi():
    class ObsCode(Enum):
        DT = 'tideObsRecent';   # 조위관측소
        IE = 'tideObsRecent';   # 해양관측부이
        TW = 'buObsRecent';
        HB = 'buObsRecent';
        KG = 'buObsRecent';
        RD = 'buObsRecent';

    def __init__(self):
        self.service_key = settings.KHOA_SERVICE_KEY

    def khoa_get_sea_state(self, obs_code):
        data_type = self.ObsCode[obs_code[0:2]].value
        params = {'ServiceKey':self.service_key, 'ObsCode':obs_code, 'ResultType':'json'}
        url = 'http://www.khoa.go.kr/oceangrid/grid/api/{}/search.do'.format(data_type)
        res = requests.get(url, params=params)
        return res

    def khoa_get_observation_post(self):
        params = {'ServiceKey':self.service_key, 'ResultType':'json'}
        url = 'http://www.khoa.go.kr/oceangrid/grid/api/ObsServiceObj/search.do'
        res = requests.get(url, params=params)
        return res
