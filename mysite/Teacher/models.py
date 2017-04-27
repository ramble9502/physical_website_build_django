# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#----------師資部分：專任師資、兼任師資


class Teacher(models.Model):
    name = models.CharField("姓名", max_length=10)
    telephone_extension = models.CharField("分機", max_length=20, blank=True)
    job = models.CharField("教職名稱", max_length=50)
    Email = models.CharField(max_length=50)
    photo = models.ImageField("大頭貼", upload_to="teacher/image", blank=True)
    education = models.CharField("學歷", max_length=100, blank=True)
    specialty = models.CharField("專長", max_length=100, blank=True)
    course = models.CharField("課程", max_length=100, blank=True)

    def __unicode__(self):
        return self.name


class Fulltime_Teacher(Teacher):

    class Meta:
        db_table = "Fulltime_Teacher"
        verbose_name = "上傳教授資訊"
        verbose_name_plural = "專任師資"


class Parttime_Teacher(Teacher):
    experience = models.TextField('經歷', max_length=200, default='',blank=True)
    year=models.CharField("最新年度",max_length=50,default='',blank=True)
    class Meta:
        db_table = "Parttime_Teacher"
        verbose_name = "上傳教師資訊"
        verbose_name_plural = "兼任師資"


class Periodical1(models.Model):
    contact = models.ForeignKey(Fulltime_Teacher, related_name="periodical1")
    title = models.CharField("名稱", max_length=500, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "Periodical1"
        verbose_name_plural = "期刊論文"


class Periodical2(models.Model):
    contact = models.ForeignKey(Parttime_Teacher, related_name="periodical2")
    title = models.CharField("名稱", max_length=500, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "Periodical2"
        verbose_name_plural = "期刊論文"


class Seminar1(models.Model):
    contact = models.ForeignKey(Fulltime_Teacher, related_name="seminar1")
    title = models.CharField("名稱", max_length=500, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "Seminar1"
        verbose_name_plural = "研討會論文"


class Seminar2(models.Model):
    contact = models.ForeignKey(Parttime_Teacher, related_name="seminar2")
    title = models.CharField("名稱", max_length=500, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "Seminar2"
        verbose_name_plural = "研討會論文"


class Book1(models.Model):
    contact = models.ForeignKey(Fulltime_Teacher, related_name="book1")
    title = models.CharField("名稱", max_length=500, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "Book1"
        verbose_name_plural = "專書"


class Book2(models.Model):
    contact = models.ForeignKey(Parttime_Teacher, related_name="book2")
    title = models.CharField("名稱", max_length=500,
                             blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "Book2"
        verbose_name_plural = "專書"

class Yearsigned(models.Model):
    year=models.IntegerField("(數字)學年度：年度+學期")
    title=models.CharField("學年度：",max_length=50)
    contact=models.ManyToManyField(Parttime_Teacher)
    def __unicode__(self):
        return self.title
    class Meta:
        db_table="Yearsigned"
        verbose_name_plural="學年度兼任老師名單"
        verbose_name="上傳學年度兼任老師名單"

        