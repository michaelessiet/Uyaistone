# Generated by Django 2.2.1 on 2019-05-20 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190520_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='stone',
            name='shortdesc',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
