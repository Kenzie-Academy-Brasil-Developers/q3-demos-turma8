# from app.controllers.dev_controller import get_devs, create_dev

from app.controllers import dev_controller


def dev_route(app):
    @app.get("/devs")
    def retrieve():
        return dev_controller.get_devs()

    @app.get("/filter-devs")
    def filter_devs():
        return dev_controller.get_by_gmail()

    @app.post("/devs")
    def create():
        return dev_controller.create_dev()

    @app.delete("/devs/<dev_id>")
    def delete(dev_id):
        return dev_controller.remove_dev(dev_id)

    @app.patch("/devs/<dev_id>")
    def update(dev_id):
        return dev_controller.update_dev(dev_id)
