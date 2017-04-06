from django.shortcuts import render
from ActivityNews.models import Finished_Special_Activity
from University.models import *
from django.shortcuts import render_to_response
# Create your views here.


def courseplan(request):
    courseplan = CoursePlan.objects.order_by('-created_time')
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'finspeact': finspeact, 'courseplan': courseplan}
    return render_to_response('courseplanindex.html', extra_context)


def curriculum(request):
    curriculum = Curriculum2.objects.order_by('-created_time')
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'finspeact': finspeact, 'curriculum': curriculum}
    return render_to_response('curriculumindex.html', extra_context)


def studentcorner(request):
    studentcorner = StudentCorner.objects.all()
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'finspeact': finspeact, 'studentcorner': studentcorner}
    return render_to_response('studentcornerindex.html', extra_context)