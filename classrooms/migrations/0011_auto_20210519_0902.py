# Generated by Django 3.2 on 2021-05-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0010_classroom_started'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='description',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='day',
            name='description',
            field=models.CharField(max_length=2048),
        ),
    ]
