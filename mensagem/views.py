# rest_framework

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.shortcuts import get_object_or_404

# Mensagem

from mensagem.serializers import UsuarioSerializer, MensagemSerializer
from mensagem.models import Usuario, Mensagem


class EnviarMensagem(APIView):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class = MensagemSerializer
    permission_class = AllowAny

    def post(self, request, format=None, **kwargs):

        id_usuario = kwargs.get("id_usuario", None)

        if id_usuario == None:
            return Response(
                data={"detalhes": "Usuario Não Informado"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if not Usuario.objects.filter(id=id_usuario).exists():
            return Response(
                data={"detalhes": "Usuario Não Encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        remetente = Usuario.objects.get(id=id_usuario)
        
        destinatario = request.data.get('destinatario', None)
        assunto = request.data.get('assunto', None)
        corpo = request.data.get('corpo', None)

        if destinatario == None or assunto == None or corpo == None:
            return Response(
                data={"detalhes": "Os seguintes campos são obrigatórios: destinatario, assunto, corpo"},
                status=status.HTTP_400_BAD_REQUEST   
            )

        if not Usuario.objects.filter(id=destinatario).exists():
            return Response(
                data={"detalhes": "Destinatario Não Encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        destinatario_usuario = Usuario.objects.get(id=destinatario)


        try:
            mensagem = Mensagem()
            mensagem.remetente = remetente
            mensagem.destinatario = destinatario_usuario
            mensagem.assunto = assunto
            mensagem.corpo = corpo
            mensagem.save()
            
            return Response(
                data={"detalhes": "Mensagem Enviada"}, 
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                data={"detalhes": "Erro no Servidor"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ListarMensagens(APIView):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class = MensagemSerializer
    permission_class = AllowAny

    def get(self, request, format=None, **kwargs):

        id_usuario = kwargs.get("id_usuario", None)

        if id_usuario == None:
            return Response(
                data={"detalhes": "Usuario Não Informado"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if not Usuario.objects.filter(id=id_usuario).exists():
            return Response(
                data={"detalhes": "Usuario Não Encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        usuario = Usuario.objects.get(id=id_usuario)

        mensagens = Mensagem.objects.filter(destinatario=usuario)
        serializer = self.serializer_class(mensagens, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

class DeletarMensagem(APIView):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class = MensagemSerializer
    permission_class = AllowAny

    def delete(self, request, format=None, **kwargs):

        id_usuario = kwargs.get("id_usuario", None)

        if id_usuario == None:
            return Response(
                data={"detalhes": "Usuario Não Informado"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if not Usuario.objects.filter(id=id_usuario).exists():
            return Response(
                data={"detalhes": "Usuario Não Encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        id_mensagem = kwargs.get("id_mensagem", None)

        if id_mensagem == None:
            return Response(
                data={"detalhes": "Mensagem Não Informada"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not Mensagem.objects.filter(id=id_mensagem).exists():
            return Response(
                data={"detalhes": "Mensagem Não Encontrada"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        usuario = Usuario.objects.get(id=id_usuario)
        mensagem = Mensagem.objects.get(id=id_mensagem)

        if mensagem.destinatario != usuario and mensagem.remetente != usuario:
            return Response(
                data={"detalhes": "Usuário Não Autorizado"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:

            mensagem.delete()

            return Response(
                data={"detalhes": "Mensagem Deletada"}, 
                status=status.HTTP_200_OK
            )

        except:
            return Response(
                data={"detalhes": "Erro no Servidor"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AbrirMensagem(APIView):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class = MensagemSerializer
    permission_class = AllowAny

    def get(self, request, format=None, **kwargs):

        id_usuario = kwargs.get("id_usuario", None)

        if id_usuario == None:
            return Response(
                data={"detalhes": "Usuario Não Informado"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if not Usuario.objects.filter(id=id_usuario).exists():
            return Response(
                data={"detalhes": "Usuario Não Encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        id_mensagem = kwargs.get("id_mensagem", None)

        if id_mensagem == None:
            return Response(
                data={"detalhes": "Mensagem Não Informada"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not Mensagem.objects.filter(id=id_mensagem).exists():
            return Response(
                data={"detalhes": "Mensagem Não Encontrada"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        usuario = Usuario.objects.get(id=id_usuario)
        mensagem = Mensagem.objects.get(id=id_mensagem)

        if mensagem.destinatario != usuario and mensagem.remetente != usuario:
            return Response(
                data={"detalhes": "Usuário Não Autorizado"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        serializer = self.serializer_class(mensagem, many=False)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )