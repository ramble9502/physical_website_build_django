# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-16 03:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finished_Special_Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u6a19\u984c')),
                ('latest_news', models.TextField(max_length=1000, verbose_name='\u6700\u65b0\u6d88\u606f')),
                ('file', models.FileField(blank=True, upload_to='activitynews/file', verbose_name='\u76f8\u95dc\u5831\u540d\u6a94\u6848')),
                ('fans_connect', models.URLField(blank=True, verbose_name='\u7c89\u7d72\u5718\u9023\u7d50')),
                ('related_url', models.URLField(blank=True, verbose_name='\u6d3b\u52d5\u7db2\u5740')),
                ('create_date', models.DateField(default=datetime.date.today, verbose_name='\u516c\u5e03\u65e5\u671f')),
                ('image', models.ImageField(upload_to='activitynews/image', verbose_name='\u4ee3\u8868\u5716\u7247')),
            ],
            options={
                'db_table': 'Finished_Special_Activity',
                'verbose_name': '\u4e0a\u50b3\u6d3b\u52d5\u8a0a\u606f',
                'verbose_name_plural': '\u7279\u6b8a\u6d3b\u52d5',
            },
        ),
        migrations.CreateModel(
            name='Latest_News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='\u6a19\u984c\uff1a')),
                ('content', models.TextField(blank=True, verbose_name='\u4e3b\u984c\u5167\u5bb9:')),
                ('create_date', models.DateField(default=datetime.date.today, verbose_name='\u516c\u5e03\u65e5\u671f')),
            ],
            options={
                'db_table': 'Latest_News',
                'verbose_name': '\u4e0a\u50b3\u6700\u65b0\u8a0a\u606f',
                'verbose_name_plural': '\u6700\u65b0\u8a0a\u606f\u516c\u544a',
            },
        ),
        migrations.CreateModel(
            name='Marqueecontrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='\u8dd1\u99ac\u71c8\u5167\u5bb9')),
            ],
            options={
                'db_table': 'Marqueecontrol',
                'verbose_name': '\u4e0a\u50b3\u8dd1\u99ac\u71c8\u5167\u5bb9',
                'verbose_name_plural': '\u8dd1\u99ac\u71c8',
            },
        ),
        migrations.CreateModel(
            name='Upload_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='activitynews/file', verbose_name='\u9644\u4ef6\u6a94\u68481:')),
                ('file2', models.FileField(blank=True, upload_to='activitynews/file', verbose_name='\u9644\u4ef6\u6a94\u68482:')),
                ('filename', models.CharField(blank=True, max_length=50, verbose_name='\u9644\u4ef6\u6a94\u6848\u540d\u7a31:')),
            ],
        ),
        migrations.CreateModel(
            name='WorkShop_News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='\u6a19\u984c\uff1a')),
                ('content', models.TextField(blank=True, verbose_name='\u4e3b\u984c\u5167\u5bb9:')),
                ('create_date', models.DateField(default=datetime.date.today, verbose_name='\u516c\u5e03\u65e5\u671f')),
            ],
            options={
                'db_table': 'WorkShop_News',
                'verbose_name': '\u4e0a\u50b3\u7814\u7fd2\u8a0a\u606f',
                'verbose_name_plural': '\u7814\u7fd2\u8a0a\u606f\u516c\u544a',
            },
        ),
        migrations.CreateModel(
            name='Latest_News_Class',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ActivityNews.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='latestnews', to='ActivityNews.Latest_News')),
            ],
            bases=('ActivityNews.upload_file',),
        ),
        migrations.CreateModel(
            name='WorkShop_News_Upload',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ActivityNews.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshop', to='ActivityNews.WorkShop_News')),
            ],
            bases=('ActivityNews.upload_file',),
        ),
    ]
