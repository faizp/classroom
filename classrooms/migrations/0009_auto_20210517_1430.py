# Generated by Django 3.2 on 2021-05-17 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0008_classroomenrolled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='sec_category',
        ),
        migrations.RemoveField(
            model_name='testpassed',
            name='sec_category',
        ),
        migrations.RemoveField(
            model_name='testpassed',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='TestPassed',
        ),
    ]
