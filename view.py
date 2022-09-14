from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import loader
from appCoder.models import Curso 

def home(self, name):
    return HttpResponse(f'Hola soy la {name}')

def homePage(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data= {'nombre' : 'Josefina' , 'apellido' : 'Ruiz' ,'lista' :lista }
    planilla =  loader.get_template('index.html')
    documento = planilla.render(data)   
    return HttpResponse(documento)

def cursos(self):
    curso = Curso(nombre="UX/UI" , camada= "12345")
    curso.save()
    documento =planilla.render()
    documento = f'Curso: {curso.nombre} camada: {curso.camada}'
    return HttpResponse(documento)

