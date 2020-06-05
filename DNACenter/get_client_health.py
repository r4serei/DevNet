from dna_center_authenticate import *

# Client Health API wrapper
def get_client_health(dnacip, headers, params):
    # client health uri
    uri = "https://" + dnacip + "/dna/intent/api/v1/client-health"

    try:
        if params == "":
            print("\n---\nGET %s" %(uri))
        else:
            print("\n---\nGET %s?%s" %(uri, params))

        resp = requests.get(uri, headers=headers, params=params, verify=False)
        return resp
    except:
        # toekn errorrrr
        print("Status: %s" %r.status_code)
        print("Response: %s" %r.text)
        sys.exit()

# Auth
token = get_X_auth_token(dnacip, username, password)
print("returned Authentication Token: ", (token))

# assign toekn to headers
headers = {"x-auth-token": token}

# get count of all devices knonwn to DNA Center
params = ""
resp = get_client_health(dnacip, headers, params)
print("All clients health: ", json.dumps(resp.json()["response"], indent=4))
