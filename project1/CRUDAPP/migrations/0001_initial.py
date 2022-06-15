# Generated by Django 4.0.3 on 2022-04-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptop_id', models.IntegerField()),
                ('name', models.CharField(max_length=70)),
                ('brand', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=20)),
                ('rom', models.CharField(max_length=20)),
                ('processor', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]
