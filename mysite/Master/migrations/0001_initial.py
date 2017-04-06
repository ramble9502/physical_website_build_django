# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-16 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bachelor_Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filetitle', models.IntegerField(choices=[(1, '\u5b78\u4f4d\u8003\u8a66\u76f8\u95dc\u6a94\u6848\u4e0b\u8f09'), (2, '\u7814\u7a76\u8a08\u756b\u53e3\u8a66\u76f8\u95dc\u6a94\u6848'), (3, '\u8ad6\u6587\u53e3\u8a66\u76f8\u95dc\u6a94\u6848')], verbose_name='\u6a94\u6848\u985e\u5225')),
            ],
            options={
                'db_table': 'Bachelor_Test',
                'verbose_name': '\u4e0a\u50b3\u5b78\u4f4d\u8003\u8a66\u8868\u683c',
                'verbose_name_plural': '\u5b78\u4f4d\u8003\u8a66\u8868\u683c\u4e0b\u8f09',
            },
        ),
        migrations.CreateModel(
            name='Course_Architecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filetitle', models.CharField(max_length=50, verbose_name='\u6a94\u6848\u540d\u7a31')),
            ],
            options={
                'db_table': 'Course_Architectur',
                'verbose_name': '\u4e0a\u50b3\u8ab2\u7a0b\u67b6\u69cb\u3002\u4fee\u696d\u8981\u9ede',
                'verbose_name_plural': '\u8ab2\u7a0b\u67b6\u69cb\u3002\u4fee\u696d\u8981\u9ede',
            },
        ),
        migrations.CreateModel(
            name='Graduatedpaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u5b78\u5e74\u5ea6/\u6a19\u984c')),
                ('year', models.IntegerField(default=1, verbose_name='\u5b78\u5e74\u5ea6')),
            ],
            options={
                'db_table': 'Graduatedpaper',
                'verbose_name': '\u4e0a\u50b3\u7562\u696d\u8ad6\u6587\u8cc7\u6599',
                'verbose_name_plural': '\u7562\u696d\u8ad6\u6587\u767c\u8868',
            },
        ),
        migrations.CreateModel(
            name='Graduatedpaper_Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=50, verbose_name='\u767c\u8868\u4eba(\u7b2c\u4e00\u4f5c\u8005)')),
                ('papertopic', models.CharField(blank=True, max_length=50, verbose_name='\u8ad6\u6587\u984c\u76ee')),
                ('advisor', models.CharField(blank=True, max_length=50, verbose_name='\u6307\u5c0e\u6559\u6388')),
                ('graduatedyear', models.CharField(blank=True, max_length=50, verbose_name='\u7562\u696d\u5e74\u5ea6')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graduatedpaper', to='Master.Graduatedpaper')),
            ],
            options={
                'db_table': 'Graduatedpaper_Upload',
                'verbose_name_plural': '\u7576\u5e74\u5ea6\u767c\u8868\u8cc7\u6599',
            },
        ),
        migrations.CreateModel(
            name='Schoolpaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u5b78\u5e74\u5ea6/\u6a19\u984c')),
                ('year', models.IntegerField(default=1, verbose_name='\u5b78\u5e74\u5ea6')),
            ],
            options={
                'db_table': 'Schoolpaper',
                'verbose_name': '\u4e0a\u50b3\u5728\u6821\u8ad6\u6587\u8cc7\u6599',
                'verbose_name_plural': '\u5728\u6821\u8ad6\u6587\u767c\u8868',
            },
        ),
        migrations.CreateModel(
            name='Schoolpaper_Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='\u65e5\u671f')),
                ('seminar', models.TextField(max_length=500, verbose_name='\u7814\u8a0e\u6703\u540d\u7a31')),
                ('papertopic', models.TextField(max_length=100, verbose_name='\u8ad6\u6587\u984c\u76ee')),
                ('publication', models.CharField(max_length=100, verbose_name='\u767c\u8868\u65b9\u5f0f')),
                ('author', models.CharField(max_length=4, verbose_name='\u767c\u8868\u4eba(\u7b2c\u4e00\u4f5c\u8005)')),
                ('advisor', models.CharField(max_length=50, verbose_name='\u6307\u5c0e\u6559\u6388')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schoolpaper', to='Master.Schoolpaper')),
            ],
            options={
                'db_table': 'Schoolpaper_Upload',
                'verbose_name_plural': '\u7576\u5e74\u5ea6\u767c\u8868\u8cc7\u6599',
            },
        ),
        migrations.CreateModel(
            name='Seminar_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u6a19\u984c\u540d\u7a31')),
                ('file1', models.FileField(blank=True, upload_to='master/file', verbose_name='\u9644\u4ef6\u6a94\u68481')),
                ('file2', models.FileField(blank=True, upload_to='master/file', verbose_name='\u9644\u4ef6\u6a94\u68482')),
                ('image', models.ImageField(blank=True, default='', upload_to='master/image', verbose_name='\u4ee3\u8868\u5716\u7247')),
                ('link', models.URLField(blank=True, verbose_name='\u9023\u7d50')),
            ],
            options={
                'db_table': 'Seminar_Information',
                'verbose_name': '\u4e0a\u50b3\u7814\u8a0e\u6703\u8cc7\u8a0a',
                'verbose_name_plural': '\u7814\u8a0e\u6703\u8cc7\u8a0a',
            },
        ),
        migrations.CreateModel(
            name='Study_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6a19\u984c\u540d\u7a31')),
                ('year', models.IntegerField(default=1, verbose_name='\u5b78\u5e74\u5ea6')),
            ],
            options={
                'db_table': 'Study_Group',
                'verbose_name': '\u4e0a\u50b3\u7814\u7a76\u751f\u8b80\u66f8\u6703',
                'verbose_name_plural': '\u78a9\u58eb\u73ed\u7814\u7a76\u751f\u8b80\u66f8\u6703',
            },
        ),
        migrations.CreateModel(
            name='Upload_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='master/file', verbose_name='\u9644\u4ef6\u6a94\u68481')),
                ('file2', models.FileField(blank=True, upload_to='master/file', verbose_name='\u9644\u4ef6\u6a94\u68482')),
                ('filename', models.CharField(max_length=50, verbose_name='\u9644\u4ef6\u6a94\u6848\u540d\u7a31')),
            ],
        ),
        migrations.CreateModel(
            name='Bachelor_Test_Upload',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Master.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bachelor', to='Master.Bachelor_Test')),
            ],
            options={
                'db_table': 'Bachelor_Test_Upload',
                'verbose_name': '\u5b78\u4f4d\u8003\u8a66\u8868\u683c\u6a94\u6848',
            },
            bases=('Master.upload_file',),
        ),
        migrations.CreateModel(
            name='Course_Architecture_Upload',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Master.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursearchi', to='Master.Course_Architecture')),
            ],
            options={
                'db_table': 'Course_Architecture_Upload',
                'verbose_name_plural': '\u8ab2\u7a0b\u67b6\u69cb\u3002\u4fee\u696d\u8981\u9ede\u6a94\u6848',
            },
            bases=('Master.upload_file',),
        ),
        migrations.CreateModel(
            name='Study_Group_Upload',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Master.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studygroup', to='Master.Study_Group')),
            ],
            options={
                'db_table': 'Study_Group_Upload',
                'verbose_name_plural': '\u7814\u7a76\u751f\u8b80\u66f8\u6703\u6a94\u6848',
            },
            bases=('Master.upload_file',),
        ),
    ]
