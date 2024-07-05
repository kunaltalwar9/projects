import requests
import configparser
from payLoad import *
import json
from utilities.configurations import *
from utilities.resources import *

#config = configparser.ConfigParser()
#config.read('utilities/properties.ini')

# addBook_response = requests.post("http://216.10.245.166/Library/Addbook.php", json=addBookPayload("as65sf")
url = getConfig()['API']['endpoint']+ ApiResources.addBook
headers = {"Content-Type": "application/json"}
addBook_response = requests.post(url, json=addBookPayload("as65sf")

#{"name":"Learn Appium Automation with Java",
#"isbn":"bcdf7",
#"aisle":"227f",
#"author":"John foe"}

, headers= headers,
 )

print(addBook_response.json())
response4_json = addBook_response.json()
book_ID = response4_json['ID']
print(book_ID)

response_deleteBook = requests.post("http://216.10.245.166/Library/DeleteBook.php", json=
    {
        "ID": book_ID
    }, headers= {"Content-Type": "application/json"})

#assert response_deleteBook.status_code == 200
response5_json = response_deleteBook.json()
print(response5_json)
#assert response5_json["msg"] == "book is successfully deleted"

se = requests.session()
se.auth = auth = ('rahulshettyacademy', getPassword())

url2 = 'https://api.github.com/user'
github_response = requests.get(url2,verify=False, auth=('rahulshettyacademy', getPassword()))
assert github_response.status_code == 200

url3 = 'https://api.github.com/user/repos'
response = se.get(url3)
#response = requests.get(url3, auth=('rahulshettyacademy', getPassword()))
print(response.status_code)