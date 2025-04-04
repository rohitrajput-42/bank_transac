from django.shortcuts import render, redirect
from .models import Bank
from django.core import serializers
import json


def home(request):
    context = {}
    # records = json.loads(serializers.serialize("json", Bank.objects.all()))s
    records = Bank.objects.all().order_by("-created_ts")
    context["records"] = records

    return render(request, "index.html", context)

def add_transaction(request):
    if request.method == "POST":

        latest_record = json.loads(serializers.serialize("json", Bank.objects.all().order_by('-created_ts')))
        if latest_record:
            latest_record = latest_record[0]

            transaction_type = request.POST.get("transaction_type")
            amount = request.POST.get("amount")
            description = request.POST.get("description")

            if transaction_type == "credit":
                credit = request.POST.get("amount")
                running_balance = int(latest_record["fields"]["running_balance"]) + int(amount)
                Bank.objects.create(
                    description = description,
                    transaction_type = transaction_type,
                    credit = credit,
                    running_balance = running_balance
                )

            elif transaction_type == "debit":
                debit = request.POST.get("amount")
                running_balance = int(latest_record["fields"]["running_balance"]) - int(amount)
                Bank.objects.create(
                    description = description,
                    transaction_type = transaction_type,
                    debit = debit,
                    running_balance = running_balance
                )
        else:
            transaction_type = request.POST.get("transaction_type")
            amount = request.POST.get("amount")
            description = request.POST.get("description")
            credit = request.POST.get("amount")
            Bank.objects.create(
                description = description,
                transaction_type = transaction_type,
                credit = credit,
                running_balance = credit
            )

        return redirect("/")
        
    else:
        context = {}
        latest_record = json.loads(serializers.serialize("json", Bank.objects.filter(transaction_type = "credit")))
        
        if len(latest_record) == 0:
            context["display_val"] = "only_credit"


        return render(request, "add_transaction.html", context)

    return render(request, "add_transaction.html")