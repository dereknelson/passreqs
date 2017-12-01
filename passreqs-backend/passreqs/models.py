from __future__ import unicode_literals
from django.db import models

class Website(models.Model):
    url        = models.CharField(max_length=100)
    passreqs   = models.ForeignKey(PassReqs, related_name="passreqs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-url"]

    def __str__(self):
        return "%s, %s"%(self.url, self.passreqs)

class PassReqs(models.Model):
    length             = models.CharField(max_length=3)
    special_characters = bool
    capitals           = bool
    complex            = bool

