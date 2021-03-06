# Generated by Django 3.2.9 on 2021-11-23 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211116_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpart',
            name='replacable',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CarBrokenPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('qty', models.IntegerField()),
                ('repairable', models.BooleanField(blank=True, null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='broken_parts', to='api.car')),
            ],
            options={
                'verbose_name': 'Car Broken Part',
                'verbose_name_plural': 'Car Broken Part',
            },
        ),
    ]
