import pytest  
import requests 
import json 
from requests.models import Response

def addNewUser(u_id, u_name, stat = 0): 
    headers =  {"Content-Type":"application/json"} 
    url_post_user='https://petstore.swagger.io/v2/user' 
    newUser = {
        "id": u_id,
        "username": u_name,
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": stat
        }
        
    r = requests.post(url_post_user, data = json.dumps(newUser),headers=headers)      
    if checkUser(u_name) == True: 
        return print(r.status_code) 
    else: 
        print("User is not added !") 

def checkUser(uname): 
    headers =  {"Content-Type":"application/json"}  
    url = 'https://petstore.swagger.io/v2/user' 
    r = requests.get(url+'/{}'.format(uname),headers=headers) 
    if uname in r.text: 
        return True 
    else: 
        return False

def test_getUserByusername(u_name): 
    headers =  {"Content-Type":"application/json"} 
    url_get_u='https://petstore.swagger.io/v2/user' 
    r = requests.get(url_get_u+"/{}".format(u_name),headers=headers) 
    #assert r.status_code == 200, "Success"
    return r.text 


def test_UpdateUserByusername(u_name): 
    headers =  {"Content-Type":"application/json"} 
    url_get_u='https://petstore.swagger.io/v2/user' 
    body = {
        "id": 1,
        "username": "user",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
        }
    r = requests.put(url_get_u+"/{}".format(u_name),data = json.dumps(body), headers=headers) 
    #assert r.status_code == 200, "Success"
    print(r.status_code)
    return r.status_code 

addNewUser(1,"droid")
print(test_getUserByusername("droid"))
test_UpdateUserByusername("droid")
print(test_getUserByusername("user"))
