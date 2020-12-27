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
    
