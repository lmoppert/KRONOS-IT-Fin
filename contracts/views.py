from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from contracts import models


# @login_required
def index(request):
    invoices = models.Invoice.objects.all()[:10]
    contracts = models.Contract.objects.filter(active=True)[:10]
    return render(request, 'contracts/index.html', context={
        'invoices': invoices, 'contracts': contracts})


class ContractView(DetailView):
    model = models.Contract


class InvoiceView(DetailView):
    model = models.Invoice


class ContractList(ListView):
    model = models.Contract


class InvoiceList(ListView):
    model = models.Invoice
