# Generated by Django 4.1.4 on 2022-12-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('johnapp', '0003_pool'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='fname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='pool',
            name='lname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
