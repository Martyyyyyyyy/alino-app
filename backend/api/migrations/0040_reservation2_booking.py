# Generated by Django 3.0 on 2023-03-22 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_remove_reservation2_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation2',
            name='booking',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Booking'),
        ),
    ]
