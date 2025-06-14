# Generated by Django 5.2 on 2025-06-14 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_remove_bus_travel_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('payment_method', models.CharField(max_length=20)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to='bookings.booking')),
            ],
        ),
    ]
