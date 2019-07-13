from django.shortcuts import render
from esacco.models import Share, Loan, Payment
from datetime import datetime


def landingpage_view(request):
    return render(request, 'landingPage.html')


def dashboard_view(request):
    date = format(datetime.now().strftime('%B  %d %Y'))
    total_shares = Share.get_share_total(request.user)
    metrics = Share.objects.filter(user_id=request.user).values('amount', 'date_collected').order_by('date_collected')
    payment = Payment.objects.filter(user=request.user).values('amount', 'payment_date').order_by('payment_date')
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
    return render(request, 'dashboard.html', {'total_shares': int(total_shares),
                                              'date': date, 'data': data, 'payments': payments})


def reports_view(request):
    return render(request, 'reports.html')


def request_view(request):
    message = ''
    if request.method == 'POST':
        loan_request = Loan(user_id=request.user.id, reason=request.POST['loan_reason'],
                            amount_Requested=request.POST['loan_amount'])
        if not loan_request:
            print('something went wrong')
            message = 'something went wrong'
            return render(request, 'request.html', dict(message=message))
        loan_request.save()
        message = 'request has been submitted'
        return render(request, 'request.html', dict(message=message))
    return render(request, 'request.html', dict(message=message))
