#!-*-coding=utf8-*-
from django.contrib import admin
from Masternight.models import *
# Register your models here.


class NCourse_Architecture_Upload(admin.TabularInline):
    model = NCourse_Architecture_Upload


class NCourse_Architecture_Class(admin.ModelAdmin):
    inlines = [NCourse_Architecture_Upload]


class NBachelor_Test_Upload(admin.TabularInline):
    model = NBachelor_Test_Upload


class NBachelor_Test_Class(admin.ModelAdmin):
    inlines = [NBachelor_Test_Upload]


admin.site.register(NCourse_Architecture, NCourse_Architecture_Class)
admin.site.register(NBachelor_Test,NBachelor_Test_Class)
admin.site.register(NSeminar_Information)