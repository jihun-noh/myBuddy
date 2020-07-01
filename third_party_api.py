import requests
from django.conf import settings

class KakaoApi():
    def __init__(self):
        self.kakao_rest_app_key = settings.KAKAO_REST_APP_KEY

    def kakao_get_region_code(self, x, y):
        headers = {'Authorization':'KakaoAK ' + self.kakao_rest_app_key}
        params = {'x':x, 'y':y}
        res = requests.get('https://dapi.kakao.com/v2/local/geo/coord2regioncode.json', headers=headers, params=params)
        return res

class KhoaApi():
    def __init__(self):
        self.service_key = settings.KHOA_SERVICE_KEY

    def khoa_get_sea_state(self, obs_code, date):
        params = {'ServiceKey':self.service_key, 'ObsCode':obs_code, 'Date':date, 'ResultType':'json'}
        res = requests.get('http://www.khoa.go.kr/oceangrid/grid/api/tideObsTemp/search.do', params=params)
        return res

    def khoa_get_observation_post(self):
        params = {'ServiceKey':self.service_key, 'ResultType':'json'}
        res = requests.get('http://www.khoa.go.kr/oceangrid/grid/api/ObsServiceObj/search.do', params=params)
        return res
