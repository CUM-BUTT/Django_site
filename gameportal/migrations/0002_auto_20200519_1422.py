# Generated by Django 3.0.2 on 2020-05-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
