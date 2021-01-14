import requests, json
from requests.auth import HTTPBasicAuth

apiHost = 'https://api.mashery.com'
tokenEndpoint = '/v3/token'
resourceEndpoint = '/v3/rest'
apikey = '<Insert V3 API Key>'
secret = '<Insert V3 API Secret>'
username = '<Insert Mashery Portal username>'
password = '<Insert Mashery Portal password'
areaUuid = '<Insert Mashery Area UUID>'
serviceId = '<Insert Mashery API Definition UUID>'

def authenticate(apikey, secret, username, password, areaUuid):
    payload = {'grant_type': 'password', 'username' : username, 'password'  : password, 'scope' : areaUuid}
    response = requests.post(apiHost + tokenEndpoint, auth=HTTPBasicAuth(apikey, secret), data=payload)
    return response.json()['access_token']

def callApi(token, resource, params, payload):
    headers = {"Content-type": "application/json", "Authorization": 'Bearer ' + token}
    if payload is None:
        response = requests.get(apiHost + resourceEndpoint + resource + '?' + params, headers=headers)
    else:
        response = requests.put(apiHost + resourceEndpoint + resource + '?' + params, headers=headers, data=json.dumps(payload))
    return response.json()

# authenticate (get oauth 2 token)
token = authenticate(apikey, secret, username, password, areaUuid)

# get service with specific fields of endpoints
service = callApi(token, '/services/' + serviceId, 'fields=endpoints.id,endpoints.requestAuthenticationType', None)

# update the data object, setting specific property, 'requestAuthenticationType', to a new value
for endpoint in service['endpoints']:
    endpoint['requestAuthenticationType'] = 'apiKeyAndSecret_MD5'

# put the service back with the updated data
service = callApi(token, '/services/' + serviceId, 'fields=endpoints.id,endpoints.requestAuthenticationType', service)