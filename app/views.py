from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html') #返回页面

def a(request):
    return HttpResponse('hello')  #直接返回内容
