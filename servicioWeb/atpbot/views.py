from django.shortcuts import render
from django.http import JsonResponse

def root(request):
	 data={"status":"OK"}
	 return JsonResponse(data,safe=False)

def status(request):
	 data={"status":"OK"}
	 return JsonResponse(data,safe=False)
