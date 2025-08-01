from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Income','Income'),
        ('Expense','Expense'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'