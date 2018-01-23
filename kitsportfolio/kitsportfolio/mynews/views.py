# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
#from botocore.vendored.requests.api import request

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<dr>this is my blog</dr>")