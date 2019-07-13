from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from mainApp.models import Share, Loan, Payment, models
from datetime import datetime


def landingpage_view(request):
    if str(request.user) is not 'AnonymousUser':
        if request.user.is_staff is not True:
            return redirect('user_dashboard')
        else:
            return redirect('admin_dashboard')
    return render(request, 'landingPage.html')


def dashboard_view(request):
    if str(request.user) is not 'AnonymousUser':
        if request.user.is_staff is True:
            return redirect('admin_dashboard')
        date = format(datetime.now().strftime('%B  %d %Y'))
        total_shares = Share.get_share_total(request.user)
        metrics = Share.objects.filter(user_id=request.user) \
            .values('amount', 'date_collected').order_by('date_collected')
        payment = Payment.objects.filter(user=request.user) \
            .values('amount', 'payment_date').order_by('payment_date')
        data = {}
        payments = {}
        for share in metrics:
            month = datetime.strftime(share['date_collected'], '%B')
            if month in data:
                data[month].append(int(share['amount']))
            else:
                data[month] = [int(share['amount'])]

        for item in payment:
            month = datetime.strftime(item['payment_date'], '%B')
            if month in payments:
                payments[month].append(int(item['amount']))
            else:
                payments[month] = [int(item['amount'])]

        if total_shares is None:
            total_shares = 0
        return render(request, 'dashboard.html', {'total_shares': int(total_shares),
                                                  'date': date, 'data': data, 'payments': payments})
    else:
        return redirect('login')


def request_view(request):
    message = ''
    pay_data = Payment.objects.filter(user_id=request.user)
    for details in pay_data:
        if details.balance is not None:
            error = ('You have a balance of %s' % int(details.balance))
            return render(request, 'request.html', dict(error=error, type='payment'))
    if request.method == 'POST':
        try:
            loan_request = Loan(user_id=request.user.id, reason=request.POST['loan_reason'],
                                amount_Requested=request.POST['loan_amount'])
            if not loan_request:
                message = 'something went wrong'
                return render(request, 'request.html', dict(message=message))
            loan_request.save()
            message = 'request has been submitted'
            return render(request, 'request.html', dict(message=message))
        except IntegrityError:
            error = 'can not make request for a loan before paying the previous loan'
            return render(request, 'request.html', dict(error=error))
    return render(request, 'request.html', dict(message=message))


def admin_dashboard_view(request):
    if str(request.user) is not 'AnonymousUser' and request.user.is_staff is True:
        date = format(datetime.now().strftime('%B  %d %Y'))
        total_shares = Share.objects.aggregate(models.Sum('amount')).get('amount__sum')
        metrics = Share.objects.values('amount', 'date_collected') \
            .order_by('date_collected')
        payment = Payment.objects.values('amount', 'payment_date').order_by('payment_date')
        loan = Loan.objects.values('amount_Requested', 'request_date').order_by('request_date')
        data = {}
        payments = {}
        requests = {}
        for share in metrics:
            month = datetime.strftime(share['date_collected'], '%B')
            if month in data:
                data[month].append(int(share['amount']))
            else:
                data[month] = [int(share['amount'])]

        for item in payment:
            month = datetime.strftime(item['payment_date'], '%B')
            if month in payments:
                payments[month].append(int(item['amount']))
            else:
                payments[month] = [int(item['amount'])]

        for item in loan:
            month = datetime.strftime(item['request_date'], '%B')
            if month in requests:
                requests[month].append(int(item['amount_Requested']))
            else:
                requests[month] = [int(item['amount_Requested'])]

        if total_shares is None:
            total_shares = 0
        return render(request, 'admin_dashboard.html', {'total_shares': int(total_shares),
                                                        'date': date, 'data': data, 'payments': payments,
                                                        'requests': requests})
    else:
        return redirect('login')


def admin_reports_view(request):
    if str(request.user) is not 'AnonymousUser' and request.user.is_staff is True:
        loans = Loan.objects.values('user_id', 'user__first_name',
                                    'user__last_name', 'amount_Requested', 'dueDate').order_by('user_id')
        loan_data = []
        for item in loans:
            if item['dueDate'] is not None:
                temp = dict(user_id=item['user_id'], first_name=item['user__first_name'], last_name=['user__last_name'],
                            amount_requested=item['amount_Requested'],
                            dueDate=datetime.strftime(item['dueDate'], '%B'))
            else:
                temp = dict(user_id=item['user_id'], first_name=item['user__first_name'],
                            last_name=item['user__last_name'], amount_requested=item['amount_Requested'],
                            dueDate=item['dueDate'])

            pay_data = Payment.objects.filter(user_id=item['user_id'])
            for details in pay_data:
                if details.balance is not None:
                    balance = int(details.balance)
                    percentage = (balance / int(item['amount_Requested'])) * 100
                    temp['percentage'] = percentage
                else:
                    temp['percentage'] = 0
            loan_data.append(temp)
        return render(request, 'reports.html', dict(loans=loan_data))
    else:
        return redirect('login')
