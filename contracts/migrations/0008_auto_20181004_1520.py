# Generated by Django 2.1.2 on 2018-10-04 13:20

from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0007_auto_20181002_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singleinvoice',
            name='vendor',
        ),
        migrations.AlterModelOptions(
            name='budget',
            options={'verbose_name': 'Budget', 'verbose_name_plural': 'Budgets'},
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Contract', 'verbose_name_plural': 'Contracts'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name': 'Invoice', 'verbose_name_plural': 'Invoices'},
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name': 'Vendor', 'verbose_name_plural': 'Vendors'},
        ),
        migrations.AddField(
            model_name='invoice',
            name='expenditure',
            field=models.CharField(blank=True, choices=[('', 'unknown'), ('c', 'CAPEX'), ('o', 'OPEX')], max_length=1, verbose_name='Expenditure'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='number',
            field=models.CharField(blank=True, max_length=200, verbose_name='Order Number'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='subject',
            field=models.CharField(blank=True, choices=[('', 'unknown'), ('hw', 'Hardware'), ('sw', 'Software'), ('ps', 'Service')], max_length=2, verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='contracts.Vendor', verbose_name='Vendor'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='value_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('NOK', 'NOK'), ('USD', 'USD $')], default='EUR', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contracts.Contract', verbose_name='Contract'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice',
            field=models.FileField(upload_to='invoices/', verbose_name='Invoice PDF'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='value_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('NOK', 'NOK'), ('USD', 'USD $')], default='EUR', editable=False, max_length=3),
        ),
        migrations.DeleteModel(
            name='SingleInvoice',
        ),
    ]