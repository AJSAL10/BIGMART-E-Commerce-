# Generated by Django 4.1.3 on 2022-12-07 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='category',
            new_name='categorydb',
        ),
    ]