# Generated by Django 3.1.1 on 2020-12-03 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201203_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='image',
        ),
    ]