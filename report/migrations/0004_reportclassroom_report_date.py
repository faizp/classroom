# Generated by Django 3.2 on 2021-05-24 15:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_reportclassroom_resolved'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportclassroom',
            name='report_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
