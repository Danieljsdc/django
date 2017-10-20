# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-18 08:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_article_temptime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='temptime',
        ),
        migrations.AddField(
            model_name='article',
            name='add_temptime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期'),
        ),
        migrations.AddField(
            model_name='article',
            name='mod_temptime',
            field=models.DateTimeField(auto_now=True, verbose_name='修改日期'),
        ),
    ]