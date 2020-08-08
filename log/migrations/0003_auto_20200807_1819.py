# Generated by Django 3.0.6 on 2020-08-07 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20200807_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='total',
            new_name='open_total',
        ),
        migrations.AddField(
            model_name='contract',
            name='exp',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]