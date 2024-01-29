from flask import Flask, render_template

class Backend:
    def __init__(self, name, config, *blueprints):
        self.__app = Flask(name)
        self.__app.config.from_object(config)
        self.register_error_handlers()
        self.register_blueprints(*blueprints)

    def register_error_handlers(self):
        @self.__app.errorhandler(404)
        def page_not_found(error):
            return render_template("error404.html"), 404

    def register_blueprints(self, *blueprints):
        for blueprint in blueprints:
            self.__app.register_blueprint(blueprint)

    def run(self, *args, **kwargs):
        self.__app.run(*args, **kwargs)
