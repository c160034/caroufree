# Generated by Django 4.1.2 on 2022-10-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0015_remove_notification_date_remove_notification_thread_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='is_read',
            new_name='receiver_read',
        ),
        migrations.AddField(
            model_name='thread',
            name='user_read',
            field=models.BooleanField(default=False),
        ),
    ]