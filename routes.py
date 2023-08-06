from controllers.login import login_
from controllers.dashboard import dashboard_

from controllers.test import test_

from controllers.ws import socketio

def routes_list(app):
    app.register_blueprint(login_)
    app.register_blueprint(dashboard_)
    app.register_blueprint(test_)

    socketio.init_app(app)

    return app