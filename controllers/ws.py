from controllers.extensions import socketio
from flask_socketio import emit
from flask import session, request

from service.check import get_cpu_usage
from service.cell_data import pcdata
from models.issue import Issue

issue_event = Issue()


@socketio.on('request_data')
def get_data():
    data = {
        'cpu_event_number': issue_event.cpu_event(),
        'mem_event_number': issue_event.mem_event(),
        'storage_event_number': issue_event.disk_event(),
        'network_event_number': issue_event.net_event()
    }

    session_id = session.get('session_id')

    emit('data_response', data, room=session_id)
    

@socketio.on('tart_pc')
def get_pc_data(data):
    url = data.get("url")
    split_list = url.split("/")
    pcname = split_list[-1]
    data = {
        "cpu": pcdata(pcname).get("cpu")[0][1] + '%',
        "mem": pcdata(pcname).get("mem")[0][4] + '%',
        "str": pcdata(pcname).get("disk")[0][4] + '%',
        "net": [12,45,68,9,12,56],
        "err": "5",
        # "pcp": ["-60","-55","-50","-45","-40", "-35", "-30", "-25", "-20", "-15", "-10", "-5", "0"],
        "pcp": pcdata(pcname).get("time_s"),
        "cpu_p":pcdata(pcname).get("cpu_list"),
    }
    
    session_id = session.get('session_id')
    
    emit("data_response", data, room=session_id)