"""
Primeiro commit

[X] Contém rotas fora do padrão, endereco e parametros, de 3 tipos
[X] Sem HATEOAS, retornos complexos (country dentro de users)
[X] Frontend totalmente misturado com o backend, acessando dados diretamente
    no front por exemplo (usuarios no index)
[X] Uma requisição que depende de outra para funcionar (validate)
[X] Não cacheável
[X] Camadas misturadas, cliente precisa passar endereço da segunda API pra acessar
    conteudo da primeira


Segundo commit, refatorar:

[ ] Revisar camadas da aplicação de forma que cliente não precise saber api
[ ] Deixar cada recurso independente (stateless)
[ ] Padronizar interface da API
[ ] HATEOAS
[ ] Separar front do backend
[ ] Como colocar cache nas rotas que fazem sentido?
"""


from flask import Flask, url_for


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from . import routes

    return app
