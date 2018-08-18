from django.shortcuts import render
from django.http import HttpResponse
from django_app.models import OurUsers
from . import forms
from django_app.forms import UserModelForm
# Create your views here.


def index(request):
    cdict = {'content': 'Index Stuff'}
    return render(request, 'django_app/index.html', context=cdict)


def users(request):
    users = OurUsers.objects.order_by('last_name')
    udict = {'users': users}
    return render(request, 'django_app/users.html', context=udict)

def form_view(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            res = OurUsers.objects.get_or_create(first_name=first_name, last_name=last_name,email=email)
            print(res)
    return render(request, 'django_app/form.html', {'form':form})

def modelform_view(request):
    form = UserModelForm()
    if request.method == "POST":
        form = UserModelForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'django_app/modelform.html',{'form':form})
