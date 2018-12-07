# Generated by Django 2.1.2 on 2018-10-10 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0010_contract_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Invoice', max_length=50, verbose_name='Document')),
                ('document', models.FileField(upload_to='invoices/', verbose_name='PDF Document')),
                ('thumb', models.ImageField(editable=False, upload_to='invoices/images/', verbose_name='PDF Preview')),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Invoice Document',
                'verbose_name_plural': 'Invoice Documents ',
                'ordering': ['-modified'],
            },
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['-active', 'name'], 'verbose_name': 'Contract', 'verbose_name_plural': 'Contracts'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ['-date'], 'verbose_name': 'Invoice', 'verbose_name_plural': 'Invoices'},
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='invoice',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.CharField(blank=True, default='--', max_length=200, verbose_name='Order Number'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='document',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contracts.InvoiceDocument', verbose_name='Invoice Document'),
        ),
    ]
