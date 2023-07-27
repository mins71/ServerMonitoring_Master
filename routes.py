from controllers.login import login_
from controllers.dashboard import dashboard_


def routes_list(app):
    app.register_blueprint(login_)
    app.register_blueprint(dashboard_)
    return app