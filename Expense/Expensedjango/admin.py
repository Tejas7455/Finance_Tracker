from django.contrib import admin
from .models import Transaction,Target
from import_export import resources
from import_export.admin import ExportMixin

# Register your models here.
class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        fields = ['date','title','amount', 'transaction_type']

@admin.register(Transaction)
class TransactionAdmin(ExportMixin ,admin.ModelAdmin):
    resource_class = TransactionResource
    list_display = ['title','amount','transaction_type','date','category']
    rearch_fields = ('title',)

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ['name','target_amount','deadline']