# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime
# Create your models here.
#----------父類別


class Upload_File(models.Model):
    file = models.FileField("附件檔案1：", upload_to="university/file", blank=True)
    file2 = models.FileField("附件檔案2：", upload_to="university/file", blank=True)
    filename = models.CharField("附件檔案名稱", max_length=50, blank=True)

    def __unicode__(self):
        return self.filename

#---------課程規劃


class CoursePlan(models.Model):
    title = models.CharField('標題', max_length=50)
    created_time = models.CharField('學年度', max_length=50)

    class Meta:
        db_table = "CoursePlan"
        verbose_name = "上傳課程規劃"
        verbose_name_plural = '課程規劃'

    def __unicode__(self):
        return self.created_time


class CoursePlan_Upload(Upload_File):
    contact = models.ForeignKey(CoursePlan, related_name="courseupload")

    class Meta:
        db_table = 'CoursePlan_Upload'
        verbose_name_plural = '課程規劃檔案'


class Curriculum2(models.Model):
    title = models.CharField('標題', max_length=50)
    created_time = models.CharField('學年度', max_length=50)

    class Meta:
        db_table = "Curriculum2"
        verbose_name = "上傳學期課表"
        verbose_name_plural = "學期課表"

    def __unicode__(self):
        return self.title


class Curriculum_Upload(Upload_File):
    contact = models.ForeignKey(Curriculum2, related_name="curriculumupload")

    class Meta:
        db_table = "Curriculum_Upload"
        verbose_name_plural = "學期課表檔案"


class StudentCorner(models.Model):
    title = models.CharField("標題", max_length=50)

    class Meta:
        db_table = "StudentCorner"
        verbose_name = "上傳學生園地"
        verbose_name_plural = "學生園地"

    def __unicode__(self):
        return self.title


class StudentCorner_Upload(Upload_File):
    contact = models.ForeignKey(StudentCorner, related_name="cornerupload")
    image1 = models.ImageField("圖片1", blank=True, default='')
    image2 = models.ImageField("圖片2", blank=True, default='')
    image3 = models.ImageField("圖片3", blank=True, default='')

    class Meta:
        db_table = "StudentCorner_Upload"
        verbose_name_plural = "學生園地資料上傳"


class Crossdomain(models.Model):
    create_year = models.IntegerField("學年度", default=1)
    create_date = models.DateField("公布日期", default=datetime.date.today)
    file = models.FileField("跨領域學分檔案1", upload_to="master/file", blank=True)
    file2 = models.FileField("跨領域學分檔案2", upload_to="master/file", blank=True)
    crosstitle = models.CharField("跨領域學分名稱", max_length=50)

    class Meta:
        db_table = "Crossdomain"
        verbose_name = "上傳跨領域學分學程"
        verbose_name_plural = "跨領域學分學程"

    def __unicode__(self):
        return self.crosstitle
