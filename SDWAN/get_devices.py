import requests
import pprint
import urllib3

# disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Auth info
vmanage_host = 'devasc-sdwan-1.cisco.com'
vmanage_port = '443'
vmanage_username = 'devnetuser'
vmanage_password = 'RE!_Yw519_27'

#URL me
base_url = 'https://%s:%s' %(vmanage_host, vmanage_port)

# token from j_security_check
login_action = '/j_security_check'

# login payload
login_data = {'j_username' : vmanage_username, 'j_password' : vmanage_password}

# login url
login_url = base_url + login_action

# session object
session = requests.session()

# login POST
login_response = session.post(url=login_url, data=login_data, verify=False)
if b'<html>' in login_response.content:
    print ("Login Failed")
    exit(1)

xsrf_token_url = base_url + '/dataservice/client/token'

login_token = session.get(url=xsrf_token_url, verify=False)
if login_token.status_code == 200:
    if b'<html>' in login_token.content:
        print ("Login Token Failed")
        exit(1)

    session.headers['X-XSRF-TOKEN'] = login_token.content

# get devices
device_url = base_url + '/dataservice/device'

device_list = session.get(url=device_url, verify=False)
if device_list.status_code == 200:
    json_data = device_list.json()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json_data)
else:
    print(device_list.status_code)
    exit(1)
