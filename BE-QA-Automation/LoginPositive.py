import requests
import json
def login(partnerId = 185, username = 'xympdpkyymlh1537875168491', password = 'password', udid = '881033'):
    url = 'https://rest-eus1.ott.kaltura.com/restful_v5_0/api_v3/service/ottuser/action/login'
    return requests.post(url, json={
        "partnerId" : partnerId,
        "username" : username,
        "password" : password,
        "udid" : udid
    }).json()['user']
    assert()