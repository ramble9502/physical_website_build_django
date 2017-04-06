from django.shortcuts import render
from ActivityNews.models import Finished_Special_Activity
from Masternight.models import *
from django.shortcuts import render_to_response
# Create your views here.

def ncoursearchi(request):
    finspeact = Finished_Special_Activity.objects.order_by('-create_date')[0:3]
    ncoursearchi = NCourse_Architecture.objects.all()
    extra_context = {'finspeact': finspeact, 'ncoursearchi': ncoursearchi}
    return render_to_response('ncoursearchindex.html', extra_context)
