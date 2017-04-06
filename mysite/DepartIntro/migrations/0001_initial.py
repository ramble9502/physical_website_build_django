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
            name='Department_Characteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reformation', models.TextField(max_length=300, verbose_name='\u6cbf\u9769')),
                ('goal', models.TextField(max_length=300, verbose_name='\u8a2d\u7acb\u76ee\u6a19')),
                ('ability_pointer', models.TextField(max_length=300, verbose_name='\u80fd\u529b\u6307\u6a19')),
                ('characteristic', models.TextField(max_length=300, verbose_name='\u7279\u8272')),
                ('future_development', models.TextField(max_length=300, verbose_name='\u7cfb\u6240\u672a\u4f86\u767c\u5c55')),
                ('graduate_job', models.TextField(max_length=300, verbose_name='\u5b78\u751f\u7562\u696d\u51fa\u8def')),
            ],
            options={
                'db_table': 'Department_Characteristic',
                'verbose_name': '\u4e0a\u50b3\u7cfb\u6240\u7279\u8272',
                'verbose_name_plural': '\u7cfb\u6240\u7279\u8272',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u6559\u5ba4\u540d\u7a31')),
                ('description', models.TextField(max_length=300, verbose_name='\u8a2d\u5099\u63cf\u8ff0')),
            ],
            options={
                'db_table': 'Equipment',
                'verbose_name': '\u4e0a\u50b3\u8a2d\u5099\u5167\u5bb9',
                'verbose_name_plural': '\u6240\u8fa6\u8a2d\u5099',
            },
        ),
        migrations.CreateModel(
            name='Legislation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Legislation',
                'verbose_name': '\u4e0a\u50b3\u884c\u653f\u6cd5\u898f',
                'verbose_name_plural': '\u884c\u653f\u6cd5\u898f',
            },
        ),
        migrations.CreateModel(
            name='Their_official_regulations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u6a19\u984c')),
                ('goal', models.TextField(max_length=500, verbose_name='\u76ee\u6a19')),
                ('regulation', models.TextField(max_length=500, verbose_name='\u7d30\u9805')),
            ],
            options={
                'db_table': 'Their_official_regulations',
                'verbose_name': '\u4e0a\u50b3\u4fee\u696d\u898f\u5b9a',
                'verbose_name_plural': '\u4fee\u696d\u898f\u5b9a',
            },
        ),
        migrations.CreateModel(
            name='Upload_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='departintro/file', verbose_name='\u9644\u4ef6\u6a94\u6848')),
                ('filename', models.CharField(max_length=50, verbose_name='\u9644\u4ef6\u6a94\u6848\u540d\u7a31')),
            ],
        ),
        migrations.CreateModel(
            name='Dep_promotion_Point',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DepartIntro.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion', to='DepartIntro.Legislation')),
            ],
            options={
                'db_table': 'Dep_promotion_Point',
                'verbose_name_plural': '\u6559\u5e2b\u5347\u7b49\u76f8\u95dc\u8981\u9ede',
            },
            bases=('DepartIntro.upload_file',),
        ),
        migrations.CreateModel(
            name='Other_Point',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DepartIntro.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='point', to='DepartIntro.Legislation')),
            ],
            options={
                'db_table': 'Other_Point',
                'verbose_name_plural': '\u5176\u4ed6\u76f8\u95dc\u8981\u9ede',
            },
            bases=('DepartIntro.upload_file',),
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DepartIntro.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scholar', to='DepartIntro.Legislation')),
            ],
            options={
                'db_table': 'Scholarship',
                'verbose_name_plural': '\u734e\u5b78\u91d1\u76f8\u95dc\u8981\u9ede',
            },
            bases=('DepartIntro.upload_file',),
        ),
    ]
