# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-13 01:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('login', models.CharField(default='', max_length=20)),
                ('senha', models.CharField(default='', max_length=20)),
                ('senha2', models.CharField(default='', max_length=20)),
                ('visivel', models.CharField(default='N', max_length=1)),
                ('nome', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='nobody@dominio.br', max_length=100)),
                ('celular', models.CharField(default='', max_length=11)),
                ('cidade', models.CharField(default='', max_length=40)),
                ('estado', models.CharField(default='', max_length=2)),
                ('objetivo', models.CharField(default='', max_length=100)),
                ('descricao', models.TextField(default='')),
                ('nome2', models.CharField(default='', max_length=100)),
                ('areadeatuacao', models.TextField(default='')),
                ('perfil', models.TextField(default='')),
                ('historicoprofissional', models.TextField(default='')),
                ('formacao', models.TextField(default='')),
                ('conhecimentos', models.TextField(default='')),
                ('cursos', models.TextField(default='')),
                ('idiomas', models.TextField(default='')),
                ('dadospessoais', models.TextField(default='')),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]