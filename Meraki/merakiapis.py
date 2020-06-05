import requests
import json

meraki_api_key = "8f90ecec4fca692f606092279f203c6020ca011c"
url = "https://api.meraki.com/api/v0/organizations"
headers = {
    "X-Cisco-Meraki-API-Key": meraki_api_key,
}

#print orgs
orgs = requests.get(url, headers=headers)
orgs = orgs.json()
print(json.dumps(orgs, indent=4))


#print first 3
url = "https://api.meraki.com/api/v0/organizations/566327653141842188/devices"
params = {
    "perPage": 3
}

res = requests.get(url, headers=headers, params=params)
formatted_message = """
Meraki Dashboard API response
-------------------------------------
Response Status Code   : {}
Response Link Header   : {}
Response Body          : {}
-------------------------------------
""".format(res.status_code, res.headers.get('Link'), json.dumps(res.json(), indent=4))
print(formatted_message)

#print next 3
second_response = requests.get(res.links['next']['url'], headers=headers)
formatted_message = """
Meraki Dashboard API response
-------------------------------------
Response Status Code   : {}
Response Link Header   : {}
Response Body          : {}
-------------------------------------
""".format(second_response.status_code, second_response.headers.get('Link'), json.dumps(second_response.json(), indent=4))
print(formatted_message)


# get networks
#url =  "https://api.meraki.com/api/v0/organizations/566327653141842188/networks"
#networks = requests.get(url, headers=headers)
#print(json.dumps(networks.json(), indent=4))

#orgs and networks
for org in orgs:
    print(org['id'])
    url = "https://api.meraki.com/api/v0/organizations/" + org['id'] + "/networks"
    networks = requests.get(url, headers=headers)
    networks = networks.json()
    #print(json.dumps(networks, indent=4))
    for network in networks:
        print("  " + network['id'])
        url = "https://api.meraki.com/api/v0/networks/" + network['id'] + "/devices"
        devices = requests.get(url, headers=headers)
        devices = devices.json()
        #print(json.dumps(devices, indent=4))
        for device in devices:
            print("        " + device['serial'])
