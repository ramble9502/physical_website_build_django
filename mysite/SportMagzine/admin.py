# -*- coding: UTF-8 -*-
from django.contrib import admin
from SportMagzine.models import *
# Register your models here.


class Regulation_Upload(admin.TabularInline):
    model = Regulation_Upload


class Regulation_Class(admin.ModelAdmin):
    inlines = [Regulation_Upload]


admin.site.register(Regulation, Regulation_Class)
admin.site.register(Magzine)
