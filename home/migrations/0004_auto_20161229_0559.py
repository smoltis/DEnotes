# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='descr1',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='descr2',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='descr3',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='headline',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro1',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro2',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro3',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subheader1',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subheader2',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subheader3',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]