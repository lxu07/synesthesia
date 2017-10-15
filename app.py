from flask import *
from data import *

application = Flask(__name__)

ATLANTA_COORDS = ['33.631674:-84.289464', '33.887419:-84.568929']

@application.route('/')
def handle_request():
    # print(request.args)
    if request.args['datatype'] == 'test':
        d = [{'a': 'b'}, {'c': 'd'}]
        return jsonify(test=d)
    if not request.args['datatype'] and request.args['start'] and request.args['end']:
        return '''ERROR: You must specify a datatype, start, and end time'''
    if request.args['datatype'] in {'temperature', 'humidity', 'pressure'}:
        data = []
        datatype = ''
        sensors = get_env_sensors(ATLANTA_COORDS[0], ATLANTA_COORDS[1])
        for uid, coords in sensors:
            q = get_mean_env_data_over_interval(uid, request.args['start'], request.args['end'],
                            request.args['datatype'].upper())
            if q[1] != 'ERROR':
                data.append({'lat': coords.split(':')[0], 'long': coords.split(':')[1], 'value': q[0]})
                datatype = q[1]
        return jsonify(
            data=data,
            datatype=datatype,
            start=request.args['start'],
            end=request.args['end'],
            max=get_max_value(data),
            min=get_min_value(data)
        )
    elif request.args['datatype'] == 'pedestrian':
        data = []
        # datatype = ''
        sensors = get_ped_sensors(ATLANTA_COORDS[0], ATLANTA_COORDS[1])
        for uid, coords in sensors:
            q = get_mean_ped_data_over_interval(uid, request.args['start'], request.args['end'])
            if q[3] != 'ERROR':
                data.append({'lat': coords.split(':')[0], 'long': coords.split(':')[1], 'value': q[1]})
                # {'direction' : q[0], 'pedestrianCount' : q[1], 'speed' : q[2]}
                # datatype = q[3]
        return jsonify(
            data=data,
            datatype='PEDESTRIANS',
            start=request.args['start'],
            end=request.args['end'],
            max=get_max_value(data),
            min=get_min_value(data)
        )
    elif request.args['datatype'] == 'traffic':
        data = []
        # datatype = ''
        sensors = get_ped_sensors(ATLANTA_COORDS[0], ATLANTA_COORDS[1])
        for uid, coords in sensors:
            q = get_mean_ped_data_over_interval(uid, request.args['start'], request.args['end'])
            if q[3] != 'ERROR':
                data.append({'lat': coords.split(':')[0], 'long': coords.split(':')[1], 'value': q[1]})
                # {'direction' : q[0], 'vehicleCount' : q[1], 'speed' : q[2]}
                # datatype = q[3]
        return jsonify(
            data=data,
            datatype='VEHICLES',
            start=request.args['start'],
            end=request.args['end'],
            max=get_max_value(data),
            min=get_min_value(data)
        )
    elif request.args['datatype'] == 'audio':
        data = []
        # datatype = 'float64'
        sensors = get_audio_locations(ATLANTA_COORDS[0], ATLANTA_COORDS[1])
        for uid, coords in sensors:
            q = get_max_amplitude_data(uid, request.args['start'])
            if q != 0.0:
                data.append({'lat': coords.split(':')[0], 'long': coords.split(':')[1], 'value': q})
                # {'maxAmplitude' : q}
        return jsonify(
            data=data,
            datatype='AMPLITUDE',
            start=request.args['start'],
            max=get_max_value(data),
            min=get_min_value(data)
        )


def get_max_value(ld):
    return max([d['value'] for d in ld])


def get_min_value(ld):
    return min([d['value'] for d in ld])


if __name__ == '__main__':
    application.run()
