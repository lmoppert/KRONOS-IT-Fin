from django.shortcuts import render
from django.views import generic
from contracts import models


# @login_required
def index(request):
    invoices = models.Invoice.objects.all()[:10]
    contracts = models.Contract.objects.filter(active=True)[:10]
    return render(request, 'contracts/index.html', context={
        'invoices': invoices, 'contracts': contracts})


class ContractView(generic.detail.DetailView):
    model = models.Contract


class InvoiceView(generic.detail.DetailView):
    model = models.Invoice


class NewInvoiceView(generic.edit.CreateView):
    model = models.Invoice
    fields = ['name', 'date', 'value', 'number', 'invoice', 'contract',
              'comment', 'expenditure', 'subject', 'vendor']


class ContractList(generic.list.ListView):
    model = models.Contract


class InvoiceList(generic.list.ListView):
    model = models.Invoice
