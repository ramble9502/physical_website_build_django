# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from ActivityNews.models import *
from django.http import HttpResponse


def index(request):
    marqueecontrol = Marqueecontrol.objects.all()
    latestnews = Latest_News.objects.order_by('-create_date')[0:10]
    workshopnews = WorkShop_News.objects.order_by('-create_date')[0:10]
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'marqueecontrol': marqueecontrol, 'latestnews': latestnews,
                     'workshopnews': workshopnews, 'finspeact': finspeact}
    return render_to_response('index.html', extra_context)


def finspeact(request, id):
    if id:
        finspeact2 = Finished_Special_Activity.objects.filter(id=id)
        finspeact = Finished_Special_Activity.objects.order_by(
            '-create_date')[0:3]
        extra_context = {'finspeact': finspeact, 'finspeact2': finspeact2}
        return render_to_response('finspeactindex.html', extra_context)
    else:
        return redirect('/index')


def latestnews(request):
    marqueecontrol = Marqueecontrol.objects.all()
    latestnews = Latest_News.objects.order_by('-create_date')
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'marqueecontrol': marqueecontrol,
                     'latestnews': latestnews, 'finspeact': finspeact}
    return render_to_response('latestnewsindex.html', extra_context)


def workshopnews(request):
    marqueecontrol = Marqueecontrol.objects.all()
    workshopnews = WorkShop_News.objects.order_by('-create_date')
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'marqueecontrol': marqueecontrol,
                     'workshopnews': workshopnews, 'finspeact': finspeact}
    return render_to_response('workshopnewsindex.html', extra_context)
