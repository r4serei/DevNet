import requests
import json

# query func
def webex_api(url, headers, params):
    if params == {}:
        res = requests.get(url, headers=headers)
    else:
        res = requests.get(url, headers=headers, params=params)
    return res

# PrettyPrinter
def webex_print(res):
    formatted_message = """
    Webex Teams API Response
    -------------------------------------
    Response Status Code    : {}
    Response Link Header    : {}
    Response Body           : {}
    -------------------------------------
    """.format(res.status_code,  res.headers.get('Link'), json.dumps(res.json(), indent=4))
    print(formatted_message)

# input access token here
access_token = "ODFkZTMxNTctMTc2Ny00MTYwLWJkNDItNzBiNDNjNmUxNDdhYzk5NzlhMzItNWEy_PF84_e271494a-7cc7-4aed-badb-78d7029ffc5e"
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
url = 'https://api.ciscospark.com/v1/people/me'

res = webex_api(url, headers, params={})

res = requests.get(url, headers=headers)

#print Auth info
print(json.dumps(res.json(), indent=4))

# print memberships
url = 'https://api.ciscospark.com/v1/rooms'

params = {
    "max": 10
}
res = webex_api(url, headers, params)

webex_print(res)
#print(json.dumps(res.json(), indent=4))


url = 'https://api.ciscospark.com/v1/people'
params = {
    'email': 'andy.ford@ascenaretail.com'
}
res = webex_api(url, headers, params)
print(res.json())
