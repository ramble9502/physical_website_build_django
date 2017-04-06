# -*- coding: UTF-8 -*-
from django.contrib import admin
from Activities.models import *
# Register your models here.





class AcademicUpload(admin.TabularInline):
    model = AcademicUpload


class AcademicActivities_Class(admin.ModelAdmin):
    inlines = [AcademicUpload]




admin.site.register(AcademicActivities, AcademicActivities_Class)
admin.site.register(AcademicObjects)
