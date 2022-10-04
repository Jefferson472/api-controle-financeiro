<h1 align="center">
	<p align="center">Challenge Back-End 3ª Edition</p>
	<a href="https://www.alura.com.br/challenges/back-end-3"><img src="docs\img\challenges-logo.png" alt="Alura Challenges"></a>
</h1>

<div align="center" id="badges">
    <img src="https://img.shields.io/badge/STATUS-WIP-red"/>
</div>

---

# API Controle Financeiro
## Descrição do Projeto
Projeto de API para Controle Financeiro Familiar desenvolvido durante o Challenge BackEnd Alura. O projeto foi desenvolvido utilizando Python, Django Rest Framework.

O projeto está disponível no link: https://api-alura-controle-financeiro.herokuapp.com

---

## Requirements
- Python 3.10
- Django 4.1
- Django Rest Framework 3.13

## Endpoints
### Autenticação
Autenticação para testes.
```json
    "username": "postman",
    "password": "teste123456"
```

### Receitas
Retorna uma lista de receitas cadastradas, uma única receita pelo `id` ou um filtro das receitas do mês

`api/v1/receitas`

`api/v1/receitas/<int:pk>`

`api/v1/receitas/<int:ano>/<int:mes>`

`ALLOW_METHODS = GET, POST, PUT, PATCH`
```json
{
    "descricao": "Receita Teste"
    "valor": 10,
}
```

### Despesas
Retorna uma lista de despesas cadastradas, uma única despesa pelo `id` ou um filtro das despesas do mês

`api/v1/despesas`

`api/v1/despesas/<int:pk>`

`api/v1/despesas/<int:ano>/<int:mes>`

`ALLOW_METHODS = GET, POST, PUT, PATCH`
```json
{
    "descricao": "Despesa Teste"
    "valor": 10,
    "categoria": "opcional"
}
```

### Resumo
Retorna um resumo das despesas e receitas do mês.

`api/v1/resumo/<int:ano>/<int:mes>`

`ALLOW_METHODS = GET`

---

## Executando o Projeto
Para executar o projeto forneça uma `SECRET_KEY` no arquivo `.env` e execute os comando abaixo:

`python src/api/manage.py migrate`

`python src/api/manage.py createsuperuser`

`python src/api/manage.py runserver`


## Executando os Testes
Para rodar os testes execute o comando abaixo:

`python src/api/manage.py test`
