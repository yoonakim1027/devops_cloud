# Generated by Django 3.2.9 on 2021-11-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoona', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pets',
            name='중성화X',
        ),
        migrations.AddField(
            model_name='pets',
            name='neutralOX',
            field=models.NullBooleanField(),
        ),
    ]
