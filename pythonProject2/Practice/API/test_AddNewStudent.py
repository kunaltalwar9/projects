import requests
import json
import jsonpath


def test_add_student_data():
    API_URL = 'https://thetestingworldapi.com/api/studentsDetails'
    f = open('C:/Users/Kunal Talwar/Desktop/Python/RequestJson.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

# In Terminal pytest test_AddNewStudent.py -s

def test_get_student_data():
    API_URL = 'https://thetestingworldapi.com/api/studentsDetails/3034'
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 3034

