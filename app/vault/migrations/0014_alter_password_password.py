# Generated by Django 3.2.2 on 2023-06-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0013_alter_password_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(default='*/_%Tt(hQr', max_length=100),
        ),
    ]
