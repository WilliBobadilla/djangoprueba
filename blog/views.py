from django.shortcuts import render,HttpResponse

from .models import MyModelName 


# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})



def index(request):
    return render(request, 'blog/index.html', {})


def posteo(request):
	if request.method=='POST':  #preguntamos si el metodo es post 
		print("sdfaf")
		nombre=request.POST['inputName']  #recibimos datos del post para luego guardarlos 
		usu=MyModelName()   #instanciamos la clase usuarios y creamos el objeto usu
		usu.nombre=nombre  #cambiamos el atributo del objeto instanciado 
		usu.save()   #guardamos los datos del post
		return HttpResponse("<h1>Me enviaste un post <a href='/'> Ir a la lista</a></h1>")
	return HttpResponse("no me enviaste nada ")