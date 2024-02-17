# Generated by Django 5.0.2 on 2024-02-17 13:54

import datetime
import django.db.models.deletion
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
                ('code', models.CharField(max_length=100)),
                ('type_item', models.CharField(choices=[('APARTAMENTO', 'APARTAMENTO'), ('KITNET', 'KITNET'), ('CASA', 'CASA')], max_length=100)),
                ('address', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_locate', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Imóvel',
                'verbose_name_plural': 'Imóveis',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Images')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_images', to='myapp.car')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_start', models.DateTimeField(verbose_name='Inicio')),
                ('dt_end', models.DateTimeField(verbose_name='Fim')),
                ('create_at', models.DateField(blank=True, default=datetime.datetime.now)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reg_location', to='myapp.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
            ],
            options={
                'verbose_name': 'Registrar Locação',
                'verbose_name_plural': 'Registrar Locação',
                'ordering': ['-id'],
            },
        ),
    ]