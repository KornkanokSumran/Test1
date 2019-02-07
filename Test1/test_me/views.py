from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def multi(request,id):
    num = str(id) *3
    return HttpResponse(num)
