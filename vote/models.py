# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)
