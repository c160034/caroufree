# Generated by Django 4.1.2 on 2022-10-25 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0010_thread_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='displays.thread'),
        ),
    ]