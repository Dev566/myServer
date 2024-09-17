import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from .service import healthCheckService
    app.register_blueprint(healthCheckService.bp)
    from .service import downloadPageService
    app.register_blueprint(downloadPageService.bp)
    
    # if __name__ == "__main__":
    #     app.run(port=8000, debug=True)

    return app

if __name__ == "__main__":
    app = create_app(None)
    app.run(debug=True)