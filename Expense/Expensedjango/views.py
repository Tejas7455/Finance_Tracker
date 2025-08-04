from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from Expensedjango.forms import RegisterForm, TransactionForm 
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction

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

class TransactionCreateView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form = TransactionForm()
        return render(request, 'Expensedjango/transaction.html', {'form':form}) 
    
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            redirect('dashboard')
        return render(request, 'Expensedjango/transaction.html',{'form':form})

class TransactionListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.all()
        return render(request, 'Expensedjango/transaction_list.html',{'transactions':transactions})