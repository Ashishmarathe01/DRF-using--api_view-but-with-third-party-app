# this thid party app for testinmg purpose for sending json responese
# made client side app for giving data

import requests
import json
URL="http://127.0.0.1:8000/"


# for geting data using with id or withough id
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data) # converting data into json
    headers={'content-Type':'application/json'} # used for giving plane json data
    r =requests.get(url=URL, headers=headers,data=json_data) # sending request to api
    data=r.json() # converting get response to json
    print(data)


# get_data(1)

# for update data
def Partial_update_data():
    data={
        'id':1,
        'name':'love',
        'age': 30,

    }
    json_data=json.dumps(data)
    r=requests.patch(url=URL,data=json_data)
    print(r.json())

# Partial_update_data()

# complter update
def complete_update_data():
    data={


        'age': 4,
        'city':'ravivar',
        'id':3


    }
    json_data=json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r=requests.put(url=URL,headers=headers,data=json_data)
    print(r.json())
complete_update_data()


# delete data
def delete_data():
    data={
        'id':2,
    }
    json_data=json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r=requests.delete(url=URL,headers=headers,data=json_data)
    print(r.json())
# delete_data()



# for POST
def post_data():
    data={

        'name':'jay',
        'age': 30,
        'city':'lavasa'

    }
    json_data=json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r=requests.post(url=URL, headers=headers,data=json_data)
    print(r.json())

# post_data()






# data={
#     'name':'love',
#     'age':2,
#     'email':'ashish@gmail.com'
#
# }
#
# json_data=json.dumps(data) # for conversion in json
# r=requests.post(url=URL,data=json_data)# for sending data
# data=r.json()# for getting response is given by webappicatuion
# print(data)
