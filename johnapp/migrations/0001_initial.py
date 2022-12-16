# Generated by Django 4.1.4 on 2022-12-16 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_type', models.CharField(choices=[('Web3', 'Web3'), ('Blockchain', 'Blockchain'), ('IoT', 'IoT'), ('Data Analytics', 'Data Analytics'), ('Ethereum', 'Ethereum')], max_length=100)),
                ('event_date', models.DateTimeField()),
                ('duration', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('target_group', models.CharField(choices=[('Students', 'Students'), ('Employees', 'Employees'), ('Both', 'Both')], max_length=100)),
            ],
        ),
    ]
