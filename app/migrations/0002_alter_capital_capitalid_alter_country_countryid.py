# Generated by Django 5.1.3 on 2024-12-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capital',
            name='capitalID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='country',
            name='countryID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
