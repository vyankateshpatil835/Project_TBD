from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello')
    # return render(request, 'index.html')
def rnd(request):
    # return HttpResponse('hello')
    return render(request, 'index.html')