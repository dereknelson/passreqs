from __future__ import unicode_literals
from django.db import models

class Website(models.Model):
    url        = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-url"]

    def __str__(self):
        return "%s"%(self.url)



class PassReqs(models.Model):
    website            = models.CharField(max_length=50, null=True)
    length             = models.CharField(max_length=3)
    special_characters = models.DecimalField(decimal_places=0, max_digits=1, default=0)
    capitals           = models.DecimalField(decimal_places=0, max_digits=1, default=0)
    complex            = models.DecimalField(decimal_places=0, max_digits=1, default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["-website"]

    def __str__(self):
        return "%s"%(self.website)