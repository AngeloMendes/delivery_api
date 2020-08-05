**Rota inteligente-api**

Uma REST-API usando Django REST Framework para atender ao serviço de entregas do Rota Inteligente 


Dependências
- [Python 3.7](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/basics/)
- [Docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)
- [Google api key](https://developers.google.com/maps/documentation/javascript/get-api-key)

Setup
- Clonar o repositório
- Criar um environment com pipenv
- Iniciar o environment
- Criar o arquivo `.env` baseando-se no `.env.template`
- Iniciar a aplicação

```
git clone git@github.com:AngeloMendes/delivery_api.git
cd delivery_api
pipenv install --dev
pipenv shell
cp .env.template .env
docker-compose up -d --build
```
Ao iniciar, já será criado o banco de dados a partir das migrations e a api, com sua documentação, pode ser acessada em: `http://localhost:8000`

- Logs: `docker-compose logs -f`
- Sair: `docker-compose down -v`

