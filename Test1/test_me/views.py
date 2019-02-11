from django.http import HttpResponse
from django.shortcuts import render

def multi(request,id):
    num = str(id) *3
    context = {
        'number': num
    }
    return render(request,'index.html',context)

def multiplication(request):
    a = []
    for i in range(1,13):
        answer = int(request.POST['number']) * i
        a.append(answer)
    print(a)
    context = {
        'id': request.POST['number'],
        'num': a
    }
    return render(request, 'multi.html', context)

def inputnum(request):
    return render(request,'index.html')