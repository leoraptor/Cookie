from django.shortcuts import render
from django.shortcuts import HttpResponse

def creatcookiee(request):
    x = HttpResponse('<h1>created by first cookie</h1>')
    x.set_cookie('myfirstcookie','welcome to my first cookie',max_age=None)
    return x

