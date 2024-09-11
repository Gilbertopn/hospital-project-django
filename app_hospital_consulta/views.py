from django.shortcuts import render, redirect, get_object_or_404
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

        return redirect('listar_pacientes')
    
    return render (request, 'paciente/cadastro_paciente.html')

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render (request, 'paciente/todos_pacientes.html', {'pacientes':pacientes})

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    
    if request.method == 'POST':
        paciente.nome = request.POST.get('nome')
        paciente.cpf = request.POST.get('cpf')
        paciente.data_nascimento = request.POST.get('data_nascimento')
        paciente.sexo = request.POST.get('sexo')
        paciente.telefone = request.POST.get('telefone')
        paciente.email = request.POST.get('email')

        return redirect('listar_pacientes')
    
    return render(request, 'paciente/editar_paciente.html', {'paciente':paciente})

def deletar_paciente(request, id):
    paciente = get_object_or_404(Paciente,id=id)
    paciente.delete()
    return redirect('listar_pacientes')