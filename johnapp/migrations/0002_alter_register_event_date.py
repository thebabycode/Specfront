# Generated by Django 4.1.4 on 2022-12-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('johnapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='event_date',
            field=models.DateField(),
        ),
    ]