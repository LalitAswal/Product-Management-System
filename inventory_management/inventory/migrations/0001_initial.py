# Generated by Django 3.1.2 on 2021-06-08 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=15)),
                ('location_id', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=15)),
                ('product_id', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_id', models.PositiveIntegerField(unique=True)),
                ('timestamp', models.TimeField()),
                ('from_location', models.CharField(blank=True, max_length=15)),
                ('to_location', models.CharField(blank=True, max_length=15)),
                ('location_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
