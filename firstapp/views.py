from django.shortcuts import render

# Create your views here.

def firstapp(request):
    return render(request,"firstapp/index.html")

def about_us(request):
    return render(request,"firstapp/about.html")


def courses(request):
    return render(request,"firstapp/courses.html")


def test_series(request):
    return render(request,"firstapp/test_series.html")

def fees(request):
    return render(request,"firstapp/fees.html")