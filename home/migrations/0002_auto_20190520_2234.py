# Generated by Django 2.2.1 on 2019-05-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stonebase',
            name='image',
        ),
        migrations.AddField(
            model_name='stonebase',
            name='images',
            field=models.FileField(blank=True, upload_to='upload_image'),
        ),
    ]
