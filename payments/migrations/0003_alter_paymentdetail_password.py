# Generated by Django 4.1.7 on 2023-03-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_remove_paymentdetail_card_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetail',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
