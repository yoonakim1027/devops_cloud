# Generated by Django 3.2.10 on 2021-12-16 09:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': '카테고리',
                'verbose_name_plural': '카테고리 목록',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': '태그',
                'verbose_name_plural': '태그 목록',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('content', models.TextField(blank=True)),
                ('telephone', models.CharField(help_text='입력 예) 042-1234-1234', max_length=14, validators=[django.core.validators.RegexValidator('^\\d{3,4}-?\\d{3,4}-?\\d{4}$', message='전화번호를 입력해주세요.')])),
                ('status', models.CharField(choices=[('D', '초안'), ('P', '공개')], db_index=True, default='D', max_length=1)),
                ('tag_set', models.ManyToManyField(blank=True, to='shop.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author_name', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글 목록',
                'ordering': ['author_name'],
            },
        ),
    ]