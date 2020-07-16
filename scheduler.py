import json
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from third_party_api import KhoaApi
from location.serializers import ObservationPostSerializer
from location.models import ObservationPost

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')

@register_job(scheduler, 'cron', minute='0')
def insert_observation_post_schedule():
    print('Delete all Observation Posts')
    queryset = ObservationPost.objects.all().delete();
    print('Observation Posts are deleted')
    print('Request KHOA to get Observation Post')
    khoa_api = KhoaApi()
    res = khoa_api.khoa_get_observation_post()
    res_dict = json.loads(res.text)
    if 'error' in res_dict['result']:
        print('api error : ' + res.text)
        return
    print('The number of Observation Post is [{}]'.format(len(res_dict['result']['data'])))
    for data in res_dict['result']['data']:
        serializer = ObservationPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('insert ObservationPost -- ' + data['obs_post_id'])
        else:
            if serializer.errors['obs_lat'][0].code == 'max_decimal_places'\
            or serializer.errors['obs_lon'][0].code == 'max_decimal_places':
                print('revalidation [{}]'.format(serializer.is_valid()))
            else:
                print(serializer.errors)
                print('data : ' + str(data))
    print('Insert Observation Posts is completed')

register_events(scheduler)
scheduler.start()
print("Scheduler started!")


# 스케줄링의 적용함수 (cron)
#@register_job(scheduler, "cron", hour='0,6,12,18')
#@register_job(scheduler, 'interval', seconds=60)
