from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('criar-recebedor', views.criar_recebedor, name="criar_recebedor"),
    path('criar-transacao', views.criar_transacao, name="criar_transacao"),
    path('estorno', views.estorno, name="estorno"),
]
