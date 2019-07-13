from django.contrib import admin
from .models import (
    Share,
    Loan,
    Dividend,
    Payment
)

admin.site.site_header = 'Esacco'


class ShareAdminView(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'date_collected')


class LoanAdminView(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount_Requested', 'dueDate', 'request_date')


class DividendAdminView(admin.ModelAdmin):
    list_display = ('id', 'user', 'issue_date', 'value', 'dividend', 'status')


class PaymentAdminView(admin.ModelAdmin):
    list_display = ('id', 'user', 'loan', 'amount', 'balance', 'payment_date')


admin.site.register(Share, ShareAdminView)
admin.site.register(Loan, LoanAdminView)
admin.site.register(Dividend, DividendAdminView)
admin.site.register(Payment, PaymentAdminView)
