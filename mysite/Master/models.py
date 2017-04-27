# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

#----------父類別


class Upload_File(models.Model):
    file = models.FileField("附件檔案1", upload_to="master/file", blank=True)
    file2 = models.FileField("附件檔案2", upload_to="master/file", blank=True)
    filename = models.CharField("附件檔案名稱", max_length=50)

    def __unicode__(self):
        return self.filename

# 碩士班有7小項目:
# 1.課程架構。修業要點2.學位考試表格3.研討資訊
# 4.研究所讀書會5.在校論文發表6.畢業論文發表7.考古題


class Course_Architecture(models.Model):
    filetitle = models.CharField("檔案名稱", max_length=50)

    class Meta:
        db_table = "Course_Architectur"
        verbose_name = "上傳課程架構。修業要點"
        verbose_name_plural = "課程架構。修業要點"

    def __unicode__(self):
        return self.filetitle


class Course_Architecture_Upload(Upload_File):
    contact = models.ForeignKey(
        Course_Architecture, related_name="coursearchi")

    class Meta:
        db_table = "Course_Architecture_Upload"
        verbose_name_plural = "課程架構。修業要點檔案"


class Bachelor_Test(models.Model):
    FILECLASSS_CHOICES = (
        ('學位考試相關檔案下載', '學位考試相關檔案下載'),
        ('研究計畫口試相關檔案', '研究計畫口試相關檔案'),
        ('論文口試相關檔案', '論文口試相關檔案'),
    )
    filetitle = models.CharField(
        "檔案類別", choices=FILECLASSS_CHOICES, max_length=50)

    class Meta:
        db_table = "Bachelor_Test"
        verbose_name = "上傳學位考試表格"
        verbose_name_plural = "學位考試表格下載"

    def __unicode__(self):
        return self.filetitle


class Bachelor_Test_Upload(Upload_File):
    contact = models.ForeignKey(Bachelor_Test, related_name="bachelor")

    class Meta:
        db_table = "Bachelor_Test_Upload"
        verbose_name = "學位考試表格檔案"


class Seminar_Information(models.Model):
    name = models.CharField('標題名稱', max_length=50)
    file1 = models.FileField("附件檔案1", upload_to="master/file", blank=True)
    file2 = models.FileField("附件檔案2", upload_to="master/file", blank=True)
    image = models.ImageField(
        "代表圖片", upload_to="master/image", blank=True, default="")
    link = models.URLField("連結", blank=True)

    class Meta:
        db_table = "Seminar_Information"
        verbose_name = "上傳研討會資訊"
        verbose_name_plural = "研討會資訊"

    def __unicode__(self):
        return self.name


class Study_Group(models.Model):
    title = models.CharField('標題名稱', max_length=50)
    year = models.IntegerField("學年度", default=1)

    class Meta:
        db_table = "Study_Group"
        verbose_name = "上傳研究生讀書會"
        verbose_name_plural = "碩士班研究生讀書會"

    def __unicode__(self):
        return self.title


class Study_Group_Upload(Upload_File):
    contact = models.ForeignKey(Study_Group, related_name="studygroup")

    class Meta:
        db_table = "Study_Group_Upload"
        verbose_name_plural = "研究生讀書會檔案"


class Schoolpaper(models.Model):
    name = models.CharField("學年度/標題", max_length=50)
    year = models.IntegerField("學年度", default=1)

    class Meta:
        db_table = "Schoolpaper"
        verbose_name = "上傳在校論文資料"
        verbose_name_plural = "在校論文發表"

    def __unicode__(self):
        return self.name


class Schoolpaper_Upload(models.Model):
    contact = models.ForeignKey(Schoolpaper, related_name="schoolpaper")
    date = models.DateField("日期")
    seminar = models.TextField("研討會名稱", max_length=500)
    papertopic = models.TextField("論文題目", max_length=100)
    publication = models.CharField("發表方式", max_length=100)
    author = models.CharField("發表人(第一作者)", max_length=4)
    advisor = models.CharField("指導教授", max_length=50)

    class Meta:
        db_table = "Schoolpaper_Upload"
        verbose_name_plural = "當年度發表資料"


class Graduatedpaper(models.Model):
    name = models.CharField("學年度/標題", max_length=50)
    year = models.IntegerField("學年度", default=1)

    class Meta:
        db_table = "Graduatedpaper"
        verbose_name = "上傳畢業論文資料"
        verbose_name_plural = "畢業論文發表"

    def __unicode__(self):
        return self.name


class Graduatedpaper_Upload(models.Model):
    contact = models.ForeignKey(Graduatedpaper, related_name="graduatedpaper")
    author = models.CharField("發表人(第一作者)", max_length=50, blank=True)
    papertopic = models.CharField("論文題目", max_length=50, blank=True)
    advisor = models.CharField("指導教授", max_length=50, blank=True)
    graduatedyear = models.CharField("畢業年度", max_length=50, blank=True)

    class Meta:
        db_table = "Graduatedpaper_Upload"
        verbose_name_plural = "當年度發表資料"

#------------考古題目前沒有


class Archeology(models.Model):
    create_year = models.IntegerField("學年度", default=1)
    create_date = models.DateField("公布日期", default=datetime.date.today)
    file = models.FileField("考古題檔案1", upload_to="master/file", blank=True)
    file2 = models.FileField("考古題檔案2", upload_to="master/file", blank=True)
    archtitle = models.CharField("考古題名稱", max_length=50)

    class Meta:
        db_table = "Archeology"
        verbose_name = "上傳考古題"
        verbose_name_plural = "考古題"

    def __unicode__(self):
        return self.archtitle


class Teachemaster(models.Model):
    FILECLASSS_CHOICES = (
        ('教學碩士班學位考試相關檔案下載', '教學碩士班學位考試相關檔案下載'),
        ('教學碩士班研究計畫口試相關檔案', '教學碩士班研究計畫口試相關檔案'),
        ('教學碩士班論文口試相關檔案', '教學碩士班論文口試相關檔案'),
    )
    filetype = models.CharField(
        "檔案類別", choices=FILECLASSS_CHOICES, max_length=50)

    class Meta:
        db_table = "Teachemaster"
        verbose_name = "上傳教學碩士班表格"
        verbose_name_plural = "教學碩士班表格"

    def __unicode__(self):
        return self.filetype


class Teachemaster_Upload(Upload_File):
    contact = models.ForeignKey(Teachemaster, related_name="teachmaster")

    class Meta:
        db_table = "Teachemaster_Upload"
        verbose_name = "教學碩士班表格檔案"
