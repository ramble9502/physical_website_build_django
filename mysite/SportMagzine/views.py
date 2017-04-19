from django.shortcuts import render
from ActivityNews.models import Finished_Special_Activity, Linkact, Linkindex
from SportMagzine.models import *
from django.shortcuts import render_to_response
# Create your views here.


def sportmagzine(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    magzine = Magzine.objects.order_by('-id')
    regulation = Regulation.objects.all()
    linkact = Linkact.objects.order_by('-create_date')[0:3]
    linkindex = Linkindex.objects.order_by('-create_date')[0:10]
    extra_context = {'finspeact': finspeact, 'magzine': magzine,
                     'regulation': regulation, 'linkact': linkact, 'linkindex': linkindex}
    return render_to_response('sportmagzineindex.html', extra_context)
