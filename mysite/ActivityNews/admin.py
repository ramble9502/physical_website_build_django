# -*- coding: UTF-8 -*-
from django.contrib import admin

# Register your models here.
from ActivityNews.models import *


class Latest_News_Class(admin.TabularInline):
    model = Latest_News_Class

class WorkShop_News_Upload(admin.TabularInline):
	model=WorkShop_News_Upload
		

class Latest_News_Class(admin.ModelAdmin):
    inlines = [Latest_News_Class, ]


class WorkShop_News_Class(admin.ModelAdmin):
    inlines = [WorkShop_News_Upload, ]


admin.site.register(Latest_News, Latest_News_Class)
admin.site.register(WorkShop_News, WorkShop_News_Class)
admin.site.register(Finished_Special_Activity)
admin.site.register(Marqueecontrol)