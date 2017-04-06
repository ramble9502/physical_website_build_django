# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
#系所簡介包含：系所特色、教學指南、行政法規、所辦設備、修業規定

# Create your models here.

#----------父類別


class Upload_File(models.Model):
    file = models.FileField("附件檔案", upload_to="departintro/file")
    filename = models.CharField("附件檔案名稱", max_length=50)

    def __unicode__(self):
        return self.filename




#------------系所特色


class Department_Characteristic(models.Model):
    reformation = models.TextField("沿革", max_length=300)
    goal = models.TextField("設立目標", max_length=300)
    ability_pointer = models.TextField("能力指標", max_length=300)
    characteristic = models.TextField("特色", max_length=300)
    future_development = models.TextField("系所未來發展", max_length=300)
    graduate_job = models.TextField("學生畢業出路", max_length=300)

    class Meta:
        db_table = "Department_Characteristic"
        verbose_name = "上傳系所特色"
        verbose_name_plural = "系所特色"

    def __unicode__(self):
        return self.reformation
#-----------教學指南
#直接用html css 編寫???


#------------行政法規

class Legislation(models.Model):

    class Meta:
        db_table = "Legislation"
        verbose_name = "上傳行政法規"
        verbose_name_plural = "行政法規"

class Dep_promotion_Point(Upload_File):
    contact = models.ForeignKey(Legislation,related_name='promotion')

    class Meta:
        db_table = "Dep_promotion_Point"
        verbose_name_plural = "教師升等相關要點"


class Other_Point(Upload_File):
    contact = models.ForeignKey(Legislation,related_name="point")

    class Meta:
        db_table = "Other_Point"
        verbose_name_plural = "其他相關要點"


class Scholarship(Upload_File):
    contact = models.ForeignKey(Legislation,related_name='scholar')

    class Meta:
        db_table = "Scholarship"
        verbose_name_plural = "獎學金相關要點"

#-------------所辦設備


class Equipment(models.Model):
    name = models.CharField("教室名稱", max_length=50)
    description = models.TextField("設備描述", max_length=300)

    class Meta:
        db_table = "Equipment"
        verbose_name = "上傳設備內容"
        verbose_name_plural = "所辦設備"

    def __unicode__(self):
        return self.name

#--------------修業規定
class Their_official_regulations(models.Model):
	name=models.CharField("標題",max_length=50)
	goal=models.TextField("目標",max_length=500)
	regulation=models.TextField("細項",max_length=500)
	class Meta:
		db_table="Their_official_regulations"
		verbose_name="上傳修業規定"
		verbose_name_plural="修業規定"
	def __unicode__(self):
		return self.name
			
