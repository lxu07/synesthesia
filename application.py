from flask import *
from data import *

application = Flask(__name__)

ATLANTA_COORDS = ['33.631674:-84.289464', '33.887419:-84.568929']


@application.route('/')
def handle_request():
    # print(request.args)
    if not request.args['datatype'] and request.args['start'] and request.args['end']:
        return '''ERROR: You must specify a datatype, start, and end time'''
    if request.args['datatype'] in {'temperature', 'humidity', 'pressure'}:
        data = {}
        datatype = ''
        sensors = get_env_sensors(ATLANTA_COORDS[0], ATLANTA_COORDS[1])
        for uid, coords in sensors:
            q = get_mean_env_data_over_interval(uid, request.args['start'], request.args['end'],
                            request.args['datatype'].upper())
            if q[1] != 'ERROR':
                data[coords] = q[0]
                datatype = q[1]
        return jsonify(
            data=data,
            datatype=datatype,
            start=request.args['start'],
            end=request.args['end']
        )
    elif request.args['datatype'] == 'pedestrian':
        data = {}
        datatype = ''
        sensors = get_ped_sensors(ATLANTA_COORDS[0], ATLANTA_COORDS[1])
        for uid, coords in sensors:
            q = get_mean_ped_data_over_interval(uid, request.args['start'], request.args['end'])
            if q[3] != 'ERROR':
                data[coords] = {'direction' : q[0], 'pedestrianCount' : q[1], 'speed' : q[2]}
                datatype = q[3]
        return jsonify(
            data=data,
            datatype=datatype,
            start=request.args['start'],
            end=request.args['end']
        )
    elif request.args['datatype'] == 'traffic':
        data = {}
        datatype = ''
        sensors = get_ped_sensors(ATLANTA_COORDS[0], ATLANTA_COORDS[1])
        for uid, coords in sensors:
            q = get_mean_ped_data_over_interval(uid, request.args['start'], request.args['end'])
            if q[3] != 'ERROR':
                data[coords] = {'direction' : q[0], 'vehicleCount' : q[1], 'speed' : q[2]}
                datatype = q[3]
        return jsonify(
            data=data,
            datatype=datatype,
            start=request.args['start'],
            end=request.args['end']
        )
    elif request.args['datatype'] == 'audio':
        data = {}
        datatype = 'float64'
        sensors = get_audio_locations(ATLANTA_COORDS[0], ATLANTA_COORDS[1])
        for uid, coords in sensors:
            q = get_max_amplitude_data(uid, request.args['start'])
            if q != 0.0:
                data[coords] = {'maxAmplitude' : q}
        return jsonify(
            data=data,
            datatype=datatype,
            start=request.args['start'],
        )

if __name__ == '__main__':
    application.run()
