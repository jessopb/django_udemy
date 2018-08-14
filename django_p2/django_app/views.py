from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    cdict = {'content': 'Index Stuff'}
    return render(request, 'django_app/index.html', context=cdict)


def users(request):
    users = ['Tom', 'Bob', 'Sam']
    udict = {'users': users}
    return render(request, 'django_app/users.html', context=udict)
