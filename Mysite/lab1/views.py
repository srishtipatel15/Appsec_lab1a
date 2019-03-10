import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.http import JsonResponse


import newspaper
from nltk import word_tokenize
import enchant
import re


# Create your views here.
def index(request):
    template = loader.get_template("lab1/index.html")
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(template.render())

def spellcheck(request):
    try:
        text = request.GET['text']
    except:
        return HttpResponse("Error: No text detected", status = 500)
    # print(request)
    # # my_article = newspaper.Article(url,language='en')
    # # my_article.download()
    # my_article.parse()

    # text = "I am a very good boy guddy boay";
    d = enchant.Dict("en_US")

    byteList = list(set([word.encode('ascii', 'ignore') for word in word_tokenize(text) if d.check(word) is False and re.match('^[a-zA-Z ]*$',word)] ))
    finlist=list()
    for i in byteList:
        finlist.append(i.decode("utf-8"))
    return JsonResponse({'data':finlist})
