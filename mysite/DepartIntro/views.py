from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from DepartIntro.models import *
from ActivityNews.models import Finished_Special_Activity, Linkact, Linkindex


def departintro(request):
    departments = Department_Characteristic.objects.all()
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    extra_context = {'departments': departments, 'finspeact': finspeact,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('departcharacterindex.html', extra_context)


def teachgoal(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    extra_context = {'finspeact': finspeact,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('teachgoal.html', extra_context)


def legislation(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    legislation = Legislation.objects.all()
    extra_context = {'finspeact': finspeact, 'legislation': legislation,'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('legislationindex.html', extra_context)


def equipment(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    equipment = Equipment.objects.all()
    extra_context = {'finspeact': finspeact, 'equipment': equipment,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('equipmentindex.html', extra_context)


def offregulation(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    offregulation = Their_official_regulations.objects.all()
    extra_context = {'finspeact': finspeact, 'offregulation': offregulation,
                     'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('offregulationindex.html', extra_context)


