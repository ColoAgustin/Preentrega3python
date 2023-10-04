from django.shortcuts import render
from .models import Pilotos
from AppCoder.forms import PilotosFormulario, BuscaPilotosForm

#def inicio(request):
 #   return render(request, "AppCoder/index.html")

#index para la logica y proceso de formulario
def index(request):
    return render(request, 'index.html')

def pilotos(request):
    return render(request, "AppCoder/pilotos.html")

def fechas(request):
    return render(request, "AppCoder/fechas.html")

def news(request):
    return render(request, "AppCoder/news.html")

#logica de formularios.-
def form_comun(request):

    if request.method == 'POST':
        
        pilotos =  Pilotos(nombre=request.POST['pilotos'],apellido=request.POST['apellido'])
        pilotos.save()
        
        fechas =  Fechas(nombre=request.POST['pilotos'],apellido=request.POST['apellido'])
        fechas.save()

        

        return render(request, "AppCoder/index.html")

    return render(request,"AppCoder/form_comun.html")

def form_con_api(request):
    if request.method == "POST":
        miFormulario = PilotosFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            pilotos = Pilotos(nombre=informacion["pilotos"], apellido=informacion["apellido"])
            pilotos.save()
            
            return render(request, "AppCoder/index.html")
    else:
        miFormulario = PilotosFormulario()

    return render(request, "AppCoder/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaPilotosForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            pilotos = Pilotos.objects.filter(nombre__icontains=informacion["pilotos"])

            return render(request, "AppCoder/resultados_buscar_form.html", {"pilotos": pilotos})
    else:
        miFormulario = BuscaPilotosForm()

    return render(request, "AppCoder/buscar_form_con_api.html", {"miFormulario": miFormulario})