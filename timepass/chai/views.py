from django.shortcuts import render
from .models import Chai
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    chais = Chai.objects.all()

    return render(request, 'index.html', {'chais': chais})


def view_chai(request, id):
    chai = get_object_or_404(Chai, id=id)
    return render(request, 'view_chai.html', {'chai': chai})


def home(request):
    return HttpResponse("my name is siddesh")

def base(request): 
    return render(request, 'base.html')