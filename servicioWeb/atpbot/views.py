from django.shortcuts import render
from django.http import JsonResponse
import db
import scraping

def root(request):
	data={"status":"OK"}
	return JsonResponse(data,safe=False)

def status(request):
	data={"status":"OK"}
	return JsonResponse(data,safe=False)

def Clasificacion(request):
	clasif=scraping.mostrarClasificacion(5)
	data={"Clas":clasif}
	return JsonResponse(data,safe=False)

