from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nome = models.CharField(
        verbose_name="Nome do Usuario", 
        null=False, 
        blank=False, 
        max_length=200
    )

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"

class Mensagem(models.Model):
    remetente = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='Remetente',
        null=False,
        blank=False
    )
    destinatario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='Destinatario',
        null=False,
        blank=False
    ) 
    assunto = models.CharField(
        verbose_name="Assunto da Mensagem", 
        null=True, 
        blank=True, 
        max_length=200
    )
    corpo = models.TextField(
        blank=False, 
        null=False, 
        verbose_name="Corpo Mensagem")
    data = models.DateTimeField(
        verbose_name="Data do Email",
        auto_now_add=True
    )
    respostas = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name="Respostas")

    
    def __str__(self):
        return "De: " + self.remetente.nome + ", Para: " + self.destinatario.nome

    
    class Meta:
        verbose_name="Mensagem"
        verbose_name_plural="Mensagens"