from test_data import *

def json_search(key, input_object):
    """
    Search a key from JSON object, get nothing back if key is not test_search_found
    key : keyword to be search, case senstive
    input_object : JSON object to be parsed
    inner_function() is actually doing the job
    return a list of key:value pair
    """

    ret_val = []
    def inner_function(key, input_object):
        if isinstance(input_object, dict): # handle dicks
            for k, v in input_object.items():
                if k == key:
                    temp = {k:v}
                    ret_val.append(temp)
                if isinstance(v, dict):
                    inner_function(key, v)
                elif isinstance(v, list):
                    for item in v:
                        if not isinstance(item, (str, int)):
                            inner_function(key, item)
        else: # handle a list, some APIs return JSON obect in a list
            for val in input_object:
                if not isinstance(val, (str, int)):
                    inner_function(key, val)
    inner_function(key, input_object)
    return ret_val
print(json_search("issueSummary", data))
print(json_search("XY&^$#*@!1234%^&", data))
