from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def index(request):
    return render(request,"core\index.html")

def contacto(request):
    return render(request,"core/contacto.html")

def acercade(request):
    return render(request,"core/acercade.html")

def contactar(request):
    if request.method == "POST":
        asunto= 'Formulario de contacto:' + request.POST['nombre']
        mensaje= '\n Documento: '+ request.POST['documento']  + ' \n Telefono: ' + request.POST['telefono'] + '\n Email: ' + request.POST['email'] + '\n Direccion: '+ request.POST['direccion']  + ' \n Ciudad: ' + request.POST['ciudad']+ '\n'+ request.POST['mensaje']
        email_desde= settings.EMAIL_HOST_USER
        email_para= ['Cobranzasc2g1@gmail.com']
        print("Asunto: " , asunto)
        print("Mensaje: " , mensaje)
        send_mail(asunto, mensaje,email_desde,email_para, fail_silently=False)
        return render(request, "core\contactoexitoso.html")
    return render(request,"core/contacto.html")