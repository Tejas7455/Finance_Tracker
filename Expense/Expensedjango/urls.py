from django.urls import path
from Expensedjango.views import RegisterView, DashboardView, TransactionCreateView, TransactionListView, TargetCreateView, export_transactions

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('transaction/add/',TransactionCreateView.as_view(), name='transaction_add'),
    path('transactions/', TransactionListView.as_view(), name="transactions"),
    path('target/', TargetCreateView.as_view(), name='target'),
    path('generate-report/', export_transactions, name='export_transactions'),
] 