from controllers.extensions import socketio
from flask_socketio import emit
from flask import session

from service.check import get_cpu_usage


@socketio.on('request_data')
def get_data():
    data = {
        'systemname': 'cpu',
        'cpu_share': get_cpu_usage(),
        'cpu_tem': 68
    }

    session_id = session.get('session_id')

    emit('data_response', data, room=session_id)