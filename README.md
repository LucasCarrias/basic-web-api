# Basic Web API :bookmark_tabs:

API construída com **Django Rest Framework** durante a disciplina de programação para Internet II

----

## Requisitos e Instalação
Você precisa do Python 3.8 :snake: ou superior instalado para executar os scripts

### Dependências
Para instalação das dependências você precisa executar o seguinte comando:
```
pipenv install
```
Para ativação do ambiente virtual:
```
pipenv shell
```

### Docker :whale:

Caso você tiver **Docker** e **docker-compose** instalado você pode executar o servidor com:
```
docker-compose up
```
O servidor ficará disponível pela porta **8000**.
> Observação: No **docker-compose.yml** o volume do servidor está configurado para utilizar os arquivos locais (bind mount).

---

## Uso da API

A API conta um endpoint que mostra todos as rotas. Ao acessar "**<server_url>/api-root/**" você vai encontrar:
```
{
    "profiles": [
        "<server_url>/profiles/",
        "<server_url>/profiles/<int:pk>",
        "<server_url>/profiles/<int:pk>/info"
    ],
    "posts": [
        "<server_url>/posts/",
        "<server_url>/posts/<int:pk>",
        "<server_url>/posts/<int:pk>/comments/",
        "<server_url>/posts/<int:post_pk>/comments/<int:pk>"
    ],
    "comments": [
        "<server_url>/comments/",
        "<server_url>/comments/<int:pk>"
    ],
    "profile-posts": [
        "<server_url>/profile-posts/",
        "<server_url>/profile-posts/<int:pk>"
    ],
    "posts-comments": [
        "<server_url>/posts-comments/",
        "<server_url>/posts-comments/<int:pk>"
    ],
    "api-root": [
        "<server_url>/api-root/",
        "<server_url>/api-root/openapi",
        "<server_url>/api-root/docs"
    ]
}
```
---
## Extras
### Alimentar o banco de dados
O servidor conta com o comando para alimetar o banco de dados. Basta executar:
```
python manager.py data_entry
```

### Testes
Para verificar se os endpoints estão de acordo com os requisitos inicias do projeto:
```
python manager.py test
```