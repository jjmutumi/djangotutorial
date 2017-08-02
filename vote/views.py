# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
#from django.templates import Template

def index(request):
	return HttpResponse("Hi, there")
