
from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import Calculatort
def index(request):
    calculatorts = Calculatort.objects.all()
    context = {'calculatorts': calculatorts}
    return render(request, 'index.html', context)
def create(request):
    val1=request.POST["expression"]
    res= eval(val1)
    calculatort = Calculatort(expression=val1, results=res)
    calculatort.save()
    return redirect('/')