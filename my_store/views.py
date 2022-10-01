from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def home_page(request):
    context = {
        "title": "Pagina principal",
        "content": "Bem vindo a página principal"
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        "title": "Pagina sobre",
        "content": "Bem vindo a página sobre"
    }
    return render(request, 'about/view.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de contato",
        "content": "Bem vindo a página de contato",
        "form": contact_form
    }  

    if contact_form.is_valid():
      print(contact_form.cleaned_data['nome_completo'])

    if request.method == "POST":
      #exibir todos os dados que chega no POST do formulário
        print(request.POST)
        #exibir dado específico que chega no POST do formulário com o .get('valor')
        print(request.POST.get('nome_completo'))
        print(request.POST.get('email'))
        print(request.POST.get('mensagem'))
    return render(request, 'contact/view.html', context)

