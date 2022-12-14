# Generated by Django 4.1 on 2022-09-26 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('luggage', models.IntegerField()),
                ('air_conditioning', models.BooleanField()),
                ('transmission', models.CharField(max_length=100)),
                ('mileage', models.CharField(max_length=100)),
            ],
        ),
    ]
