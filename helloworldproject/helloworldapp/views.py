from django.shortcuts import render

def hellofunction(request):
    return render(request, 'helloworldapp/hello.html')