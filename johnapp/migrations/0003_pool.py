# Generated by Django 4.1.4 on 2022-12-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('johnapp', '0002_alter_register_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pnumber', models.CharField(max_length=100)),
                ('interest', models.CharField(max_length=100)),
            ],
        ),
    ]