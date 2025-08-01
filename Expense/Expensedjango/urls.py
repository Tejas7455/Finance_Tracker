from django.urls import path
from Expensedjango.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
] 