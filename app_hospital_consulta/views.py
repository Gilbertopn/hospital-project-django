from django.shortcuts import render, redirect
from .models import Paciente

def criar_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        Paciente.objects.create(
            nome = nome,
            cpf = cpf,
            data_nascimento = data_nascimento,
            sexo = sexo,
            telefone = telefone,
            email = email
        )

       
    return render (request, 'paciente/cadastro_paciente.html')