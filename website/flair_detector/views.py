# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        val = request.POST.get('url')
        print(val)
        return render(request,"flair_detector/index.html",{"output":val})

    return render(request,"flair_detector/index.html")