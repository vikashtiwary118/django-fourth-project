from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greetings_views(request):
	return HttpResponse('<h1>Hello, Friends Good Morning have a Nice Day!!!</h1>')
