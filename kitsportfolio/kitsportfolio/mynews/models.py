# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from pyexpat import model

# Create your models here.
class Reporter(models.Model):
        full_name = models.CharField(max_length = 70)
        
        def __str__(self):
            return self.full_name
        
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_legnth=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline