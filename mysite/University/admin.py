# -*- coding: UTF-8 -*-
from django.contrib import admin
from University.models import *

# Register your models here.


class CoursePlan_Upload(admin.TabularInline):
    model = CoursePlan_Upload


class CoursePlan_Class(admin.ModelAdmin):
    inlines = [CoursePlan_Upload]

class Curriculum_Upload(admin.TabularInline):
	model=Curriculum_Upload

class Curriculum_Class(admin.ModelAdmin):
	inlines=[Curriculum_Upload]

class StudentCorner_Upload(admin.TabularInline):
	model=StudentCorner_Upload

class StudentCorner_Class(admin.ModelAdmin):
	inlines=[StudentCorner_Upload]
		
		
admin.site.register(StudentCorner,StudentCorner_Class)
admin.site.register(Curriculum2,Curriculum_Class)		
admin.site.register(CoursePlan, CoursePlan_Class)