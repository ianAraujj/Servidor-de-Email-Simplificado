# Generated by Django 3.1.4 on 2020-12-25 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do Usuario')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(blank=True, max_length=200, null=True, verbose_name='Assunto da Mensagem')),
                ('corpo', models.TextField(verbose_name='Corpo Mensagem')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data do Email')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destinatario', to='mensagem.usuario')),
                ('remetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Remetente', to='mensagem.usuario')),
                ('respostas', models.ManyToManyField(blank=True, related_name='_mensagem_respostas_+', to='mensagem.Mensagem', verbose_name='Respostas')),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
    ]
