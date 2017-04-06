from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
from Teacher.models import *
from ActivityNews.models import Finished_Special_Activity


def fulltime_teacher(request):
    fulltime_teacher = Fulltime_Teacher.objects.all()
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'fulltime_teacher': fulltime_teacher,
                     'finspeact': finspeact}
    return render_to_response('fullteacherindex.html', extra_context)


def fulldetail(request, id):
    if id:
        fulldetail = Fulltime_Teacher.objects.filter(id=id)
        finspeact = Finished_Special_Activity.objects.order_by(
            '-create_date')[0:3]
        extra_context = {'fulldetail': fulldetail, 'finspeact': finspeact}
        return render_to_response('fulldetailindex.html', extra_context)
    else:
        return redirect('/fullteacher')


def parttime_teacher(request):
    parttime_teacher = Parttime_Teacher.objects.all()
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    extra_context = {'parttime_teacher': parttime_teacher,
                     'finspeact': finspeact}
    return render_to_response('partteacherindex.html', extra_context)


def partdetail(request, id):
    if id:
        partdetail = Parttime_Teacher.objects.filter(id=id)
        finspeact = Finished_Special_Activity.objects.order_by(
            '-create_date')[0:3]
        extra_context = {'partdetail': partdetail, 'finspeact': finspeact}
        return render_to_response('partdetailindex.html', extra_context)
    else:
        return redirect('/partteacher')
