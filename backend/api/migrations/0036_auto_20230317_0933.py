# Generated by Django 3.0 on 2023-03-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_booking_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbershop',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
