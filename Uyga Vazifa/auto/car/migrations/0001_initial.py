# Generated by Django 5.1.1 on 2024-09-17 13:54

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
                ('model', models.CharField(max_length=50)),
                ('max_speed', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=20)),
                ('production_year', models.IntegerField(default=2000)),
                ('marka_car', models.CharField(max_length=50)),
            ],
        ),
    ]
