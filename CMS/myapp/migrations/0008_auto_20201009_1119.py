# Generated by Django 3.1.2 on 2020-10-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20201009_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='currency_short',
            field=models.CharField(choices=[('eur', 'EUR'), ('usd', 'USD'), ('chf', 'CHF')], max_length=100),
        ),
    ]
