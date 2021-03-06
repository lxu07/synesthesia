from authentication import get_ps_auth, get_env_auth, get_ped_auth, get_traffic_auth
import requests
import soundfile
import numpy
import io
from functools import reduce

mediaurl = 'https://ic-media-service.run.aws-usw02-pr.ice.predix.io/v2/mediastore'
metadataurl = 'https://ic-metadata-service.run.aws-usw02-pr.ice.predix.io/v2/metadata'
eventurl = 'https://ic-event-service.run.aws-usw02-pr.ice.predix.io/v2'

def get_audio_locations(x1y1, x2y2):
# format for inputs (bbox): 32.715675:-117.161230,32.708498:-117.151681 (gps lat/long for corners of box)
# returns list of tuples of ID and coord
    params = {
        'bbox' : ','.join([x1y1,x2y2]),
        'page' : '0',
        'size' : '200',
        'q' : 'mediaType:AUDIO'
    }
    data = [] #data format: [(ID, coords)]
    try:
        r = requests.get(metadataurl +'/assets/search', params=params, auth=get_ps_auth())
        r.raise_for_status()
        for asset in r.json()['content']:
            data.append((asset['assetUid'], asset['coordinates']))
    except ValueError as ve:
        print('Encountered error when getting audio locations for %s %s' % (x1y1, x2y2))
        print(ve)
    except KeyError as ke:
        print('Encountered error when getting audio data')
        print(ke)
    return data

def get_max_amplitude_data(assetUid, timefrom):
# get FLAC audio data in numpy data format given asset id and epoch time in ms to get data from
# returns numpy array
    params = {
        'mediaType' : 'AUDIO',
        'timestamp' : str(timefrom)
    }
    data = 0.0 # assetUid, max amplitude
    try:
        # get media asset url (step 1)
        r = requests.get(mediaurl + '/ondemand/assets/{}/media'.format(assetUid), params=params, auth=get_ps_auth())
        r.raise_for_status()
        # get polling url (step 2)
        url = r.json()['pollUrl']
        r = requests.get(url, auth=get_ps_auth())
        r.raise_for_status()
        for flac_url_data in r.json()['listOfEntries']['content']:
            url = flac_url_data['url']
            r = requests.get(url, auth=get_ps_auth(), stream=True)
            audio_data, sample_rate = soundfile.read(io.BytesIO(r.content))
            # print(audio_data)
            data = max(numpy.amax(audio_data), data)
    except ValueError as ve:
        print('Encountered error when getting audio data for UID %s from timestamp %s' % (assetUid, str(timefrom)))
        print(ve)
    except KeyError as ke:
        print('Encountered error when getting audio data for %s from time %s' % (assetUid, timefrom))
        print(ke)
    return data


def get_env_sensors(x1y1, x2y2):
# format for inputs (bbox): 32.715675:-117.161230,32.708498:-117.151681 (gps lat/long for corners of box)
# returns list of tuples of ID and coord
    params = {
        'bbox': ','.join([x1y1, x2y2]),
        'page': '0',
        'size': '200',
        'q': 'assetType:ENV_SENSOR'
    }
    data = []  # data format: [(ID, coords)]
    try:
        r = requests.get(metadataurl + '/assets/search', params=params, auth=get_env_auth())
        r.raise_for_status()
        for asset in r.json()['content']:
            data.append((asset['assetUid'], asset['coordinates']))
    except ValueError as ve:
        print('Encountered error when getting environment sensors locations for %s %s' % (x1y1, x2y2))
        print(ve)
    except KeyError as ke:
        print('Encountered error when getting ped data')
        print(ke)
    return data


def get_env_data(assetUid, starttime, endttime, value):
# get environmental data given epoch time range in which to pull data and data type (TEMPERATURE, PRESSURE, or HUMIDITY)
# returns list of tuples of (time, max, mean, median, min, unit)
    data = []
    params = {
        'eventType' : value,
        'startTime' : str(starttime),
        'endTime' : str(endttime)
    }
    try:
        r = requests.get(eventurl + '/assets/{}/events'.format(assetUid), params=params, auth=get_env_auth())
        r.raise_for_status()
        for reading in r.json()['content']:
            data.append((reading['timestamp'], reading['measures']['max'], reading['measures']['mean'],
                         reading['measures']['median'], reading['measures']['min'],
                         reading['properties']['unit']+' E '+reading['properties']['powerOf10']))
    except ValueError as ve:
        print('Encountered error when getting %s for %s from time %s to %s' % (value, assetUid, starttime, endttime))
        print(ve)
    except KeyError as ke:
        print('Encountered error when getting ped data for %s from time %s to %s' % (assetUid, starttime, endttime))
        print(ke)
    return data


def get_mean_env_data_over_interval(assetUid, starttime, endttime, value):
# gets mean environmental data over interval
# returns tuple of (value, unit)
    data = get_env_data(assetUid, starttime, endttime, value)
    if data:
        return reduce(lambda x, y: x+(y[3]/len(data)), data, 0), data[0][5] # accumulate all means divided by the number of data entries
    return 0.0, 'ERROR'


def get_ped_sensors(x1y1, x2y2):
# format for inputs (bbox): 32.715675:-117.161230,32.708498:-117.151681 (gps lat/long for corners of box)
# returns list of tuples of ID and coord
    params = {
        'bbox': ','.join([x1y1, x2y2]),
        'page': '0',
        'size': '200',
        'q': 'assetType:CAMERA'
    }
    data = []  # data format: [(ID, coords)]
    try:
        r = requests.get(metadataurl + '/assets/search', params=params, auth=get_ped_auth())
        r.raise_for_status()
        for asset in r.json()['content']:
            data.append((asset['assetUid'], asset['coordinates']))
    except ValueError as ve:
        print('Encountered error when getting camera locations for %s %s' % (x1y1, x2y2))
        print(ve)
    except KeyError as ke:
        print('Encountered error when getting ped data')
        print(ke)
    return data


def get_ped_data(assetUid, starttime, endttime):
# get pedestrian data given epoch time range
# returns list of tuples of (time, direction, count, speed, unit)
    data = []
    params = {
        'eventType' : 'PEDEVT',
        'startTime' : str(starttime),
        'endTime' : str(endttime)
    }
    try:
        r = requests.get(eventurl + '/assets/{}/events'.format(assetUid), params=params, auth=get_ped_auth())
        r.raise_for_status()
        # print(assetUid)
        # print(r.json())
        for reading in r.json()['content']:
            data.append((reading['timestamp'], reading['measures']['direction'], reading['measures']['pedestrianCount'],
                         reading['measures']['speed'],
                         reading['properties']['speedUnit']))
    except ValueError as ve:
        print('Encountered error when getting ped data for %s from time %s to %s' % (assetUid, starttime, endttime))
        print(ve)
    except KeyError as ke:
        print('Encountered error when getting ped data for %s from time %s to %s' % (assetUid, starttime, endttime))
        print(ke)
    return data


def get_mean_ped_data_over_interval(assetUid, starttime, endttime):
# gets mean environmental data over interval
# returns tuple of (avg direction, avg count, avg speed, unit)
    data = get_ped_data(assetUid, starttime, endttime)
    if data:
        return reduce(lambda x, y: x + (float(y[1]) if y[1] != 'NaN' else x) / len(data), data, 0), \
               reduce(lambda x, y: x + (float(y[2]) if y[2] != 'NaN' else x) / len(data), data, 0), \
               reduce(lambda x, y: x + (float(y[3]) if y[3] != 'NaN' else x) / len(data), data, 0), \
               data[0][4] # accumulate all means divided by the number of data entries
    return 0.0,0.0,0.0,'ERROR'


def get_traffic_sensors(x1y1, x2y2):
# format for inputs (bbox): 32.715675:-117.161230,32.708498:-117.151681 (gps lat/long for corners of box)
# returns list of tuples of ID and coord
    params = {
        'bbox': ','.join([x1y1, x2y2]),
        'page': '0',
        'size': '200',
        'q': 'assetType:CAMERA'
    }
    data = []  # data format: [(ID, coords)]
    try:
        r = requests.get(metadataurl + '/assets/search', params=params, auth=get_traffic_auth())
        r.raise_for_status()
        for asset in r.json()['content']:
            data.append((asset['assetUid'], asset['coordinates']))
    except ValueError as ve:
        print('Encountered error when getting camera locations for %s %s' % (x1y1, x2y2))
        print(ve)
    except KeyError as ke:
        print('Encountered error when getting traffic data')
        print(ke)
    return data


def get_traffic_data(assetUid, starttime, endttime):
# get pedestrian data given epoch time range
# returns list of tuples of (time, direction, count, speed, vehicleType, unit)
    data = []
    params = {
        'eventType' : 'TFEVT',
        'startTime' : str(starttime),
        'endTime' : str(endttime)
    }
    try:
        r = requests.get(eventurl + '/assets/{}/events'.format(assetUid), params=params, auth=get_traffic_auth())
        r.raise_for_status()
        for reading in r.json()['content']:
            data.append((reading['timestamp'], reading['measures']['direction'], reading['measures']['vehicleCount'],
                         reading['measures']['speed'], reading['properties']['vehicleType'],
                         reading['properties']['speedUnit']))
    except ValueError as ve:
        print('Encountered error when getting traffic data for %s from time %s to %s' % (assetUid, starttime, endttime))
        print(ve)
    except KeyError as ke:
        print('Encountered error when getting traffic data for %s from time %s to %s' % (assetUid, starttime, endttime))
        print(ke)
    return data


def get_mean_traffic_data_over_interval(assetUid, starttime, endttime):
# gets mean environmental data over interval
# returns tuple of (avg direction, avg count, avg speed, unit)
    data = get_traffic_data(assetUid, starttime, endttime)
    if data:
        return reduce(lambda x, y: x + (float(y[1]) if y[1] != 'NaN' else x) / len(data), data, 0), \
               reduce(lambda x, y: x + (float(y[2]) if y[2] != 'NaN' else x) / len(data), data, 0), \
               reduce(lambda x, y: x + (float(y[3]) if y[3] != 'NaN' else x) / len(data), data, 0), \
               data[0][5] # accumulate all means divided by the number of data entries
    return 0.0, 0.0, 0.0, 'ERROR'

'''
print('AUDIO')
for uid, coords in get_audio_locations('33.754226:-84.396138', '33.746551:-84.384996'):
   print(get_max_amplitude_data(uid, 1507606046000))

print('ENV')
for uid, coords in get_env_sensors('33.754226:-84.396138', '33.746551:-84.384996'):
   print(get_mean_env_data_over_interval(uid, 1507606046000, 1507969145000, 'TEMPERATURE'))


print('PED')
for uid, coords in get_ped_sensors('33.754226:-84.396138', '33.746551:-84.384996'):
   print(get_mean_ped_data_over_interval(uid, 1507606046000, 1507969145000))

print('TRAFFIC')

for uid, coords in get_traffic_sensors('33.754226:-84.396138', '33.746551:-84.384996'):
    print(get_mean_traffic_data_over_interval(uid, 1507606046000, 1507969145000))

'''