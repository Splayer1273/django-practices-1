from django.shortcuts import render
from .models import Chai
from django.http import HttpResponse

# Create your views here.
def index(request):
    chais = Chai.objects.all()

    return render(request, 'index.html', {'chais': chais})

def home(request):
    return HttpResponse("my name is siddesh")

def base(request): 
    return render(request, 'base.html')