from django.http import HttpResponse
from django.shortcuts import *
from django.shortcuts import render, redirect
from merge.db import Dao
import json


class View(object):
    def __init__(self):
        self.dao = Dao()
        self.fair_html = 'index.html'
        self.seminar_html = 'seminar.html'

    def fair_data(self, request):
        result = self.dao.get_fail()
        res = {
            "aaData": result,
        }
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")

    def seminar_data(self, request):
        result = self.dao.get_serminar()
        res = {
            "aaData": result,
        }
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")

    def fair(self, request):
        return render(request, self.fair_html)

    def seminar(self, request):
        return render(request, self.seminar_html)
