# Generated by Django 4.1.2 on 2022-10-20 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image_name',
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(null=True, upload_to='listings'),
        ),
    ]