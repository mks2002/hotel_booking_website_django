# Generated by Django 4.2 on 2023-04-12 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_bookinghotel_userpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('useremail', models.EmailField(max_length=50)),
                ('contact_no', models.CharField(max_length=13)),
                ('querydetails', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('querystatus', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=50)),
            ],
        ),
    ]