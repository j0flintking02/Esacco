from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from users.models import User, Profile
from mainApp.models import Loan, Dividend
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['user_password'] != request.POST['user_password1']:
            return render(request, 'signup.html', {'password_error': 'you\'re passwords don\'t match'})
        try:
            User.objects.get(email=request.POST['user_email'])
            return render(request, 'signup.html', {'account_error': 'ERROR: user already exists try again'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['user_email'], request.POST['first_name'],
                                            request.POST['last_name'], request.POST['user_password'])
            auth.login(request, user)
            return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['user_email'], password=request.POST['user_password'])
        if user is not None:
            if str(user.status) == 'PED':
                print(user.status)
                return render(request, 'login.html',
                              {'account_error': 'account is still waiting for approval'})
            else:
                auth.login(request, user)
                if str(request.user.is_staff) is not True:
                    return redirect('user_dashboard')
                else:
                    return redirect('admin_dashboard')
        else:
            return render(request, 'login.html', {'account_error': 'something went wrong with your password or email'})
    return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')


def profile(request):
    message = ''
    data = {}
    obj = get_object_or_404(Profile, user=request.user)
    user_profile = dict(firstName=obj.user.first_name, lastName=obj.user.last_name, email=obj.user.email,
                        age=obj.age, address=obj.address, phone=obj.phone, job=obj.occupation)
    loan_obj = Loan.objects.filter(user_id=request.user).values('amount_Requested', 'status', 'dueDate')
    pending_count = Loan.objects.filter(status='PED').count()
    over_due_count = Loan.objects.filter(dueDate__lt=datetime.now()).count()
    issuing_date = Dividend.objects.filter(user_id=request.user).values('issue_date')

    for loan in loan_obj:
        data.update(amount=int(loan['amount_Requested']), status=loan['status'],
                    over_due_count=over_due_count,
                    pending_count=pending_count, overDue_count=over_due_count)
    if issuing_date.count() is 0:
        data.update(issuing_date='0/00/0000')
    for temp in issuing_date:
        data.update(issuing_date=datetime.strftime(temp['issue_date'], '%d/%m/%Y'))

    if request.method == 'POST':
        data = request.POST
        new_data = dict(address=data['address'], phone=data['phone'], occupation=data['job'])
        Profile.objects.filter(user=request.user).update_or_create(new_data)
        return redirect('profile')
    return render(request, 'profile.html', dict(profile=user_profile, message=message, loan=data))
