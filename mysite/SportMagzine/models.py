# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models


class UploadFile(models.Model):
    filename = models.CharField("檔案標題名稱", max_length=100)
    file1 = models.FileField(
        "附件檔案1", upload_to='sportmagzine/file', blank=True)
    file2 = models.FileField(
        "附件檔案1", upload_to='sportmagzine/file', blank=True)

    def __unicode__(self):
        return self.filename


# Create your models here.
class Regulation(models.Model):
    topic = models.TextField("體育學報主題", max_length=500)

    def __unicode__(self):
        return self.topic

    class Meta:
        db_table = 'Regulation'
        verbose_name = '上傳體育學報審查內容'
        verbose_name_plural = '體育學報審查內容'


class Regulation_Upload(UploadFile):
    contact = models.ForeignKey(Regulation, related_name="regulation")

    class Meta:
        db_table = 'Regulation_Upload'
        verbose_name_plural = '相關檔案閱覽與下載'


class Magzine(models.Model):
    FIlECLASS_CHOICES = (
        (1, '《南大體育學報》（新版刊物）概覽'),
        (2, '《南大體育學報》（舊版刊物）概覽')
    )
    headline = models.IntegerField("檔案類別", choices=FIlECLASS_CHOICES)
    filetitle = models.CharField("刊物名稱", max_length=50)
    file = models.FileField(
        "刊物上傳1:", upload_to='sportmagzine/magzine', blank=True)
    file2 = models.FileField(
        "刊物上傳2:", upload_to='sportmagzine/magzine', blank=True)

    class Meta:
        db_table = "Magzine"
        verbose_name = "上傳刊物內容"
        verbose_name_plural = "體育學報刊物"
