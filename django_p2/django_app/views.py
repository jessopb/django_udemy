from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # dict = {'content':'WELCOME'}
    return HttpResponse('Hello')

def users(request):
    return HttpResponse('Users')
