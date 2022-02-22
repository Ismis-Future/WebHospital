from django.shortcuts import render

# Create your views here.
def Servicios(request):
    return render(request, 'servicios.html')
