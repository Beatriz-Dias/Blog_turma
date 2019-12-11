from django.shortcuts import render
from .forms import PedidoForms

# Create your views here.
def home(request):
    nome = 'groger'
    # posts = {
    #     'Gabriel' : 'Narnia para projetos ágeis',
    #     'Vinicius': 'IA para comer biscoitos',
    #     'Ana Lu': 'BTS é muito bondoso',
    #     'Downtown': 'Não seja maníaco'
    # }

    lista = ['Roré', 'Generro', 'Anlu', 'DOwnT0wn']
    contexto = {
        'nome': nome,
        'lista': lista
    }
    return render(request, 'home.html', )

def post(request):
    return render(request, 'post.html', contexto)

def cadastro(request):
    form = PedidoForms(request.POST or None)
    if form.is_valid():
        form.save()
        contexto = {
            'msg':"Pedido de certo!"
        
    }    

        return render(request, 'cadastro.html', contexto)
    contexto = {
        'formulario':form 
    }
    return render(request, 'cadastro.html', contexto)
