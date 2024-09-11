from django.db import models

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11,unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F','Feminino'), ('O', 'Outros')])
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

class TipoExame(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

class Exame(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    observacao = models.CharField(max_length=255)
    tipo_exame = models.ForeignKey(TipoExame, on_delete=models.CASCADE)

class Consulta(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_exame = models.ForeignKey(TipoExame, on_delete=models.CASCADE)
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    protocolo = models.CharField(max_length=20, unique=True, editable=False)
