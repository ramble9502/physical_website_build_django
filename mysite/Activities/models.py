# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 活動集錦包含學術與體育活動和活動照片
#--------父類別


class Upload_Image(models.Model):
    image = models.ImageField("照片上傳", upload_to='activities/image')

    def __unicode__(self):
        return str(self.image)


class AcademicObjects(models.Model):
    year = models.CharField("學年度", max_length=10)
    FILECALSS_CHOICE = (
        ('研討會與研習', '研討會與研習'),
        ('專題演講', '專題演講'),
        ('體育表演會', '體育表演會'),
    )
    filetitle = models.CharField(
        "檔案類別", choices=FILECALSS_CHOICE, max_length=10)

    class Meta:
        db_table = "AcademicObjects"
        verbose_name = "上傳活動年度與項目配置"
        verbose_name_plural = "活動年度與項目配置"

    def __unicode__(self):
        return self.filetitle + self.year


class AcademicActivities(models.Model):
    contact = models.ForeignKey(AcademicObjects, related_name="activities")
    date = models.DateField("活動日期")
    name = models.CharField("活動名稱", max_length=100)
    speaker = models.CharField("演講者", max_length=50, blank=True)
    place = models.CharField("地點", max_length=50, blank=True)

    class Meta:
        db_table = "AcademicActivities"
        verbose_name = "上傳活動內容"
        verbose_name_plural = "活動內容"

    def __unicode__(self):
        return self.name


class AcademicUpload(Upload_Image):
    contact = models.ForeignKey(
        AcademicActivities, related_name="academicimage")

    class Meta:
        db_table = "AcademicUpload"
        verbose_name = "活動照片"
