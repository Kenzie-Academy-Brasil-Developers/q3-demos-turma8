from app.controllers.dev_controller import retrieve


def dev_route(app):
    @app.get("/devs")
    def get_devs():
        return retrieve()

    @app.get("/filter-devs")
    def filter_devs():
        return ""

    # Criar rotas de inserção e deleçao
