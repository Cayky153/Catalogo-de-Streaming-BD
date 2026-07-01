# Catálogo de Streaming

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)


## Introdução

| Projeto | Criado em | Status |
|---|---|---|
| Trabalho Final - Catálogo de Streaming | June 27, 2026 12:00 PM | Done |



## Contextualização

Este projeto foi desenvolvido com o objetivo de praticar conceitos de modelagem de banco de dados relacional, escrita de comandos SQL e estudo de Python e Django. A proposta simula o backend de uma plataforma de streaming, contemplando o cadastro de usuários, clientes, planos de assinatura, catálogos e filmes, além dos relacionamentos entre essas entidades.

Ao longo do desenvolvimento, o foco esteve em consolidar o entendimento sobre modelagem de dados (chaves primárias, estrangeiras e relacionamentos), a construção de queries SQL diretamente via `cursor` do Django, e a criação de uma API REST utilizando o Django REST Framework.


## Tecnologias

- Python
- Django
- SQL / PostgreSQL



## Equipe

| Nome |
|---|
| Pedro Rafael |
| John Lennon |
| Antônio Pedro |
| Tiago Viana |
| Sabryna Lopes |



## Estrutura de arquivos

```
streaming/
├── apps/
│   ├── catalogo/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── filmes/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── usuarios/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   └── __init__.py
│
├── env/
│
├── streaming/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   └── urls.py
│
├── .gitignore
├── manage.py
└── requirements.txt
```



## Estrutura do Banco de Dados

– **usuario** (id [PK], senha, nome, ddd, numero)

– **catalogo** (id [PK], quantidade_de_filmes, data_entrada, data_saida)

– **genero** (id [PK], tipo, descricao, catalogo_id [FK])
• catalogo_id é uma chave estrangeira para a chave primária id de catalogo

– **planos** (id [PK], nome, duracao, preco, numero_de_telas, qualidade, anuncios)

– **filmes** (id [PK], sinopse, duracao, titulo, ano_de_lancamento, equipe, genero_id [FK], catalogo_id [FK])
• genero_id é uma chave estrangeira para a chave primária id de genero
• catalogo_id é uma chave estrangeira para a chave primária id de catalogo

– **cliente** (id_usuario [PK, FK], forma_de_pagamento, planos_id [FK])
• id_usuario é uma chave estrangeira para a chave primária id de usuario
• planos_id é uma chave estrangeira para a chave primária id de planos

– **cliente_filme** (cliente_id [PK, FK], filme_id [PK, FK], historico)
• cliente_id é uma chave estrangeira para a chave primária id_usuario de cliente
• filme_id é uma chave estrangeira para a chave primária id de filmes

– **admin** (id [PK], id_usuario [PK, FK])
• id_usuario é uma chave estrangeira para a chave primária id de usuario




## Como rodar

**1. Clone o repositório**
```bash
git clone <url-do-repositorio>
cd streaming
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv env
```
- Windows:
```bash
env\Scripts\activate
```
- Linux/macOS:
```bash
source env/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure o banco de dados**

Ajuste as credenciais de conexão com o banco de dados no arquivo `streaming/settings.py`.

*

**5. Inicie o servidor**
```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

# Manual de API — Streaming

Documentação das rotas disponíveis no projeto, organizadas por app.

---

## Catálogo — `/api/catalogo/`

### `GET /api/catalogo/`
Lista todos os catálogos.

**Retorno:** lista de objetos com todas as colunas da tabela `catalogo`.



### `POST /api/catalogo/planos/`
Cria um novo plano.

**Request body:**
```json
{
    "nome": "Premium",
    "duracao": "12",
    "preco": 39.90,
    "numero_de_telas": 4,
    "qualidade": "Ultra HD",
    "anuncios": 4
}
```

**Response `201`:**
```json
{
    "mensagem": "Plano inserido com sucesso!",
    "id": 1,
    "nome": "Premium",
    "duracao": "12",
    "preco": 39.90,
    "numero_de_telas": 4,
    "qualidade": "Ultra HD",
    "anuncios": 4
}
```

**Response `400`** (campos inválidos ou faltando): retorna os erros de validação do serializer.



## Filmes — `/api/filmes/`

### `GET /api/filmes/`
Lista todos os filmes.

**Retorno:** lista de objetos com `id`, `titulo`, `ano_de_lancamento`, `genero_id`.


### `GET /api/filmes/<id>/`
Busca um filme específico pelo `id`.

**Response `200`:**
```json
{
    "id": 1,
    "sinopse": "Um grupo de heróis enfrenta uma ameaça global.",
    "duracao": "120 min",
    "titulo": "Exemplo de Filme",
    "ano_de_lancamento": 2024,
    "equipe": "Diretor X, Produtor Y",
    "genero_id": 1,
    "catalogo_id": 1
}
```

**Response `404`** (não encontrado):
```json
{
    "erro": "Filme não encontrado"
}
```

**Response `400`** (sem `id` na rota):
```json
{
    "erro": "ID obrigatório"
}
```

---

### `POST /api/filmes/`
Cria um novo filme.

**Request body:**
```json
{
    "sinopse": "Um grupo de heróis enfrenta uma ameaça global.",
    "duracao": "120 min",
    "titulo": "Exemplo de Filme",
    "ano_de_lancamento": 2024,
    "equipe": "Diretor X, Produtor Y",
    "genero": 1,
    "catalogo": 1
}
```
> `genero` e `catalogo` são os `id`s dos registros já existentes nas respectivas tabelas.

**Response `201`:**
```json
{
    "mensagem": "Filme inserido com sucesso",
    "id": 1,
    "titulo": "Exemplo de Filme",
    "sinopse": "Um grupo de heróis enfrenta uma ameaça global.",
    "duracao": "120 min",
    "ano_de_lancamento": 2024,
    "equipe": "Diretor X, Produtor Y",
    "genero": 1,
    "catalogo": 1
}
```

**Response `400`** (campos inválidos ou faltando): retorna os erros de validação do serializer.


### `DELETE /api/filmes/<id>/`
Remove um filme pelo `id`.

**Response `204`:** sem corpo.



### `GET /api/filmes/generos/`
Lista todos os gêneros.

**Retorno:** lista de objetos com `id`, `tipo`, `descricao`, `catalogo_id`.



## Usuários — `/api/usuarios/`



### `GET /api/usuarios/<id>/`
Busca um usuário específico pelo `id`.

**Response `200`:**
```json
{
    "id": 1,
    "nome": "João da Silva",
    "ddd": 85,
    "numero": 999999999
}
```

**Response `404`** (não encontrado):
```json
{
    "erro": "Usuário não encontrado"
}
```

---

### `POST /api/usuarios/`
Cria um novo usuário.

**Request body:**
```json
{
    "nome": "João da Silva",
    "senha": "senha123",
    "ddd": "85",
    "numero": "999999999"
}
```

**Response `201`:**
```json
{
    "mensagem": "Usuario inserido com sucesso",
    "id": 1,
    "nome": "João da Silva",
    "senha": "senha123",
    "ddd": "85",
    "numero": "999999999"
}
```

**Response `400`** (campos inválidos ou faltando): retorna os erros de validação do serializer.

---

### `PUT /api/usuarios/<id>/`
Atualiza um usuário existente pelo `id`. Espera **todos** os campos (não é atualização parcial).

**Request body:**
```json
{
    "nome": "João da Silva",
    "senha": "novaSenha123",
    "ddd": "85",
    "numero": "988888888"
}
```

**Response `200`:**
```json
{
    "mensagem": "Usuario atualizado com sucesso"
}
```

**Response `400`** (campos inválidos ou faltando): retorna os erros de validação do serializer.


### `DELETE /api/usuarios/<id>/`
Remove um usuário pelo `id`.

**Response `204`:**
```json
{
    "mensagem": "Usuário removido com sucesso"
}
```


## Clientes — `/api/usuarios/clientes/`

> Um "cliente" representa a assinatura de um usuário (vínculo entre `usuario` e `planos`). A chave usada é o `id_usuario`, não um id próprio de cliente.

### `GET /api/usuarios/clientes/<id_usuario>/`
Busca os dados da assinatura de um usuário pelo `id_usuario`.

**Response `200`:**
```json
{
    "id_usuario": 1,
    "nome": "Premium",
    "duracao": "12",
    "preco": 39.90,
    "numero_de_telas": 4,
    "qualidade": "Ultra HD",
    "anuncios": 4
}
```

**Response `404`** (não encontrado):
```json
{
    "erro": "Assinatura não encontrada"
}
```

**Response `400`** (sem `id_usuario` na rota):
```json
{
    "erro": "ID obrigatório"
}
```


### `POST /api/usuarios/clientes/`
Cria um cliente, vinculando um usuário existente a um plano.

**Request body:**
```json
{
    "id_usuario": 1,
    "forma_de_pagamento": "cartao_credito",
    "planos": 1
}
```
> `id_usuario` e `planos` são os `id`s de registros já existentes nas respectivas tabelas.

**Response `201`:**
```json
{
    "Mensagem": "Cliente criado com sucesso",
    "id_usuario": 1,
    "forma_de_pagamento": "cartao_credito",
    "planos_id": 1
}
```

**Response `400`** (campos inválidos ou faltando): retorna os erros de validação do serializer.



### `PUT /api/usuarios/clientes/<id_usuario>/`
Atualiza o plano de um cliente existente, identificado pelo `id_usuario`.

**Request body:**
```json
{
    "planos": 2
}
```

**Response `200`:**
```json
{
    "mensagem": "Plano de usuário atualizado"
}
```

**Response `400`** (campos inválidos ou faltando): retorna os erros de validação do serializer.



## Notas gerais

- Todas as rotas de escrita (`POST`/`PUT`) validam o corpo da requisição via serializer do DRF antes de tocar no banco. Se a validação falhar, a resposta é sempre `400` com os erros específicos do campo.
- Os campos que representam relações (`genero`, `catalogo`, `planos`, `id_usuario`) esperam o **id** do registro relacionado, não um objeto completo.

