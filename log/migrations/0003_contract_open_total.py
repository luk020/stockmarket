# Generated by Django 3.0.6 on 2020-08-08 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20200808_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='open_total',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=8),
            preserve_default=False,
        ),
    ]
