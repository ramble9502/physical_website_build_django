# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#-----父類別


class Upload_File(models.Model):
    file = models.FileField("檔案上傳", upload_to='others/file', blank=True)
    filename = models.CharField("檔案名稱", max_length=100, blank=True)

    def __unicode__(self):
        return self.filename

    # 其他區包含榮譽榜,系學會,系友會


class Honorannounce(models.Model):
    content = models.TextField("榮譽榜內容", max_length=200)

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'Honorannounce'
        verbose_name = '上傳榮譽榜'
        verbose_name_plural = '榮譽榜'


class Honorannounce_Upload(Upload_File):
    contact = models.ForeignKey(Honorannounce, related_name="honor")

    class Meta:
        db_table = 'Honorannounce_Upload'
        verbose_name_plural = "榮譽榜檔案"


class StuAccociation(Upload_File):
    file2 = models.FileField("檔案上傳2", upload_to='others/file', blank=True)

    class Meta:
        db_table = "StuAccociation"
        verbose_name = "上傳系學會"
        verbose_name_plural = "系學會"


class AlumniAccociation(models.Model):
    title = models.CharField("標題", max_length=100, default="")
    headline = models.CharField("大標題", max_length=100)
    sitetitle = models.CharField("側標", max_length=100)

    def __unicode__(self):
        return self.headline

    class Meta:
        db_table = "AlumniAccociation"
        verbose_name = "上傳系友會"
        verbose_name_plural = "系友會"


class AlumniAccociation_Upload(models.Model):
    contact = models.ForeignKey(AlumniAccociation, related_name="alumni")
    title = models.CharField("標題", max_length=100)
    content = models.TextField("內容", max_length=2000)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "AlumniAccociation_Upload"
        verbose_name_plural = "系友會細項"
