
### 1.Qual a diferença entre o SQLite e o PostgreSQL? Por que um precisa de usuário e senha e o outro não?
O SQLite é um servidor que fica em um espaço físico no seu computador, já o PostgreeSQL é um servidor em nuvem. Por ser um servidor, o SQLite necessita de senha.

### 2 Por que a API usa o agenda_app e não o postgres ?
Pois o posrgres é o administrador que mexe com todos os outros bancos, caso a senha vaze, afetará apenas aquele banco criado.

### 3. . Explique cada pedaço da URL
postgresql = refere-se ao tipo de banco que está sendo usado,  

usuario:senha123 = usuário e senha

localhost/2222 = porta onde o servidor está sendo utilizado

/banco = qual banco dentro das tabelas está sendo utilizado

### 4. Para que serve o driver psycopg ? Por que você não precisava dele no SQLite?
O pycopg serve para gerenciar o banco PostgreSQL, pois o sqlite é rodado localmente.

### 5. Por que o .env fica fora do GitHub e o .env.example vai? 

O .env são as credenciais do servidor, logo pode ocorrer um vazamento de dados, já o .env.example é apenas um exemplo e suas informações não causam vulnerabilidades para o banco

### 6. Quem cria as tabelas? O que acontece se o models.py não bater com elas?
O PostgreSQL que cria as tabelas, caso a models não seja semelhante a tabela, não será retornado nada.

### 7. 7. No experimento do Passo 7.3, a API deu 500 mas o contato duplicado não entrou. Quem protegeu o dado? E para que serve, então, o 409?
O "unique" do atributo protegeu a tabela da redundância desse dados. O 409 serve para tratar esse erro e não dar uma mensagem genérica para o usuário

###  8. Por que o UPDATE do PATCH mexe só em uma coluna? (Passo 7.2)
Por causa do exclude_unset = True
### 9. No 1:N entre grupos e contatos, por que a chave estrangeira fica em contatos?
Porque cada contato pertence a apenas um grupo e cada contato guarda o ID de seu grupo.