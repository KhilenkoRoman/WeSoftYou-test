# Generated by Django 3.2.9 on 2021-11-16 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('qty', models.IntegerField()),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='api.car')),
            ],
            options={
                'verbose_name': 'Car Part',
                'verbose_name_plural': 'Car Parts',
            },
        ),
    ]
