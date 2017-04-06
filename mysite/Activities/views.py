from django.shortcuts import render
from django.shortcuts import render_to_response

from Activities.models import *
from django.http import HttpResponse
from ActivityNews.models import Finished_Special_Activity

# Create your views here.


def activities1(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    activities = AcademicObjects.objects.all()
    extra_context = {'activities': activities, 'finspeact': finspeact}
    return render_to_response('activities1index.html', extra_context)


def activities2(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    activities = AcademicObjects.objects.all()
    extra_context = {'activities': activities, 'finspeact': finspeact}
    return render_to_response('activities2index.html', extra_context)


def activities3(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    activities = AcademicObjects.objects.all()
    extra_context = {'activities': activities, 'finspeact': finspeact}
    return render_to_response('activities3index.html', extra_context)


def actdetail(request, id):
    if id:
        activities = AcademicActivities.objects.filter(id=id)
        finspeact = Finished_Special_Activity.objects.order_by(
            '-create_date')[0:3]
        extra_context = {'activities': activities, 'finspeact': finspeact}
        return render_to_response('actdetailindex.html', extra_context)
    else:
        return redirect('/activities1')
