#!-*-coding=utf8-*-
from django.contrib import admin
from Master.models import *
from django.forms import Textarea
# Register your models here.


class Course_Architecture_Upload(admin.TabularInline):
    model = Course_Architecture_Upload


class Course_Architecture_Class(admin.ModelAdmin):
    inlines = [Course_Architecture_Upload]


class Bachelor_Test_Upload(admin.TabularInline):
    model = Bachelor_Test_Upload


class Bachelor_Test_Class(admin.ModelAdmin):
    inlines = [Bachelor_Test_Upload]


class Study_Group_Upload(admin.TabularInline):
    model = Study_Group_Upload


class Study_Group_Class(admin.ModelAdmin):
    inlines = [Study_Group_Upload]


class Schoolpaper_Upload(admin.TabularInline):
    model = Schoolpaper_Upload
    formfield_overrides = {models.TextField: {
        'widget': Textarea(attrs={'rows': 4, 'cols': 40})}, }


class Schoolpaper_Class(admin.ModelAdmin):
    inlines = [Schoolpaper_Upload]


class Graduatedpaper_Upload(admin.TabularInline):
    model = Graduatedpaper_Upload


class Graduatedpaper_Class(admin.ModelAdmin):
    inlines = [Graduatedpaper_Upload]


admin.site.register(Schoolpaper, Schoolpaper_Class)
admin.site.register(Study_Group, Study_Group_Class)
admin.site.register(Bachelor_Test, Bachelor_Test_Class)
admin.site.register(Course_Architecture, Course_Architecture_Class)
admin.site.register(Seminar_Information)
admin.site.register(Graduatedpaper, Graduatedpaper_Class)
admin.site.register(Archeology)
