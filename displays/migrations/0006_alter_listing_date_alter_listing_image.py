# Generated by Django 4.1.2 on 2022-10-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0005_alter_listing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='listings'),
        ),
    ]
