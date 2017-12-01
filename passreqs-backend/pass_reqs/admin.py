# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Website, PassReqs
from django.contrib import admin

# Register your models here.
admin.site.register(Website)

admin.site.register(PassReqs)