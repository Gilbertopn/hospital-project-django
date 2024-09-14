"""
URL configuration for hospital_consulta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from app_hospital_consulta.views import views, views_exame, views_tipo_exame, views_consulta


urlpatterns = [
    path('', views.criar_paciente, name = 'home'),
    path('paciente/create', views.criar_paciente, name='cadastrar_paciente'),
    path("paciente/", views.listar_pacientes, name='listar_pacientes'),
    path("paciente/editar/<int:id>/", views.editar_paciente, name='editar_paciente'),
    path("paciente/deletar/<int:id>/", views.deletar_paciente, name='deletar_paciente'), 


    path('criar_tipo_exame/', views_tipo_exame.criar_tipo_exame, name='criar_tipo_exame'),
    path('listar_tipo_exame/', views_tipo_exame.listar_tipo_exame, name='listar_tipo_exame'),

    path('criar_exame/', views_exame.criar_exame, name='criar_exame'),
    path('listar_exame/', views_exame.listar_exame, name='listar_exame'),

  path('criar_consulta/', views_consulta.criar_consulta, name='criar_consulta'),
    path('listar_consultas/', views_consulta.listar_consultas, name='listar_consultas'),
    path('get_tipo_exame_por_exame/<int:exame_id>/', views_consulta.get_tipo_exame_por_exame, name='get_tipo_exame_por_exame'),
]
