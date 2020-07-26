Funcionalidades:
solicitar produtos O caminhão e PDVs pode solicitar quais produtos ele precisa para completar sua carga ou estoque
disponibilizar produtos O PDV pode avisar quais produtos ele tem no estoque para disponibilizar
coletar produtos O caminhão informa ao PDV que irá coletar seus produtos
calculo de rota A API será responsável pelo cálculo de rota a fim de priorizar PDVs que já estão na rota de entrega do motorista
atribuição de pontos A API é responsável pela atribuição de pontos ao PDV que realiza compra e venda de produtos            

site
ver produtos disponibilizados para entrega
add produto/entregas
ver produtos entregues pelo entregador {dados da entrega como data, hora...}


entregador
ver entregas
ver rota de entrega
confirmar entrega


API
cadastrar vendedor com endereço
cadastrar produto para venda com vendedor
cadastrar venda {produto, data}

buscar produtos a serem entregues #por um raio de Xkm e score 
pegar produtos e add na rota do entregador

entrega rankeada por distancia e score do vendedor!!!!!!
score do vendedor = faturamento do vendedor, distancia, risco do produto

**BrejApp-api**

Uma REST-API usando Django REST Framework para atender ao serviço de entregas do app BrejApp 


Dependências
- [Python 3.7](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/basics/)
- [Docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)

Setup
- Clonar o repositório
- Criar um environment com pipenv
- Iniciar o environment
- Criar o arquivo `.env` baseando-se no `.env.template`
- Iniciar a aplicação

```
git clone git@github.com:AngeloMendes/entrega-compartilhada.git
cd entrega-compartilhada
pipenv install --dev
pipenv shell
cp .env.template .env
docker-compose up -d --build
```
Ao iniciar, já será criado o banco de dados a partir das migrations e a api, com sua documentação, pode ser acessada em: `http://localhost:8000`

- Logs: `docker-compose logs -f`
- Sair: `docker-compose down -v`

