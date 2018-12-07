# Generated by Django 2.1.2 on 2018-10-11 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0013_auto_20181011_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='document',
        ),
        migrations.AddField(
            model_name='invoicedocument',
            name='invoice',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documents', to='contracts.Invoice', verbose_name='Invoice'),
        ),
    ]