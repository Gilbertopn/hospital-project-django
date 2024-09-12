# views.py
from django.shortcuts import render, redirect
from ..models import TipoExame

def criar_tipo_exame(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        
        if nome and descricao:
            TipoExame.objects.create(nome=nome, descricao=descricao)
            return redirect('listar_tipo_exame')
        else:
            return render(request, 'tipo_exame/criar_tipo_exame.html', {'error': 'Preencha todos os campos'})
    
    return render(request, 'tipo_exame/criar_tipo_exame.html')

def listar_tipo_exame(request):
    tipo_exame = TipoExame.objects.all()
    return render(request, 'tipo_exame/todos_tipo_exame.html', {'tipo_exame': tipo_exame})
