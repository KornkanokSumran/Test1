from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def countnum(request):
    Num = request.POST['number']
    try:
        selected_num = Num.objects.get(id=request.POST['number'])

    except (KeyError, request.POST['number'].DoesNotExist):
        return render(request, 'index.html', {
            'error_message': "Input num.",
        })

    else:
        selected_num.count += 1
        selected_num.save()
    return HttpResponseRedirect(reverse('multi.html',args =(Num.id)))
