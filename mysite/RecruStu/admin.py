# -*- coding: UTF-8 -*-
from django.contrib import admin
from RecruStu.models import *
from django.forms import Textarea
# Register your models here.


class RulesAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {
        'widget': Textarea(attrs={'rows': 3, 'cols': 40})}, }


class RulesAdmin_T(admin.TabularInline):
    formfield_overrides = {models.TextField: {
        'widget': Textarea(attrs={'rows': 4, 'cols': 40})}, }

#父類別


class Sport_Admission_Upload(admin.TabularInline):
    model = Sport_Admission_Upload


class Sport_Excellent_Class(admin.ModelAdmin):
    inlines = [Sport_Admission_Upload]


class Seninor_Upload(admin.TabularInline):
    model = Seninor_Upload


class Senior_Admission_Class(admin.ModelAdmin):
    inlines = [Seninor_Upload]


class Seninor2_Upload(admin.TabularInline):
    model = Seninor2_Upload


class Senior_Distribution_Class(admin.ModelAdmin):
    inlines = [Seninor2_Upload]


class Master_Admission_Test(admin.TabularInline):
    model = Master_Admission_Test


class Master_Audition(admin.TabularInline):
    model = Master_Audition


class Master_Admission_Class(admin.ModelAdmin):
    inlines = [Master_Admission_Test, Master_Audition]


class MasterNight_Audition2(admin.TabularInline):
    model = MasterNight_Audition2


class Master_night_Class(admin.ModelAdmin):
    inlines = [MasterNight_Audition2]


class Traffic_Method(admin.TabularInline):
    model = Traffic_Method


class Traffic_Information_Class(admin.ModelAdmin):
    inlines = [Traffic_Method]



class Transfer_Test_Upload(admin.TabularInline):
    model = Transfer_Test_Upload


class Transfer_Test_Class(RulesAdmin):
    inlines = [Transfer_Test_Upload]


class List_Upload(admin.TabularInline):
    model=List_Upload

class List_Class(admin.ModelAdmin):
    inlines=[List_Upload]
        







admin.site.register(Sport_Excellent_Admission, Sport_Excellent_Class)
admin.site.register(Senior_Distribution, Senior_Distribution_Class)
admin.site.register(Senior_Admission, Senior_Admission_Class)
admin.site.register(Transfer_Test, Transfer_Test_Class)
admin.site.register(Master_Admission, Master_Admission_Class)
admin.site.register(Master_night2, Master_night_Class)
admin.site.register(Traffic_Information, Traffic_Information_Class)
admin.site.register(Transfer_Test_Detail)
admin.site.register(List,List_Class)