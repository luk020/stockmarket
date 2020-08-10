# Generated by Django 3.0.6 on 2020-08-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_contract_open_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='open_avg',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='avg',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]