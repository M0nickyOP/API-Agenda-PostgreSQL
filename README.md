# API Agenda de contatos
  Uma API de agenda com CRUD e banco de dados PostgreSQL

  _____

### Instruções de instalação
``` 
sudo apt update

sudo apt install postgresql

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

fastapi dev

```
### Como rodar o banco
``` 
// instale o banco
sudo apt install postgresql
// entre no modo administrador do postgresql
sudo -u postgres psql
// crie um usuario e senha
CREATE USER exemplo_app WITH PASSWORD '12345';
CREATE DATABASE exemplo OWNER exemplo_app;

```
### Pré requisitos
psql (PostgreSQL) 16.15 

Python 3.12.3

___
## Rotas
| Método | Caminho | O que envio | Sucesso | Erros possíveis |
|---|---|---|---|---|
| POST | /contatos | nome, email, telefone  | 201 | 409 - Email já cadastrado |
| GET | /contatos | ---  | 200 | ---  |
| GET | grupos/{grupo_id} | id |200 | 404 - Grupo não encontrado
| GET | /contatos/{id} | id | 200 | 404 - Contato não encontrado|
| DELETE | /contatos/{id} | id  | 204 | 404 - Contato não encontrado |
| PATCH | /contatos/{id} | nome, contato e email | 200 | 404 - Contato não encontrado, 409 - Email já cadastrado|
----

