# Generated by Django 4.1.7 on 2023-04-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotellist', '0002_alter_hotellist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotellist',
            name='image',
            field=models.FileField(
                default=None, max_length=2500, null=True, upload_to='image_folder_mysql_wamp/'),
        ),
    ]
