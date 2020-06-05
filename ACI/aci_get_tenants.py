import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

APIC_URL = "https://devasc-aci-1.cisco.com/"

def apic_login():
    """Log in to APIC"""

    token = ""
    err = ""

    try:
        response = requests.post(
            url=APIC_URL + "/api/aaaLogin.json",
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps(
                {
                    "aaaUser": {
                        "attributes": {
                            "name": "devnetuser",
                            "pwd": "CardBoardGreen12!"
                        }
                    }
                }
            ),
            verify=False
        )

        json_response = json.loads(response.content)
        token = json_response['imdata'][0]['aaaLogin']['attributes']['token']
        print(token)

        print('Response HTTTP Status Code: {status_code}'.format(status_code=response.status_code))

    except requests.exceptions.RequestException as err:
        print("HTTP Request failed")
        print(err)

    return token

# get tenants
def apic_query(token, api_url):
    """APIC Query"""


    url = APIC_URL + api_url
    print('GET request resource: ', url)

    try:
        response = requests.get(
            url,
            headers={
                "Cookie": "APIC-cookie=" + token,
                "Content-Type": "application/json; charset=utf-8"
            },
            verify=False
        )

        print('Response HTTP Status Code: {status_code}'.format(status_code = response.status_code))
        print('Response HTTP Resposne Body:', json.dumps(response.json(), indent=4))

    except requests.exceptions.RequestException:
        print("HTTP Request failed")

#Supress disable_warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

token = apic_login()

# get tenants
print("======================GET TENANTS========================")
api_url = "/api/node/class/fvTenant.json"
apic_query(token, api_url)

# get devices
print("======================GET DEVICES========================")
api_url = "/api/node/class/topology/pod-1/topSystem.json"
apic_query(token, api_url)
