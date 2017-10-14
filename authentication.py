import requests
from requests.auth import *

client_id = r'hackathon'
client_secret = r'@hackathon'

uaaurl = 'https://890407d7-e617-4d70-985f-01792d693387.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token, predix_zone_id):
        self.token=token
        self.predix_zone_id=predix_zone_id

    def __call__(self, r):
        r.headers.update({'Authorization' : 'Bearer {}'.format(self.token), 'Predix-Zone-Id' : self.predix_zone_id})
        #print(r.headers)
        return r


def get_ps_auth():
    return BearerAuth(requests.get(uaaurl, params={'grant_type' : 'client_credentials'}, auth=HTTPBasicAuth(client_id, client_secret)).json()['access_token'],'SDSIM-IE-PUBLIC-SAFETY')


def get_env_auth():
    return BearerAuth(requests.get(uaaurl, params={'grant_type' : 'client_credentials'}, auth=HTTPBasicAuth(client_id, client_secret)).json()['access_token'],'SDSIM-IE-ENVIRONMENTAL')


def get_ped_auth():
    return BearerAuth(requests.get(uaaurl, params={'grant_type' : 'client_credentials'}, auth=HTTPBasicAuth(client_id, client_secret)).json()['access_token'],'SDSIM-IE-PEDESTRIAN')
