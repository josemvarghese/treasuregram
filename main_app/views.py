from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import Treasure
from datetime import datetime
from .forms import TreasureForm
# Create your views here.

def index(request):
    # name  = 'Gold Nugget'
    # value = 1000
    context=Treasure.objects.all()
    form=TreasureForm()
    # context['treasures'] = {'name':"jose",'value':500, 'material':'gold','location':'india In','img_url':'jose.jpg'}
    return render(request,'index.html',{'treasures':context,'form':form})


def detail(request,detail_id):
    context = Treasure.objects.get(pk=detail_id)
    return render(request, 'detail.html', {'treasure': context})


def post_treasure(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = Treasure(name=form.cleaned_data['name'],value=form.cleaned_data['value'],material=form.cleaned_data['material'],location=form.cleaned_data['location'],img_url=form.cleaned_data['img_url'])
        treasure.save()
    return HttpResponseRedirect("/")