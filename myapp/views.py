from django.shortcuts import render
from .models import *

# Create your views here.


def read(request):
    return render(request, 'read.html')



def create(request):
    return render(request, 'create.html')


def update(request):
    return render(request, 'update.html')