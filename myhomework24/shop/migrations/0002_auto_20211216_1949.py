# Generated by Django 3.2.10 on 2021-12-16 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Review',
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['-id'], 'verbose_name': '상점', 'verbose_name_plural': '상점 목록'},
        ),
    ]
