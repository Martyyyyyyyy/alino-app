# Generated by Django 3.0 on 2023-03-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_reservation2_restaurantid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation2',
            name='duration',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
