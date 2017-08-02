# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["text", "publish_date", "choice_count"]

    def choice_count(self, obj):
        return obj.choice_set.count()

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["votes", "text", "question"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
