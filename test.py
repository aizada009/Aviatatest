import pytest  
import requests 
import json 
from requests.models import Response

def addNewPet(pet_id, pet_name,stat="available"): 
    headers =  {"Content-Type":"application/json"} 
    url_post_pet='https://petstore.swagger.io/v2/pet' 
    newPet = {
        "id": pet_id,
        "category": {
        "id": 0,
        "name": "string"
        },
        "name": pet_name,
        "photoUrls": [
        "string"
        ],
        "tags": [
        {
        "id": 0,
        "name": "string"
        }
        ],
        "status": stat
}
    r = requests.post(url_post_pet, data = json.dumps(newPet),headers=headers)      
    if checkPet(pet_id,pet_name) == True: 
        return print(r.status_code) 
    else: 
        print("Pet is not added !") 

def checkPet(pid, pname): 
    headers =  {"Content-Type":"application/json"} 
    url = 'https://petstore.swagger.io/v2/pet' 
    r = requests.get(url+'/{}'.format(pid),headers=headers) 
    if pname in r.text: 
        return True 
    else: 
        return False

def test_getPetById(pet_id): 
    headers =  {"Content-Type":"application/json"} 
    url_get_pet='https://petstore.swagger.io/v2/pet' 
    r = requests.get(url_get_pet+"/{}".format(pet_id),headers=headers) 
    #assert r.status_code == 200, "Success"
    return r.text 


def DeletePetById(pet_id, pname): 
    headers =  {"Content-Type":"application/json"} 
    url_get_pet='https://petstore.swagger.io/v2/pet' 
    if checkPet(pet_id, pname) == True: 
        r = requests.delete(url_get_pet+"/{}".format(pet_id),headers=headers) 
        return r.status_code
    else: 
        print("Pet not found!") 

addNewPet(4,"Murzik")
print(test_getPetById(4))
DeletePetById(4,"Murzik" )
print(test_getPetById(4))
