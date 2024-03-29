# Generated by Django 3.0 on 2023-03-14 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20230314_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorites',
            name='barber',
            field=models.ManyToManyField(to='api.Barbershop'),
        ),
        migrations.AddField(
            model_name='history',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reservation2',
            name='barber',
            field=models.ManyToManyField(to='api.Barbershop'),
        ),
        migrations.AddField(
            model_name='reservation2',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
