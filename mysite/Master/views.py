from django.shortcuts import render
from ActivityNews.models import Finished_Special_Activity, Linkact, Linkindex
from Master.models import *
from django.shortcuts import render_to_response
# Create your views here.


def coursearchi(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    coursearchi = Course_Architecture.objects.all()[0:10]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    extra_context = {'finspeact': finspeact, 'coursearchi': coursearchi,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('coursearchindex.html', extra_context)


def bachelortest(request):
    bachelortest = Bachelor_Test.objects.all()
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    extra_context = {'finspeact': finspeact, 'bachelortest': bachelortest,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('bachelortestindex.html', extra_context)


def seminar(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    seminar = Seminar_Information.objects.all()
    extra_context = {'finspeact': finspeact, 'seminar': seminar,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('seminarindex.html', extra_context)


def schoolpaper(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    schoolpaper = Schoolpaper.objects.order_by('-year')[:1]
    extra_context = {'finspeact': finspeact, 'schoolpaper': schoolpaper,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('schoolpaperindex.html', extra_context)


def graduatedpaper(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    graduatedpaper = Graduatedpaper.objects.order_by('-year')[:1]
    extra_context = {'graduatedpaper': graduatedpaper,
                     'finspeact': finspeact, 'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('graduatedindex.html', extra_context)


def studygroup(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    studygroup = Study_Group.objects.order_by('-year')[0:10]
    extra_context = {'finspeact': finspeact, 'studygroup': studygroup,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('studygroupindex.html', extra_context)


def archeology(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    archeology = Archeology.objects.order_by('-create_year')
    extra_context = {'finspeact': finspeact, 'archeology': archeology,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('archeologyindex.html', extra_context)


def teachmaster(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    teachmaster = Teachemaster.objects.all()[0:3]
    extra_context = {'finspeact': finspeact, 'teachmaster': teachmaster,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('teachmasterindex.html', extra_context)
