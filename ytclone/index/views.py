from django.shortcuts import render

# Create your views here.

def index_home(request):
    return render(request,'index/home.html')

def index_trend(request):
    return render(request,'index/trending.html')

def index_sub(request):
    return render(request,'index/subscription.html')

