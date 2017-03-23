from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import Treasure
from datetime import datetime
from .forms import TreasureForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
    form = TreasureForm(request.POST,request.FILES)
    if form.is_valid():
        # treasure = Treasure(name=form.cleaned_data['name'],value=form.cleaned_data['value'],material=form.cleaned_data['material'],location=form.cleaned_data['location'],img_url=form.cleaned_data['img_url'])
        # treasure.save()
        treasure = form.save(commit=False)
        treasure.user = request.user
        treasure.save()
    return HttpResponseRedirect("/")


def delete_treasure(request,treasure_id):
    tresure = Treasure.objects.get(pk=treasure_id)
    tresure.delete()
    return HttpResponseRedirect("/")


def profile(request,username):
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(request,'profile.html',{'treasures':treasures,'username':username})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u,password=p)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect("/")
                else:
                    print ("The account has been disabled")
            else:
                print("The username or password were incorrect")

    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})


def logout_view(request):
    logout(request)
    return  HttpResponseRedirect("/")









