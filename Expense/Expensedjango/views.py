from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from Expensedjango.forms import RegisterForm 
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'Expensedjango/register.html',{'form':form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'Expensedjango/register.html',{'form':form})
        
class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Expensedjango/dashboard.html')
    