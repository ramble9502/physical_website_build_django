# -*- coding: UTF-8 -*-
from django.contrib import admin
from Teacher.models import *
# Register your models here.


class Periodical1_Class(admin.TabularInline):
    model = Periodical1


class Seminar1_Class(admin.TabularInline):
    model = Seminar1


class Book1_Class(admin.TabularInline):
    model = Book1


class Periodical2_Class(admin.TabularInline):
    model = Periodical2


class Seminar2_Class(admin.TabularInline):
    model = Seminar2


class Book2_Class(admin.TabularInline):
    model = Book2


class Fulltime_Teacher_Class(admin.ModelAdmin):
    inlines = [Periodical1_Class, Seminar1_Class, Book1_Class]


class Parttime_Teacher_Class(admin.ModelAdmin):
    inlines = [Periodical2_Class, Seminar2_Class, Book2_Class]


admin.site.register(Yearsigned)


admin.site.register(Fulltime_Teacher, Fulltime_Teacher_Class)
admin.site.register(Parttime_Teacher, Parttime_Teacher_Class)
