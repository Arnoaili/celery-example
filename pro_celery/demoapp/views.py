# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render

from demoapp.tasks import *

# Create your views here.

def test():
    print "celery test: "
    add.delay(2,7)
