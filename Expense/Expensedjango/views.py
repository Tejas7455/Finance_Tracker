from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from Expensedjango.forms import RegisterForm, TransactionForm, TargetForm 
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, Target
from django.db.models import Sum 
from .admin import TransactionResource
from django.contrib import messages
from django.shortcuts import get_object_or_404

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'Expensedjango/register.html',{'form':form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
        
        return render(request, 'Expensedjango/register.html',{'form':form})
        
class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_transactions = Transaction.objects.filter(user=request.user)
        targets = Target.objects.filter(user=request.user).order_by('deadline')  # ✅ Sort by deadline

        total_income = user_transactions.filter(transaction_type='Income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = user_transactions.filter(transaction_type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0

        net_saving = total_income - total_expense
        remaining_savings = net_saving

        goal_progress = []

        for target in targets:
            if target.target_amount > 0:
                if remaining_savings >= target.target_amount:
                    progress = 100
                    remaining_savings -= target.target_amount
                elif remaining_savings > 0:
                    progress = round((remaining_savings / target.target_amount) * 100, 2)
                    remaining_savings = 0
                else:
                    progress = 0
            else:
                progress = 0

            goal_progress.append({'target': target, 'progress': progress})

        context = {
            'transactions': user_transactions,
            'total_income': total_income,
            'total_expense': total_expense,
            'net_saving': net_saving,
            'goal_progress': goal_progress,
        }

        return render(request, 'Expensedjango/dashboard.html', context)

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
            return redirect('dashboard')
        return render(request, 'Expensedjango/transaction.html',{'form':form})

class TransactionListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(user = request.user)
        return render(request, 'Expensedjango/transaction_list.html', {'transactions':transactions})
    
class TargetCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TargetForm()
        return render(request, 'Expensedjango/targetform.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = TargetForm(request.POST)
        if form.is_valid():
            target = form.save(commit=False)
            target.user = request.user
            target.save()
            messages.success(request, 'Transaction Added Successfully!')
            return redirect('dashboard')
        return render(request, 'Expensedjango/targetform.html', {'form':form})

class TargetUpdateView(LoginRequiredMixin, View):
    def get (self, request, pk, *args, **kwargs):
        target = get_object_or_404(Target, pk=pk, user= request.user)
        form = TargetForm(instance=target)
        return render(request, 'Expensedjango/targetform.html', {'form':form})

    def post(self, request, pk, *args, **kwargs):
        target = get_object_or_404(Target, pk=pk, user=request.user)
        form = TargetForm(request.POST, instance=target)
        if form.is_valid():
            form.save()
            messages.success(request, 'Target updated successfully')
            return redirect('dashboard')
        return render(request, 'Expensedjango/targetform.html', {'form':form})

class TargetDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        target = get_object_or_404(Target, pk=pk, user=request.user)
        target.delete()
        messages.success(request, 'Target deleted successfully')
        return redirect('dashboard')    

def export_transactions(request):
    user_transactions = Transaction.objects.filter(user = request.user)
    transaction_resource = TransactionResource()
    dataset = transaction_resource.export(queryset=user_transactions)
    excel_data = dataset.export('xlsx')

    response = HttpResponse(excel_data, content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    #set the header for downloading the file 
    response['Content-Disposition'] = 'attachment; filename=transaction_report.xlsx'
    return response