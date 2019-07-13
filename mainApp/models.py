from django.db import models
from users.models import User


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_collected = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)

    @staticmethod
    def get_share_total(user_id):
        total = Share.objects.filter(user_id=user_id).aggregate(models.Sum('amount')).get('amount__sum')
        return total


class Loan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    APPROVED = 'APV'
    REJECTED = 'REJ'
    PENDING = 'PED'
    STATUS_CHOICES = [
        (APPROVED, 'approved'),
        (REJECTED, 'rejected'),
        (PENDING, 'pending'),
    ]
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    reason = models.CharField(max_length=255, null=False)
    amount_Requested = models.DecimalField(max_digits=10, decimal_places=2)
    request_date = models.DateField(auto_now=True, null=False)
    dueDate = models.DateField(auto_now=False, null=True)

    def __str__(self):
        return str(self.amount_Requested)


class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)

    def get_balance(self):
        """Returns the person's balance."""
        return self.loan.amount_Requested - self.amount

    balance = property(get_balance)


class Dividend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    APPROVED = 'APV'
    REJECTED = 'REJ'
    PENDING = 'PED'
    STATUS_CHOICES = [
        (APPROVED, 'approved'),
        (REJECTED, 'rejected'),
        (PENDING, 'pending'),
    ]
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    def __str__(self):
        return str(self.value)

    def get_accumulated_total(self):
        """Returns the Users accumulated total"""
        accumulated_total = self.value * Share.get_share_total(self.user_id)
        return round(accumulated_total, 2)

    dividend = property(get_accumulated_total)
