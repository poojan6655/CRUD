# Generated by Django 3.2.5 on 2021-07-31 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('contactno', models.IntegerField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('contactno', models.IntegerField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
    ]
