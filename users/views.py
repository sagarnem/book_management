from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from users.models import UserBalance
from users.forms import UserBalanceForm
from transaction.service import TransactionService
from transaction.models import Transaction
from django.db import transaction
# Create your views here.
@login_required
@transaction.atomic
def admin_add_balance(request):
    form = UserBalanceForm()
    if request.method == "POST":
        form = UserBalanceForm(request.POST)
        if form.is_valid():
            form.save()
            TransactionService.create_transaction(
                "Top up",
                request.POST['user'],
                request.POST['balance'],
                Transaction.Transactionstatus.COMPLETED,
                Transaction.PaymentMethod.ADMIN,
            )
            return redirect('/users/userbalance')
    context = {
        'form':form
    }
    return render(request, 'users/balance-create.html',context)


def list_user_balance(request):
    user_balance = UserBalance.objects.all()
    context = {
        'user_balance':user_balance
    }
    return render(request, 'users/balance-list.html',context)
