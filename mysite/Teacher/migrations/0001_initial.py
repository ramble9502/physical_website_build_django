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
            name='Book1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='\u540d\u7a31')),
            ],
            options={
                'db_table': 'Book1',
                'verbose_name_plural': '\u5c08\u66f8',
            },
        ),
        migrations.CreateModel(
            name='Book2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='\u540d\u7a31')),
            ],
            options={
                'db_table': 'Book2',
                'verbose_name_plural': '\u5c08\u66f8',
            },
        ),
        migrations.CreateModel(
            name='Periodical1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='\u540d\u7a31')),
            ],
            options={
                'db_table': 'Periodical1',
                'verbose_name_plural': '\u671f\u520a\u8ad6\u6587',
            },
        ),
        migrations.CreateModel(
            name='Periodical2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='\u540d\u7a31')),
            ],
            options={
                'db_table': 'Periodical2',
                'verbose_name_plural': '\u671f\u520a\u8ad6\u6587',
            },
        ),
        migrations.CreateModel(
            name='Seminar1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='\u540d\u7a31')),
            ],
            options={
                'db_table': 'Seminar1',
                'verbose_name_plural': '\u7814\u8a0e\u6703\u8ad6\u6587',
            },
        ),
        migrations.CreateModel(
            name='Seminar2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='\u540d\u7a31')),
            ],
            options={
                'db_table': 'Seminar2',
                'verbose_name_plural': '\u7814\u8a0e\u6703\u8ad6\u6587',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
                ('telephone_extension', models.CharField(blank=True, max_length=20, verbose_name='\u5206\u6a5f')),
                ('job', models.CharField(max_length=50, verbose_name='\u6559\u8077\u540d\u7a31')),
                ('Email', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='teacher/image', verbose_name='\u5927\u982d\u8cbc')),
                ('education', models.CharField(blank=True, max_length=100, verbose_name='\u5b78\u6b77')),
                ('specialty', models.CharField(blank=True, max_length=100, verbose_name='\u5c08\u9577')),
                ('course', models.CharField(blank=True, max_length=100, verbose_name='\u8ab2\u7a0b')),
            ],
        ),
        migrations.CreateModel(
            name='Fulltime_Teacher',
            fields=[
                ('teacher_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Teacher.Teacher')),
            ],
            options={
                'db_table': 'Fulltime_Teacher',
                'verbose_name': '\u4e0a\u50b3\u6559\u6388\u8cc7\u8a0a',
                'verbose_name_plural': '\u5c08\u4efb\u5e2b\u8cc7',
            },
            bases=('Teacher.teacher',),
        ),
        migrations.CreateModel(
            name='Parttime_Teacher',
            fields=[
                ('teacher_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Teacher.Teacher')),
                ('experience', models.TextField(blank=True, default='', max_length=200, verbose_name='\u7d93\u6b77')),
                ('year', models.CharField(blank=True, default='', max_length=50, verbose_name='\u6700\u65b0\u5e74\u5ea6')),
            ],
            options={
                'db_table': 'Parttime_Teacher',
                'verbose_name': '\u4e0a\u50b3\u6559\u5e2b\u8cc7\u8a0a',
                'verbose_name_plural': '\u517c\u4efb\u5e2b\u8cc7',
            },
            bases=('Teacher.teacher',),
        ),
        migrations.AddField(
            model_name='seminar2',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seminar2', to='Teacher.Parttime_Teacher'),
        ),
        migrations.AddField(
            model_name='seminar1',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seminar1', to='Teacher.Fulltime_Teacher'),
        ),
        migrations.AddField(
            model_name='periodical2',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periodical2', to='Teacher.Parttime_Teacher'),
        ),
        migrations.AddField(
            model_name='periodical1',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periodical1', to='Teacher.Fulltime_Teacher'),
        ),
        migrations.AddField(
            model_name='book2',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book2', to='Teacher.Parttime_Teacher'),
        ),
        migrations.AddField(
            model_name='book1',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book1', to='Teacher.Fulltime_Teacher'),
        ),
    ]
