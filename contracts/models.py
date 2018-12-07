from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from djmoney.models.fields import MoneyField
from django.db import models
from django.urls import reverse
from contracts.constants import EXPENDITURES, SUBJECTS


class Vendor(models.Model):
    """Model for a vendor that sends invoices"""
    name = models.CharField(max_length=200, verbose_name=_("Vendor"))
    contact = models.TextField(blank=True, verbose_name=_("Contact"))

    class Meta:
        verbose_name = _("Vendor")
        verbose_name_plural = _("Vendors")

    def __str__(self):
        return "{}".format(self.name)


class Contract(models.Model):
    """Model for contracts that have to be continued on a rgualar basis"""

    name = models.CharField(max_length=200, verbose_name=_("Contract"))
    number = models.CharField(max_length=200, blank=True,
                              verbose_name=_("Order Number"))
    active = models.BooleanField(default=True, verbose_name=_("Active"))
    expenditure = models.CharField(max_length=1, choices=EXPENDITURES,
                                   blank=True, verbose_name=_("Expenditure"))
    subject = models.CharField(max_length=2, blank=True, choices=SUBJECTS,
                               verbose_name=_("Subject"))
    contract = models.FileField(blank=True, upload_to='contracts/',
                                verbose_name=_("Contract PDF"))
    comment = models.TextField(blank=True, verbose_name=_("Comment"))

    # Relationship fields
    vendor = models.ForeignKey(Vendor, default=1, on_delete=models.PROTECT,
                               verbose_name=_("Vendor"))

    class Meta:
        ordering = ['-active', 'name']
        verbose_name = _("Contract")
        verbose_name_plural = _("Contracts")

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('contract', args=[str(self.pk)])


class Budget(models.Model):
    """Yearly budget for Contracts"""

    valid_from = models.DateField(default=timezone.localdate,
                                  verbose_name=_("Begin date"))
    valid_for = models.SmallIntegerField(verbose_name=_("Validity in month"))
    value = MoneyField(max_digits=11, decimal_places=2, default_currency='EUR',
                       verbose_name=_("Value"))
    comment = models.TextField(blank=True, verbose_name=_("Comment"))

    # Relationship fields
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT,
                                 verbose_name=_("Contract"))

    class Meta:
        verbose_name = _("Budget")
        verbose_name_plural = _("Budgets")

    def __str__(self):
        return "{} {}".format(self.valid_from, self.contract.name)


class Invoice(models.Model):
    """Model for received invoices"""

    name = models.CharField(max_length=200, verbose_name=_("Invoice"),
                            default=_("Invoice"))
    date = models.DateField(default=timezone.localdate,
                            verbose_name=_("Date of invoice"))
    value = MoneyField(max_digits=11, decimal_places=2, default_currency='EUR',
                       verbose_name=_("Value"))
    number = models.CharField(max_length=200, blank=True, default='--',
                              verbose_name=_("Order Number"))
    expenditure = models.CharField(max_length=1, choices=EXPENDITURES,
                                   blank=True, verbose_name=_("Expenditure"))
    subject = models.CharField(max_length=2, blank=True, choices=SUBJECTS,
                               verbose_name=_("Subject"))
    comment = models.TextField(blank=True, verbose_name=_("Comment"))

    # Relationship fields
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL,
                                 null=True, blank=True, default=None,
                                 verbose_name=_("Contract"))
    vendor = models.ForeignKey(Vendor, default=None, on_delete=models.SET_NULL,
                               null=True, blank=True, verbose_name=_("Vendor"))

    class Meta:
        ordering = ['-date']
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('invoice', args=[str(self.pk)])

    def get_expenditure(self):
        if self.contract:
            return self.contract.expenditure
        else:
            return self.expenditure

    def get_subject(self):
        if self.contract:
            return self.contract.subject
        else:
            return self.subject


class NewDocumentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(invoice__isnull=True)


class InvoiceDocument(models.Model):
    """Model for the PDF document of received invoices"""

    name = models.CharField(max_length=50, verbose_name=_("Document"),
                            default=_("Invoice"))
    pdf = models.FileField(upload_to='invoices/',
                           verbose_name=_("PDF Document"))
    thumb = models.ImageField(upload_to='invoices/images/', editable=False,
                              verbose_name=_("PDF Preview"))
    modified = models.DateTimeField(auto_now=True,
                                    verbose_name=_("Date Modified"))

    # Relationship fields
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True,
                                default=None, related_name='documents',
                                verbose_name=_("Invoice"))

    # Custom manager
    objects = models.Manager()
    unassigned = NewDocumentManager()

    class Meta:
        ordering = ['-modified']
        verbose_name = _("Invoice Document")
        verbose_name_plural = _("Invoice Documents ")

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('invoice_pdf', args=[str(self.pk)])
