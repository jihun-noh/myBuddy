import json
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from third_party_api import KhoaApi
from location.serializers import ObservationPostSerializer
from location.models import ObservationPost

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')

@register_job(scheduler, 'interval', seconds=60)
def insert_observation_post_schedule():
    print('Request KHOA to get Observation Post')
    khoa_api = KhoaApi()
    res = khoa_api.khoa_get_observation_post()
    res_dict = json.loads(res.text)
    if 'error' in res_dict['result']:
        print('api error : ' + res.text)
        return
    print('The number of Observation Post is [{}]'.format(len(res_dict['result']['data'])))
    for data in res_dict['result']['data']:
        queryset = ObservationPost.objects.filter(obs_post_id=data['obs_post_id'])
        if queryset.exists():
            continue
        else:
            serializer = ObservationPostSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print('insert ObservationPost -- ' + data['obs_post_id'])
            else:
                print(serializer.errors)
                print('data : ' + data)

register_events(scheduler)
scheduler.start()
print("Scheduler started!")


# 스케줄링의 적용함수 (cron)
# 0:00, 6:00, 12:00, 18:00 정시에 실행
#@register_job(scheduler, "cron", hour='0,6,12,18')
