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
    # selected_num = request.POST['number']
    # if selected_num = 1:
    #     selected_num.votes += 1
    #     selected_num.save()
    context = {
        'range': range(1,13)
    }
    try:
        selected_num = request.POST['number']

    except (KeyError, request.POST['number'].DoesNotExist):
        return render(request, 'indexhtml', {
            'error_message': "Input num.",
        })

    else:
        selected_num.votes += 1
        selected_num.save()
    return HttpResponseRedirect(reverse('static_num' , context))
