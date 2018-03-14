# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime  import datetime

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=20,default="")
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    login                 = models.CharField(max_length=20, default="")
    senha                 = models.CharField(max_length=20, default="")
    senha2                = models.CharField(max_length=20, default="")
    visivel               = models.CharField(max_length=1,  default="N")

    nome                  = models.CharField(max_length=100, default="")
    email                 = models.EmailField(max_length=100, default="nobody@dominio.br")
    celular               = models.CharField(max_length=11, default="")
    cidade                = models.CharField(max_length=40, default="")
    estado                = models.CharField(max_length=2, default="")
    objetivo              = models.CharField(max_length=100, default="")
    descricao             = models.TextField(default="")
    nome2                 = models.CharField(max_length=100, default="")

    areadeatuacao         = models.TextField(default="")
    perfil                = models.TextField(default="")
    historicoprofissional = models.TextField(default="")
    formacao              = models.TextField(default="")
    conhecimentos         = models.TextField(default="")
    cursos                = models.TextField(default="")
    idiomas               = models.TextField(default="")
    dadospessoais         = models.TextField(default="")

    def __str__(self):
        #return self.title
         return self.nome
    class Meta:
        verbose_name_plural = "Posts"






