# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#----------父類別


class Upload_File(models.Model):
    file = models.FileField("附件檔案1", upload_to="masternight/file", blank=True)
    file2 = models.FileField("附件檔案2", upload_to="masternight/file", blank=True)
    filename = models.CharField("附件檔案名稱", max_length=50)

    def __unicode__(self):
        return self.filename

# 碩專班包含：1.課程架構。修業要點 2.學位考試表格下載 3.研討資訊


class NCourse_Architecture(models.Model):
    character = models.TextField("特色簡介", max_length=300)
    architecture = models.TextField("課程架構", max_length=300)

    class Meta:
        db_table = "NCourse_Architectur"
        verbose_name = "上傳課程架構。修業要點"
        verbose_name_plural = "課程架構。修業要點"

    def __unicode__(self):
        return self.character


class NCourse_Architecture_Upload(Upload_File):
    contact = models.ForeignKey(NCourse_Architecture,related_name="ncourse")

    class Meta:
        db_table = "NCourse_Architecture_Upload"
        verbose_name_plural = "課程架構。修業要點檔案"


class NBachelor_Test(models.Model):
    FILECLASSS_CHOICES = (
        (1, '學位考試相關檔案下載'),
        (2, '研究計畫口試相關檔案'),
        (3, '論文口試相關檔案'),
    )
    filetitle = models.IntegerField("檔案類別", choices=FILECLASSS_CHOICES)

    class Meta:
        db_table = "NBachelor_Test"
        verbose_name = "上傳學位考試表格"
        verbose_name_plural = "學位考試表格下載"

    def __unicode__(self):
        return self.filetitle


class NBachelor_Test_Upload(Upload_File):
    contact = models.ForeignKey(NBachelor_Test,related_name="nbachelor")

    class Meta:
        db_table = "NBachelor_Test_Upload"
        verbose_name = "學位考試表格檔案"


class NSeminar_Information(models.Model):
    name = models.CharField('標題名稱', max_length=50)
    file1 = models.FileField("附件檔案1", upload_to="masternight/file", blank=True)
    file2 = models.FileField("附件檔案2", upload_to="masternight/file", blank=True)
    link = models.URLField("連結")

    class Meta:
        db_table = "NSeminar_Information"
        verbose_name = "上傳研討會資訊"
        verbose_name_plural = "研討會資訊"

    def __unicode__(self):
        return self.name
