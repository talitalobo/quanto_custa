from django.urls import path,include
from . import views
app_name='esclarecimento'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/adicionar_mensagem',views.adicionar_mensagem,name='add_chat'),
    path('<int:id>/identificar_obra',views.identificar_obra,name='id_obra'),
]
