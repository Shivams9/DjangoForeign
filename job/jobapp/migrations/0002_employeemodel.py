# Generated by Django 4.1.4 on 2023-05-09 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.jobmodel')),
            ],
        ),
    ]
