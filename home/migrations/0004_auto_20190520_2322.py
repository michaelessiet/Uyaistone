# Generated by Django 2.2.1 on 2019-05-20 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190520_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stone',
            name='images',
            field=models.ImageField(blank=True, upload_to='upload_image'),
        ),
    ]
