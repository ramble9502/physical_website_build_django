# -*- coding: UTF-8 -*-
from django.contrib import admin

# Register your models here.
from DepartIntro.models import *

class Dep_promotion_Point(admin.TabularInline):
    model = Dep_promotion_Point


class Other_Point(admin.TabularInline):
    model = Other_Point


class Scholarship(admin.TabularInline):
    model = Scholarship


class Legislation_Class(admin.ModelAdmin):
    inlines = [Dep_promotion_Point, Scholarship, Other_Point]


admin.site.register(Department_Characteristic)
admin.site.register(Legislation, Legislation_Class)
admin.site.register(Equipment)
admin.site.register(Their_official_regulations)

