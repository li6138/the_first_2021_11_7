# Generated by Django 3.2 on 2021-11-11 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20211111_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidebar',
            name='pv',
        ),
        migrations.RemoveField(
            model_name='sidebar',
            name='uv',
        ),
    ]
