# Generated by Django 3.2.10 on 2021-12-13 02:34

# [๋ฉํฐ์ฅฐ์๐ฆ] [์ค์  11:45] https://docs.djangoproject.com/ko/3.2/topics/migrations/

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

# ์ ๋ ์๋จ์์ from shop.models. import Category๋ฅผ ํ์ง ๋ง์๊ณ 
# ๋ง์ด๊ทธ๋ ์ด์ ํจ์ ๋ด๋ถ์์ apps๋ฅผ ํตํด ๋ชจ๋ธ ํด๋์ค๋ฅผ ๊ฐ์ ธ์ค์ธ์
# ๋ฐ์์ฒ๋ผ!!


# ์นดํ๊ณ ๋ฆฌ ํ์ด๋ธ์ด ๋ง๋ค์ด์ง๊ณ  ๋์ ์ํ (์ ๋ฐฉํฅ)
def create_dummy_category(apps,schema_editor):
    Category = apps.get_model("shop","Category") # model class
    Category.objects.create(name="dummy") # pk :1

# ์นดํ๊ณ ๋ฆฌ ํ์ด๋ธ์ด ์ญ์ ๋๊ณ  ๋์ ์ํ (์ญ๋ฐฉํฅ)
def delete_dummy_category(apps,schema_editor):
    Category = apps.get_model("shop", "Category")  # model class
    Category.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
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
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': '๋ฆฌ๋ทฐ', 'verbose_name_plural': '๋ฆฌ๋ทฐ ๋ชฉ๋ก'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': '์์ ', 'verbose_name_plural': '์์  ๋ชฉ๋ก'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'ํ๊ทธ', 'verbose_name_plural': 'ํ๊ทธ ๋ชฉ๋ก'},
        ),
        migrations.AddField(
            model_name='shop',
            name='photo',
            field=models.ImageField(default=1, upload_to='diary/post/%Y/%M/%d', verbose_name='์์ฒด ์ฌ์ง'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='author_name',
            field=models.CharField(max_length=20, verbose_name='์์ฑ์ ์ด๋ฆ'),
        ),
        migrations.AlterField(
            model_name='review',
            name='message',
            field=models.TextField(verbose_name='๋ฆฌ๋ทฐ'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(blank=True, verbose_name='์์ฒด ์ค๋ช'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='์์ฒด ๋ช'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='shop.Tag', verbose_name='ํด์ํ๊ทธ'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='telephone',
            field=models.CharField(help_text='์๋ ฅ ์) 042-1234-1234', max_length=14, validators=[django.core.validators.RegexValidator('^\\d{3}-?\\d{4}-?\\d{4}$', message='์ ํ๋ฒํธ๋ฅผ ์๋ ฅํด์ฃผ์ธ์.')], verbose_name='์์ฒด ์ ํ๋ฒํธ'),
        ),
        migrations.AddField(
            model_name='shop',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
            preserve_default=False,
        ),

        migrations.RunPython(create_dummy_category,delete_dummy_category)
    ]

    # ์นดํ๊ณ ๋ฆฌ๋ผ๋ ์ด๋ฆ์ ๋ชจ๋ธ์ ๋ง๋ค๊ณ  makemigrations
    # ์นดํ๊ณ ๋ฆฌ ๋ชจ๋ธ ์์ฑ์ ๋ํ migraion ํ์ผ ์์ฉ
    # create_dummy (์ ๋ฐฉํฅ)
    # delete_dummy (์ญ๋ฐฉํฅ)
    # operations์ ํญ์ ์์๊ฐ ์์



