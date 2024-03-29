# Generated by Django 4.0.2 on 2022-02-23 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id_procedure', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
                ('procedures', models.ManyToManyField(to='main.Procedure')),
            ],
        ),
    ]
