from django.shortcuts import render
from django.http import HttpResponse # モジュールの読み込み

# Create your views here.
def hellofunction(request):
    return HttpResponse('Hello World!')