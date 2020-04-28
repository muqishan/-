

# Create your models here.
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from django.db import models


class Seminar(models.Model):  # 宣讲会及小型招聘会(单个公司)
    # define the fields for your item here like:
    # name = scrapy.Field()
    Seminar_id = models.AutoField(primary_key=True)
    Seminar_title = models.CharField(max_length=255, null=False)  # 宣讲会标题
    Seminar_time = models.CharField(max_length=255, null=False)  # 宣讲会时间段
    Seminar_site = models.CharField(max_length=100, null=False)  # 宣讲会地点
    Seminar_college = models.CharField(max_length=255, null=False)  # 宣讲会举办学校
    Seminar_partment = models.CharField(max_length=255, null=False)  # 宣讲会主办单位
    Seminar_url = models.CharField(max_length=255, null=False)  # 宣讲会链接


class Fail(models.Model):  # 大型招聘会
    Fail_id = models.AutoField(primary_key=True)
    Fail_college = models.CharField(max_length=255, null=False)  # 宣讲会举报学校
    Fail_partment = models.CharField(max_length=255, null=False)  # 宣讲会举办学校
    Fail_title = models.CharField(max_length=255, null=False)  # 招聘会的标题
    Fail_time = models.CharField(max_length=255, null=False)  # 招聘会日期
    Fail_detail_time = models.CharField(max_length=255, null=False)  # 详细时间
    Fail_site = models.CharField(max_length=255, null=False)  # 宣讲会地点
    Fail_url = models.CharField(max_length=255, null=False)  # 宣讲会链接
