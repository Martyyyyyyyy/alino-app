# Generated by Django 3.0 on 2023-03-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20230312_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbershop',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
