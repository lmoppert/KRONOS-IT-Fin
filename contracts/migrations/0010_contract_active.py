# Generated by Django 2.1.2 on 2018-10-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0009_auto_20181004_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
