def home_route(app):
    @app.get("/")
    def home():
        return ""
