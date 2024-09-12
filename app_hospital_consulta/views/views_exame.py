# views.py
from django.shortcuts import render, redirect
from ..models import Exame, TipoExame

def criar_exame(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        observacao = request.POST.get('observacao')
        tipo_exame_id = request.POST.get('tipo_exame')

        if nome and observacao and tipo_exame_id:
            tipo_exame = TipoExame.objects.get(id=tipo_exame_id)
            Exame.objects.create(nome=nome, observacao=observacao, tipo_exame=tipo_exame)
            return redirect('listar_exame')
        else:
            tipos_exame = TipoExame.objects.all()
            return render(request, 'exame/criar_exame.html', {'tipos_exame': tipos_exame, 'error': 'Preencha todos os campos'})
    
    tipos_exame = TipoExame.objects.all()
    return render(request, 'exame/criar_exame.html', {'tipos_exame': tipos_exame})

def listar_exame(request):
    exames = Exame.objects.all()
    return render(request, 'exame/todos_exame.html', {'exames': exames})
