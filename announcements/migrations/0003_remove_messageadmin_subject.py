# Generated by Django 3.2 on 2021-06-02 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_announcementadmin_messageadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageadmin',
            name='subject',
        ),
    ]
