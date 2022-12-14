# Generated by Django 4.1.2 on 2022-10-26 07:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0013_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notification',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='displays.thread'),
        ),
    ]
