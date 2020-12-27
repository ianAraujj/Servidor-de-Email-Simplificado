from rest_framework import serializers
from mensagem.models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields = ('id', 'nome')

class MensagemSerializer(serializers.ModelSerializer):
    remetente = UsuarioSerializer(many=False)
    destinatario = UsuarioSerializer(many=False)

    class Meta:
        model = Mensagem
        fields = ('id', 'remetente', 'destinatario', 'assunto', 'corpo', 'data', 'respostas')