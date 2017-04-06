from django.shortcuts import render
from ActivityNews.models import Finished_Special_Activity
from RecruStu.models import *
from django.shortcuts import render_to_response
# Create your views here.


def sportexcellent(request):
    sportexcellent = Sport_Excellent_Admission.objects.order_by(
        '-created_time')
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'finspeact': finspeact, 'sportexcellent': sportexcellent}
    return render_to_response('sportexcellentindex.html', extra_context)


def senioradmi(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    senioradmi = Senior_Admission.objects.all()
    extra_context = {'finspeact': finspeact, 'senioradmi': senioradmi}
    return render_to_response('senioradmissionindex.html', extra_context)


def unitestdistribute(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    unitestdistribute = Senior_Distribution.objects.all()
    extra_context = {'finspeact': finspeact,
                     'unitestdistribute': unitestdistribute}
    return render_to_response('unitestdistrindex.html', extra_context)


def transform(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    transform = Transfer_Test.objects.order_by('-id')[:1]
    extra_context = {'finspeact': finspeact, 'transform': transform}
    return render_to_response('transformtestindex.html', extra_context)


def masteradmission(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    masteradmission = Master_Admission.objects.order_by('-created_time')
    extra_context = {'finspeact': finspeact,
                     'masteradmission': masteradmission}
    return render_to_response('remasterindex.html', extra_context)


def manightadmission(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    manightadmission = Master_night2.objects.order_by('-created_time')
    extra_context = {'finspeact': finspeact,
                     'manightadmission': manightadmission}
    return render_to_response('remasternightindex.html', extra_context)


def liston(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    liston = List.objects.order_by('-title')
    extra_context = {'finspeact': finspeact, 'liston': liston}
    return render_to_response('listindex.html', extra_context)


def trafficmethod(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    traffic = Traffic_Information.objects.order_by('-id')
    extra_context = {'finspeact': finspeact, 'traffic': traffic}
    return render_to_response('trafficindex.html', extra_context)