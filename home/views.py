from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import *
import json
import requests
from mongoengine import *


def index(request):
    return render(request, 'home/index.html', {})
