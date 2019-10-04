from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time_info_view(request):
	time=datetime.datetime.now()
	s="<h1>Hello Current Date and Timeis :"+str(time)+"</h1>"
	return HttpResponse(s)