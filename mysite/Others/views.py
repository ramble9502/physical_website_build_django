from django.shortcuts import render
from ActivityNews.models import Finished_Special_Activity
from Others.models import *
from django.shortcuts import render_to_response
# Create your views here.


def honor(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    honor = Honorannounce.objects.order_by('-id')
    extra_context = {'finspeact': finspeact, 'honor': honor}
    return render_to_response('honorindex.html', extra_context)


def alumni(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    alumni = AlumniAccociation.objects.all()
    extra_context = {'finspeact': finspeact, 'alumni': alumni}
    return render_to_response('alumniindex.html', extra_context)


def stuaccociation(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    stuaccociation = StuAccociation.objects.order_by('-filename')
    extra_context = {'finspeact': finspeact, 'stuaccociation': stuaccociation}
    return render_to_response('stuaccociationindex.html', extra_context)


def coursemap(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'finspeact': finspeact}
    return render_to_response('coursemap.html', extra_context)
