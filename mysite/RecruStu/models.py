#!-*-coding=utf8-*-
from __future__ import unicode_literals
from django import forms
from django.db import models

# Create your models here.
#----------父類別


class Upload_File(models.Model):
    file1 = models.FileField(
        "附件檔案1:", upload_to="recrustu/file", blank=True)
    file2 = models.FileField(
        "附件檔案2:", upload_to="recrustu/file", blank=True)
    filename = models.CharField("附件檔案名稱", max_length=50, blank=True)

    def __unicode__(self):
        return self.filename


#------------------------招生資訊
# 招生資訊包含：大學-運動績優單獨招生、高中生申請入學、大學考試入學分發、轉學考
#--------------研究所-碩士班、碩專班、榜單專區
#--------------交通資訊、新生入學專區


#----大學生
class Sport_Excellent_Admission(models.Model):
    title = models.CharField('標題(學年度)：', max_length=15)
    created_time = models.CharField('學年度(數字)', max_length=10)

    class Meta:
        db_table = "Sport_Excellent_Admission"
        verbose_name = "上傳運動績優單獨招生"
        verbose_name_plural = "運動績優單獨招生"

    def __unicode__(self):
        return self.title


class Sport_Admission_Upload(Upload_File):
    contact = models.ForeignKey(
        Sport_Excellent_Admission, related_name='sportad')

    class Meta:
        db_table = "Sport_Admission_Upload"
        verbose_name_plural = "上傳招生訊息"


class Senior_Admission(models.Model):
    title = models.CharField("標題(學年度)：", max_length=100)

    class Meta:
        db_table = "Senior_Admission"
        verbose_name = "上傳高中生申請入學資訊"
        verbose_name_plural = "高中生申請入學"

    def __unicode__(self):
        return self.title


class Seninor_Upload(Upload_File):
    contact = models.ForeignKey(Senior_Admission, related_name='seninorup')
    image = models.ImageField(
        "照片上傳", upload_to='recrustu/image', blank=True)

    class Meta:
        db_table = "Seninor_Upload"
        verbose_name_plural = "高中申請入學檔案"


class Senior_Distribution(models.Model):
    title = models.CharField("標題(學年度)：", max_length=100)

    class Meta:
        db_table = "Senior_Distribution"
        verbose_name = "上傳大學考試入學分發"
        verbose_name_plural = "大學考試入學分發"


class Seninor2_Upload(Upload_File):
    contact = models.ForeignKey(Senior_Distribution, related_name='seninor2up')
    image = models.ImageField(
        "照片上傳", upload_to='recrustu/image', blank=True)

    class Meta:
        db_table = "Seninor2_Upload"
        verbose_name_plural = "大學考試入學檔案"

#-----轉學考


class Transfer_Test_Detail(models.Model):
    project = models.CharField("測驗項目", max_length=50, blank=True)
    description = models.TextField("測驗說明", max_length=500, blank=True)

    class Meta:
        db_table = "Transfer_Test_Detail"
        verbose_name_plural = "轉學考細項目"

    def __unicode__(self):
        return self.project


class Transfer_Test(models.Model):
    contact = models.ManyToManyField(
        Transfer_Test_Detail, related_name='transtestdetail')
    title = models.TextField("轉學考招生標題", max_length=200)
    place = models.TextField("招生名額", max_length=100, blank=True)
    commonsubject = models.TextField("共同科目", max_length=50, blank=True)
    profesubject = models.TextField("專業科目", max_length=150, blank=True)
    achievement = models.TextField("成績採計方式", max_length=150, blank=True)
    order = models.TextField("同分錄取順序", max_length=150, blank=True)

    class Meta:
        db_table = "Transfer_Test"
        verbose_name = "上傳轉學考資料"
        verbose_name_plural = "轉學考"

    def __unicode__(self):
        return self.title


class Transfer_Test_Upload(Upload_File):
    contact = models.ForeignKey(Transfer_Test, related_name='transtestu')

    class Meta:
        db_table = "Transfer_Test_Upload"
        verbose_name_plural = "轉學考檔案"


#------碩士/專班
class Master_Admission(models.Model):
    title = models.CharField('標題(學年度)：', max_length=15)
    created_time = models.CharField('學年度(數字)：', max_length=10)

    class Meta:
        db_table = "Master_Admission"
        verbose_name = "上傳碩士班招生資訊"
        verbose_name_plural = "碩士班招生"

    def __unicode__(self):
        return self.title


class Master_Admission_Test(Upload_File):
    contact = models.ForeignKey(Master_Admission, related_name='mastertest')

    class Meta:
        db_table = "Master_Admission_Test"
        verbose_name_plural = "碩士班入學考試"


class Master_Audition(Upload_File):
    contact = models.ForeignKey(Master_Admission, related_name='masteraudi')

    class Meta:
        db_table = "Master_Audition"
        verbose_name_plural = "碩士班甄試"


class Master_night2(models.Model):
    title = models.CharField('標題(學年度)：', max_length=15)
    created_time = models.CharField('學年度(數字)：', max_length=10)

    class Meta:
        db_table = "Master_night2"
        verbose_name = "上傳碩專班招生資訊"
        verbose_name_plural = "碩專班招生"

    def __unicode__(self):
        return self.title


class MasterNight_Audition2(Upload_File):
    contact = models.ForeignKey(Master_night2, related_name='mastnighaudi')

    class Meta:
        db_table = "MasterNight_Audition2"
        verbose_name_plural = "碩專班甄試"


class Traffic_Information(models.Model):
    FILECLASS_CHOICE = (
        (1, '臺南大學交通資訊（府城校區）'),
        (2, '臺南大學交通資訊（榮譽教學中心）')
    )
    name = models.IntegerField("台南大學校區(交通)：", choices=FILECLASS_CHOICE)

    class Meta:
        db_table = "Traffic_Information"
        verbose_name = "上傳交通資訊"
        verbose_name_plural = "交通資訊"

    def __unicode__(self):
        return str(self.name)


class Traffic_Method(models.Model):
    contact = models.ForeignKey(Traffic_Information, related_name='trafmeth')
    method = models.CharField("交通方法", max_length=10, blank=True)
    process = models.TextField("交通過程", max_length=250, blank=True)

    class Meta:
        db_table = "Traffic_Method"
        verbose_name_plural = "到達方法"


#--------榜單專區
class List(models.Model):
    title = models.CharField('榜單名稱', max_length=20)
    discription = models.TextField('說明(包含報到等)', max_length=800)

    class Meta:
        db_table = "List"
        verbose_name_plural = "各項考試榜單"

    def __unicode__(self):
        return self.title


class List_Upload(Upload_File):
    contact = models.ForeignKey(List, related_name='listupload')

    class Meta:
        db_table = "List_Upload"
        verbose_name_plural = "榜單資料"


#-------最後一項:新生入學專區
