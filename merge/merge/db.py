import json
from django.http import HttpResponse

from model.models import Fail, Seminar
from merge.settings import DATA_TIMES
import time
import datetime
class Dao(object):
    def __init__(self):
        self.result = ''

    def get_fail(self):
        self.result = Fail.objects.values().all()
        if DATA_TIMES is False:
            return list(self.result)
        else:
            r = []
            rusult = list(self.result)
            for i in rusult:
                data_time = i.get('Fail_time')[:10]
                try:
                    int_time = int(data_time.replace('-',''))
                    today_time = datetime.datetime.today()
                    yesterday = int(str(today_time - datetime.timedelta(days=1))[:10].replace('-',''))
                    if int_time-yesterday >= 0:
                        r.append(i)
                except:
                    pass
            return r

    def get_serminar(self):
        self.result = Seminar.objects.values().all()
        if DATA_TIMES is False:
            return list(self.result)
        else:
            r = []
            rusult = list(self.result)
            for i in rusult:
                data_time = i.get('Seminar_time')[:10]
                try:
                    int_time = int(data_time.replace('-',''))
                    today_time = datetime.datetime.today()
                    yesterday = int(str(today_time - datetime.timedelta(days=1))[:10].replace('-',''))
                    if int_time-yesterday >= 0:
                        r.append(i)
                except:
                    pass
            return r


    def select_info(self, info):  # 模糊查询
        Seminar.objects.filter(Seminar_college_contains=info)
        Seminar.objects.filter(Seminar_title_contains=info)
        return 1
