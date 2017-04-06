from django.shortcuts import render
from ActivityNews.models import Finished_Special_Activity
from SportMagzine.models import *
from django.shortcuts import render_to_response
# Create your views here.


def sportmagzine(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    magzine = Magzine.objects.order_by('-id')
    regulation = Regulation.objects.all()
    extra_context = {'finspeact': finspeact,
                     'magzine': magzine, 'regulation': regulation}
    return render_to_response('sportmagzineindex.html', extra_context)
