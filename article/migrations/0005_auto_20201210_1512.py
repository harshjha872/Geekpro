# Generated by Django 3.1.1 on 2020-12-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=80),
        ),
    ]
