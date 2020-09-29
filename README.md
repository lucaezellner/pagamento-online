# Pagamento Online

Repositório criado para o desenvolvimento de uma aplicação consumindo a API do Pagar.me. Com esse projeto é possível:

  - Cadastrar recebedor
  - Consultar recebedores cadastrados
  - Consultar o saldo dos recebedores
  - Realizar transação de cartão de crédito com split para dois recebedores
  - Consultar as transações realizadas
  - Estornar transação com split para dois recebedores

## Instalação

Pagamento online utiliza [Python](https://www.python.org/) v3.7.6+ para funcionar.

Instalação das dependencias necessárias

```sh
$ pip install -r > requirements.txt
```

## Variáveis de ambiente

Deve ser criado um arquivo chamado .ENV dentro do diretório pagonline-project com as seguintes variáveis de ambiente, necessárias para execução do projeto:
```sh
PAGARME_API_KEY = "sua chave de api do pagarme"
SECRET_KEY = "secret key do django"
```

## Execução do projeto

Para iniciar o servidor localmente, basta executar o comando:
```sh
$ cd pagonline-project
$ python manage.py runserver
```
Pronto! O projeto já estará rodando e disponível para testes em http://localhost:8000/.
