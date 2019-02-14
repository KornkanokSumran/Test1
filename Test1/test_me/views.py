from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render


from .models import Number

def index(request):
    return HttpResponse("Hello")

def multi(request,id):
    number = str(id) *3
    context = {
        'num': number
    }
    return render(request,'index.html',context)

def multiplication(request):
    a = []
    for i in range(1,13):
        answer = int(request.POST['number']) * i
        a.append(answer)
    print(a)
    try:
        selected_num = Number.objects.get(num = request.POST['number'])
    except (KeyError, Number.DoesNotExist):
        selected_num = Number(num=request.POST['number'])
        selected_num.save()
    else:
        selected_num.count += 1
        selected_num.save()
    context = {
        'id': request.POST['number'],
        'num': a,
        'count': selected_num.count
    }
    return render(request, 'multi.html', context)

def inputnum(request):
    return render(request,'index.html')
