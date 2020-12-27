# Servidor-de-Email-Simplificado
Servidor de Email Simplificado no Modelo REST. Esta aplicação foi desenvolvida utilizando DJANGO.

## Endereço Eletrônico:
  
  * https://servidor-email.herokuapp.com/api/
  
## Endereço Eletrônico para Administração

  * https://servidor-email.herokuapp.com/admin
 
        user: admin

        senha: admin

## Cliente:

  1. Endereço Para Testar ONLINE: https://repl.it/@IanLucas/Cliente
  
  2. Repositório: https://github.com/ianAraujj/Cliente-Python-da-Aplica-o-de-E-mail-Simplificado

## Instruções Para Testar o Servidor Localmente:

   - Tutorial Ótimo Aqui: https://tutorial.djangogirls.org/pt/django_installation/

  1. Requisitos: 
 
    * Python3 Instalado na sua Máquina
    
  2. Criar um ambiente virtual, para isso digite o comando abaixo no seu terminal: 
  
    * python3 -m venv myvenv
   
  Após isso, será criada na pasta atual um diretório com o nome ```myvenv```
   
  3. Entrar/Ativar o ambiente virtual:
   
    * No Windows: myvenv\Scripts\activate 
    
    * No LINUX: source myvenv/bin/activate 
 
   
  4. Instalar as Dependências do projeto, para isso, será usado o instalador de pacotes do python chamado ```pip```
  
    * Comando: pip install -r requirements.txt OU pip3 install -r requirements.txt
  
  Com isso, todos os pacotes necessários para a execução deste projeto serão instalados.
  
  5. Com o Ambiente Virtual Ativado e com as dependências do projeto instalada, para executar o projeto, digite no terminal:
  
    python3 manage.py runserver
    
  O servidor irá rodar no endereço local: 127.0.0.1 e na porta 8000:

## Instruções Para Testar o Cliente Localmente:

OBSERVACAO: 
    Para Testes ONLINE: https://repl.it/@IanLucas/Cliente

  1. Por motivos organizacionais, o código do cliente da aplicação está em um repositório separado. Então o primeiro passo é clonar o seguinte repositório com endereço: https://github.com/ianAraujj/Cliente-Python-da-Aplica-o-de-E-mail-Simplificado
  
  2. Criar um ambiente virtual, ativar o ambiente virtual e instalar as dependências igual aos passos 2, 3 e 4 do item anterior
  
  3. Para executar, digite no terminal:
  
    *    python3 cliente.py

  4. Na linha 05 do código do cliente, a variável ```url_base``` indica que o cliente está configurado para se comunicar com o servidor através do endereço "https://servidor-email.herokuapp.com/", o projeto do servidor foi hospedado na plataforma HEROKU.

Caso queira testar o cliente com um servidor local, altere o valor desta variável para: "http://127.0.0.1:8000/"

## Análise do Código:
  
  * As rotas foram implementadas neste arquivo:

          https://github.com/ianAraujj/Servidor-de-Email-Simplificado/blob/main/mensagem/views.py

## Rotas Criadas

1. Entrar No Sistema

      * path('api/usuario/entrar')
      
      * POST
      
      * Rota utlizada para o Usuário entrar no Sistema. O Usuário deve informar apenas seu nome no programa do Cliente. Se o Usuário já tiver Cadastrado, então o Sistema realiza o LOGIN, mas se o Usuário for novo, o Sistema irá cadastrar esse novo Usuário.

2. Enviar Mensagem

      * path('api/usuario/<str:usuario>/mensagem/enviar')
      
      * POST

3. Listar Todas as Mensagens

      * path('api/usuario/<str:usuario>/mensagem/listar')
      
      * GET

4. Deletar Uma Mensagem

      * path('api/usuario/<str:usuario>/mensagem/<str:id_mensagem>/apagar')
      
      * DELETE
      
5. Abrir Mensagem:

      * path('api/usuario/<str:usuario>/mensagem/<str:id_mensagem>/abrir')
      
      * GET
      
6. Encaminhar uma Mensagem pra Alguém

      * path('api/usuario/<str:usuario>/mensagem/<str:id_mensagem>/encaminhar')
      
      * POST
      
7. Responder uma Mensagem

      * path('api/usuario/<str:usuario>/mensagem/<str:id_mensagem>/responder')
      
      * POST
     
    
