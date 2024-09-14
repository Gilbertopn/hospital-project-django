from django.shortcuts import render, redirect
from django.http import JsonResponse
from ..models import Consulta, Paciente, Exame, TipoExame
import uuid

def criar_consulta(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        exame_id = request.POST.get('exame')
        data_hora = request.POST.get('data_hora')

        paciente = Paciente.objects.get(id=paciente_id)
        exame = Exame.objects.get(id=exame_id)
        tipo_exame = exame.tipo_exame  

        
        if Consulta.objects.filter(exame=exame, data_hora=data_hora).exists():
            return render(request, 'consulta/criar_consulta.html', {
                'pacientes': Paciente.objects.all(),
                'exames': Exame.objects.all(),
                'error': 'Já existe uma consulta marcada para este exame neste horário.',
            })

       
        protocolo = str(uuid.uuid4())[:20]

       
        Consulta.objects.create(
            paciente=paciente,
            tipo_exame=tipo_exame,  
            exame=exame,
            data_hora=data_hora,
            protocolo=protocolo
        )

        return redirect('listar_consultas')


    pacientes = Paciente.objects.all()
    exames = Exame.objects.all()
    return render(request, 'consulta/criar_consulta.html', {'pacientes': pacientes, 'exames': exames})

def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consulta/todas_consultas.html', {'consultas': consultas})

def get_tipo_exame_por_exame(request, exame_id):
    exame = Exame.objects.get(id=exame_id)
    tipo_exame = exame.tipo_exame
    return JsonResponse({'tipo_exame': {'id': tipo_exame.id, 'nome': tipo_exame.nome}})




