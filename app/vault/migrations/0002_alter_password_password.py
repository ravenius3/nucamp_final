# Generated by Django 3.2.2 on 2023-06-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(default='M;~"teOA3EM', max_length=100),
        ),
    ]
