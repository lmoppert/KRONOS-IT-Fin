from django.contrib import admin
from contracts import models


class BudgetInline(admin.TabularInline):
    model = models.Budget
    exclude = ['comment']
    show_change_link = True
    extra = 0


class ContractInline(admin.TabularInline):
    model = models.Contract
    exclude = ['comment']
    show_change_link = True
    extra = 0


class InvoiceInline(admin.TabularInline):
    model = models.Invoice
    exclude = ['comment']
    order = ['-date']
    show_change_link = True
    extra = 0


@admin.register(models.InvoiceDocument)
class InvoiceDocuemnt(admin.ModelAdmin):
    model = models.InvoiceDocument


@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):
    model = models.Contract
    inlines = [BudgetInline, InvoiceInline]
    list_display = ['name', 'number', 'vendor', 'active']
    search_fields = ['name', 'number', 'comment']
    list_filter = ['expenditure', 'subject', 'active']


@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    model = models.Vendor
    inlines = [ContractInline, InvoiceInline]


@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    model = models.Invoice
    order = ['-date']
    list_display = ['name', 'date', 'number', 'vendor', 'value']
    search_fields = ['name', 'contract__name', 'vendor__name', 'comment']
    list_filter = ['expenditure', 'subject']
