# Generated by Django 2.0.2 on 2018-02-28 12:43

import apps.utils.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=apps.utils.storage.ImageStorage(), upload_to='carousel/%Y/%m', verbose_name='轮播')),
                ('content', models.CharField(max_length=20, verbose_name='图片内容')),
                ('added_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播',
                'verbose_name_plural': '轮播',
            },
        ),
    ]