# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20170430_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psyptitemdef',
            name='psy_pt',
        ),
        migrations.RemoveField(
            model_name='psyptitemdef',
            name='psy_pt_domain',
        ),
        migrations.RemoveField(
            model_name='psyptitemdef',
            name='psy_pt_item',
        ),
        migrations.AddField(
            model_name='psyptitem',
            name='facet',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='psyptitem',
            name='keyed',
            field=models.TextField(default='+'),
        ),
        migrations.AddField(
            model_name='psyptitem',
            name='psy_pt_domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.PSYPTDomain'),
        ),
        migrations.DeleteModel(
            name='PSYPTItemDef',
        ),
    ]