from controllers.login import login_
from controllers.dashboard import dashboard_
from controllers.pcstatue import pcstatue_
from controllers.managment import managment_

from controllers.test import test_

from controllers.ws import socketio

def routes_list(app):
    app.register_blueprint(login_)
    app.register_blueprint(dashboard_)
    app.register_blueprint(test_)
    app.register_blueprint(pcstatue_)
    app.register_blueprint(managment_)

    socketio.init_app(app)

    return app