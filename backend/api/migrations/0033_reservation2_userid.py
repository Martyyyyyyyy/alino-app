# Generated by Django 3.0 on 2023-03-16 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_remove_reservation2_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation2',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
