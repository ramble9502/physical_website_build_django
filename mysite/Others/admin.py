# -*- coding: UTF-8 -*-
from django.contrib import admin
from Others.models import *
# Register your models here.


class Honorannounce_Upload(admin.TabularInline):
    model = Honorannounce_Upload


class Honorannounce_Class(admin.ModelAdmin):
    inlines = [Honorannounce_Upload]


class AlumniAccociation_Upload(admin.TabularInline):
    model = AlumniAccociation_Upload


class AlumniAccociation_Class(admin.ModelAdmin):
    inlines = [AlumniAccociation_Upload]

admin.site.register(Honorannounce, Honorannounce_Class)
admin.site.register(StuAccociation)
admin.site.register(AlumniAccociation, AlumniAccociation_Class)
