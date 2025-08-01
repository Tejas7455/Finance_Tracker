from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from Expensedjango.forms import RegisterForm 
from django.contrib.auth import login

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'Expensedjango/register.html',{'form':form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('')
    