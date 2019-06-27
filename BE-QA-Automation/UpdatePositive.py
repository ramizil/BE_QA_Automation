#Positive update first name and last name
import requests
import json
import jsonpath

#URL
url = "https://rest-eus1.ott.kaltura.com/restful_v5_0/api_v3/service/ottuser/action/update"

#Setting header and proxy
headers = {"content-type": "application/json"}
http_proxy  = "http://genproxy:8080"
https_proxy = "https://genproxy:8080"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }

FN="Rami"
LN="Test"
json_input = '{user: {firstName: "'+FN+'", lastName: "'+LN+'" }, id: 881033}'
request_value = json.loads(json_input)
request_json = json.dumps(request_value)
print(request_json)
response = requests.post(url, request_json, proxies=proxyDict, headers=headers)
print(response.content)

#Validate respone code
assert response.status_code == 200

#parse response to json format
response_json = json.loads(response.text)

# Pick refresh token
resultA = jsonpath.jsonpath(response_json,'result.user.firstName')
print("firstName: "+resultA[0])
resultB = jsonpath.jsonpath(response_json,'result.user.lastName')
print("lastName: "+resultB[0])


if (resultA[0] == FN) and (resultB[0] == LN):
    print("Passed")
else:
    print("Failed")

