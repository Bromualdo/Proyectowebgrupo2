# Generated by Django 4.1.2 on 2022-10-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celulares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca',models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
