from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    # name  = 'Gold Nugget'
    # value = 1000
    context= dict()
    context['treasures'] = {'name':"jose",'value':500, 'material':'gold','location':'india In','img_url':'jose.jpg'}
    return render(request,'index.html',context)
