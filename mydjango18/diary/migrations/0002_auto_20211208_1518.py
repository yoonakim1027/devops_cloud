# Generated by Django 3.2.9 on 2021-12-08 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '댓글', 'verbose_name_plural': '댓글 목록'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '포스팅', 'verbose_name_plural': '포스팅 목록'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '태그', 'verbose_name_plural': '태그 목록'},
        ),
    ]
