# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.conf import settings
from . import reddit_flair_prediction as rdf
# Create your views here.
def index(request):
    
    if request.method == 'POST':
        
        model = settings.MODEL_FILE
        val = request.POST.get('url')
        return render(request,"flair_detector/index.html",{"output":rdf.detect_flair(val,model)[0]})

    return render(request,"flair_detector/index.html")




