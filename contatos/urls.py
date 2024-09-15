from . import views
from django.urls import path

urlpatterns=[
    path('adicionar/',views.adicionar_contato,name='adicionar_contato'),
    path('',views.listar_contato,name='listar_contato'),
    path('editar/<int:id>/',views.editar_contato,name='editar_contato'),
    path('excluir/<int:id>/',views.excluir_contato,name='excluir_contato'),
]