from django.shortcuts import render
from ActivityNews.models import Finished_Special_Activity, Linkact, Linkindex
from University.models import *
from django.shortcuts import render_to_response
# Create your views here.


def courseplan(request):
    courseplan = CoursePlan.objects.order_by('-created_time')[0:10]
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    extra_context = {'finspeact': finspeact, 'courseplan': courseplan,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('courseplanindex.html', extra_context)


def curriculum(request):
    curriculum = Curriculum2.objects.order_by('-created_time')[0:10]
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    extra_context = {'finspeact': finspeact, 'curriculum': curriculum,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('curriculumindex.html', extra_context)


def studentcorner(request):
    studentcorner = StudentCorner.objects.all()
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    extra_context = {'finspeact': finspeact, 'studentcorner': studentcorner,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('studentcornerindex.html', extra_context)


def crossdomain(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    crossdomain = Crossdomain.objects.order_by('-create_year')
    extra_context = {'finspeact': finspeact, 'crossdomain': crossdomain,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('crossdomainindex.html', extra_context)
