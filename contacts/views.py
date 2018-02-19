# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from .models import ContactInfo

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def view_home(request):
	contact_info = ContactInfo.objects.all()
	return render(request,'contacts/base.html',{'contact_info':contact_info})

def redirecting(request):
	return redirect('view_home')