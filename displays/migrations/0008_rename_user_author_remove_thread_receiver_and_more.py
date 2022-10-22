# Generated by Django 4.1.2 on 2022-10-21 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0007_alter_listing_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Author',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='user',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='user',
            new_name='author',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]