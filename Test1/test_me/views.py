from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello")

def multi(request,id):
    num = str(id) *3
    context = {
        'number': num
    }
    return render(request,'index.html',context)
