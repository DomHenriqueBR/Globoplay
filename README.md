# Globoplay
## Atividade individual de DAW

Globoplay é o serviço de streaming da Rede Globo, contendo os seriados, filmes e novelas mais icônicas da televisão brasileira. 
Como fã de dversas obras dessa emissora (a maioria são antigas, porque pelo amor de Deus, a qualidade decaiu muito), decidi criar um sistema Django simples com o tema do serviço.
Finja que você é funcionário da emissora e está encarregado de cadastrar os vídeos (ela também possui trechos de programas, como aqueles exibidos na televisão. Bom, pelo menos na minha época tinha), relacionando-os com as categorias que a emissora criou.

## Conteúdo do repositório
- Pasta do projeto 'globoplay_site'
``` django-admin startproject globoplay_site . ```
- Pasta do aplicativo 'cadastro'
``` django-admin startapp cadastro ```
- Ambiente virtual 'venv'
``` python3 -m venv venv ```
``` venv\Scripts\activate ```
PS: o meu é Windows e o senhor disse que era esse comando

- Arquivo sqlite3 contendo o banco de dados das migrations
``` python3 manage.py makemigrations ```
``` python3 manage.py migrate ```
- Arquivo principal 'manage.py'