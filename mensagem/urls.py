from django.urls import path
from mensagem.views import *

urlpatterns = [

    path('usuario/entrar',
        RegistarUsuario.as_view(),
        name='entrar'
    ),
    path('usuario/<str:usuario>/mensagem/enviar', 
        EnviarMensagem.as_view(), 
        name="enviar-mensagem"
    ),
    path('usuario/<str:usuario>/mensagem/listar', 
        ListarMensagens.as_view(), 
        name='listar-mensagens'
    ),
    path('usuario/<str:usuario>/mensagem/<str:id_mensagem>/apagar',
        DeletarMensagem.as_view(),
        name='deletar-mensagem'
    ),
    path('usuario/<str:usuario>/mensagem/<str:id_mensagem>/abrir',
        AbrirMensagem.as_view(),
        name='abrir-mensagem'
    ),
    path('usuario/<str:usuario>/mensagem/<str:id_mensagem>/encaminhar',
        EncaminharMensagem.as_view(),
        name='encaminhar-mensagem'
    ),
    path('usuario/<str:usuario>/mensagem/<str:id_mensagem>/responder',
        ResponderMensagem.as_view(),
        name='responder-mensagem'
    )
]