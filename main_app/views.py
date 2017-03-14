from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    name  = 'Gold Nugget'
    value = 1000
    context = {'treasure_name':name,'treasure_val':value}
    return render(request,'index.html',context)
