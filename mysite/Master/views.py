from django.shortcuts import render
from ActivityNews.models import Finished_Special_Activity
from Master.models import *
from django.shortcuts import render_to_response
# Create your views here.


def coursearchi(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    coursearchi = Course_Architecture.objects.all()
    extra_context = {'finspeact': finspeact, 'coursearchi': coursearchi}
    return render_to_response('coursearchindex.html', extra_context)


def bachelortest(request):
    bachelortest = Bachelor_Test.objects.all()
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'finspeact': finspeact, 'bachelortest': bachelortest}
    return render_to_response('bachelortestindex.html', extra_context)


def seminar(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    seminar = Seminar_Information.objects.all()
    extra_context = {'finspeact': finspeact, 'seminar': seminar}
    return render_to_response('seminarindex.html', extra_context)


def schoolpaper(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    schoolpaper = Schoolpaper.objects.order_by('-year')[:1]
    extra_context = {'finspeact': finspeact, 'schoolpaper': schoolpaper}
    return render_to_response('schoolpaperindex.html', extra_context)


def graduatedpaper(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    graduatedpaper = Graduatedpaper.objects.order_by('-year')[:1]
    extra_context = {'graduatedpaper': graduatedpaper, 'finspeact': finspeact}
    return render_to_response('graduatedindex.html', extra_context)


def studygroup(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    studygroup = Study_Group.objects.order_by('-year')
    extra_context = {'finspeact': finspeact, 'studygroup': studygroup}
    return render_to_response('studygroupindex.html', extra_context)
