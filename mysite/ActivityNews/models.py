# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import validate_email
import datetime

# Create your models here.

#----------父類別


class Upload_File(models.Model):
    file = models.FileField(
        "附件檔案1:", upload_to="activitynews/file", blank=True)
    file2 = models.FileField(
        "附件檔案2:", upload_to="activitynews/file", blank=True)
    filename = models.CharField("附件檔案名稱:", max_length=50, blank=True)

    def __unicode__(self):
        return unicode(self.filename) or u''

#----------首頁內容:最新消息,研討會研習


class Latest_News(models.Model):
    title = models.CharField("標題：", max_length=30)
    content = models.TextField("主題內容:", blank=True)
    create_date = models.DateField("公布日期", default=datetime.date.today)

    class Meta:
        db_table = "Latest_News"
        verbose_name = "上傳最新訊息"
        verbose_name_plural = "最新訊息公告"

    def __unicode__(self):
        return unicode(self.title) or u''


class WorkShop_News(models.Model):
    title = models.CharField("標題：", max_length=30)
    content = models.TextField("主題內容:", blank=True)
    create_date = models.DateField("公布日期", default=datetime.date.today)

    class Meta:
        db_table = "WorkShop_News"
        verbose_name = "上傳研習訊息"
        verbose_name_plural = "研習訊息公告"

    def __unicode__(self):
        return unicode(self.title) or u''


class WorkShop_News_Upload(Upload_File):
    contact = models.ForeignKey(
        "WorkShop_News", on_delete=models.CASCADE, related_name="workshop")

    def __unicode__(self):
        return unicode(self.contact) or u''


class Latest_News_Class(Upload_File):
    contact = models.ForeignKey(
        "Latest_News", on_delete=models.CASCADE, related_name="latestnews")

    def __unicode__(self):
        return unicode(self.contact) or u''


#----------目前不確定，活動宣傳

class Finished_Special_Activity(models.Model):
    name = models.CharField("標題", max_length=50)
    latest_news = models.TextField("最新消息", max_length=1000)
    file = models.FileField(
        "相關報名檔案", upload_to="activitynews/file", blank=True)
    fans_connect = models.URLField("粉絲團連結", blank=True)
    related_url = models.URLField("活動網址", blank=True)
    create_date = models.DateField("公布日期", default=datetime.date.today)
    image = models.ImageField("代表圖片", upload_to="activitynews/image")

    class Meta:
        db_table = "Finished_Special_Activity"
        verbose_name = "上傳活動訊息"
        verbose_name_plural = "特殊活動"

    def __unicode__(self):
        return self.name


class Linkindex(models.Model):
    jobtitle = models.CharField("相關求職訊息標題", max_length=100)
    link = models.URLField("求職連結", blank=True)
    create_date = models.DateField("公布日期", default=datetime.date.today)

    class Meta:
        db_table = "Linkindex"
        verbose_name = "上傳求職訊息"
        verbose_name_plural = "求職訊息"

    def __unicode__(self):
        return self.jobtitle


class Linkact(models.Model):
    actitle = models.CharField('相關連結名稱', max_length=100)
    actlink = models.URLField('連結', blank=True)
    actimage = models.ImageField('圖片', upload_to="activitynews/image")
    create_date = models.DateField("公布日期", default=datetime.date.today)

    class Meta:
        db_table = "Linkact"
        verbose_name = "上傳相關連結"
        verbose_name_plural = "相關連結"

    def __unicode__(self):
        return self.actitle


class Marqueecontrol(models.Model):
    content = models.CharField("跑馬燈內容", max_length=100)

    def __unicode__(self):
        return unicode(self.content) or u''

    class Meta:
        db_table = "Marqueecontrol"
        verbose_name = "上傳跑馬燈內容"
        verbose_name_plural = "跑馬燈"
