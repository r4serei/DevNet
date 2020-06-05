import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys

#Auth credentials
dnacip = "devasc-dnacenter-1.cisco.com"
username = "devnetuser"
password = "C!3c0d$Y"

# auth method
def get_X_auth_token(dnacip, username, password):
    # Auth to remote server

    # supress warning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # Auth API full URI
    post_uri = "https://" + dnacip + "/dna/system/api/v1/auth/token"
    print("\nAuthenticate: POST %s" %(post_uri))

    try:
        # verify = False to no verify cert
        r = requests.post(post_uri, auth=(username, password), verify=False)
        return r.json()["Token"]
    except:
        # Something wrong, cannot get access Token
        print("Status: %s" %r.status_code)
        print("Response: %s" %r.text)
        sys.exit()
