# Generated by Django 3.0 on 2023-03-12 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20230312_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation2',
            name='barberId',
        ),
        migrations.RemoveField(
            model_name='reservation2',
            name='restaurantId',
        ),
        migrations.AddField(
            model_name='barbershop',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reservation2',
            name='restaurant',
            field=models.ManyToManyField(to='api.Restaurants'),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('party_size', models.IntegerField(null=True)),
                ('rate', models.IntegerField(null=True)),
                ('restaurant', models.ManyToManyField(to='api.Restaurants')),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ManyToManyField(to='api.Restaurants')),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.CharField(max_length=500, null=True)),
                ('party_size', models.IntegerField(null=True)),
                ('comment', models.CharField(max_length=500, null=True)),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
    ]
