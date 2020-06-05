from dna_center_authenticate import *

# get network device API wrapper
def get_network_device(dnacip, headers, params, modifier):
    # Get NEtowrk Device URI
    uri = "https://" + dnacip + "/dna/intent/api/v1/network-device" + modifier
    try:
        if params == "":
            print("\n---\nGET %s" %(uri))
        else:
            print("\n---\nGET %s?%s" %(uri, params))

        resp = requests.get(uri, headers=headers, params=params, verify=False)
        return resp
    except:
        # token fail
        print("Status: %s" %r.status_code)
        print("Respond: %s" %r.text)
        sys.exit()

# get auth token
token = get_X_auth_token(dnacip, username, password)
print("returned Authentication Token: ", (token))

# assign token to headers
headers = {"x-auth-token": token}

# get count of devices
params = ""
modifier = "/count"
resp = get_network_device(dnacip, headers, params, modifier)
print("All devices count: ", json.dumps(resp.json()["response"], indent=4))

# full device information
params = ""
modifier = ""
resp = get_network_device(dnacip, headers, params, modifier)
print(json.dumps(resp.json()["response"], indent=4))

# filter Cat 9300 devices
params = "series=Cisco Catalyst 9300 Series Switches"
modifier = "/count"
resp = get_network_device(dnacip, headers, params, modifier)

switch_count = int(json.dumps(resp.json()["response"]))
print("Catalyst 9300 Switch count: ", switch_count)

# request list of 9300 series
modifier = ""
resp = get_network_device(dnacip, headers, params, modifier)
print("Catalyst 9300 Switch list: ", json.dumps(resp.json()["response"], indent=4))

# print specific informatio
json_resp = resp.json()["response"]

for i in range(0, switch_count):
    print("Switch %d:  Type: %s.  Serial Number: %s.  DeviceId: %s. Mgmt IPv4: %s"
      %(i, json_resp[i]['type'], json_resp[i]['serialNumber'], json_resp[i]['id'],
        json_resp[i]['managementIpAddress']))

# find vlans
params = ""

for i in range(0, switch_count):
    modifier = "/" + json_resp[i]['id'] + "/vlan"
    resp = get_network_device(dnacip, headers, params, modifier)
    print("Device Serial Number %s is attached to VLANs: " %(json_resp[i]['serialNumber']))
    print(json.dumps(resp.json()["response"], indent=4))
