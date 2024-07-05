import requests
import json
import jsonpath
from payLoad import *


url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

print(response.content)

json_response = json.loads(response.text)
print(json_response)

pages = jsonpath.jsonpath(json_response, 'total_pages')
# print(pages)

first_name = jsonpath.jsonpath(json_response,'data[0].first_name')
# print(first_name)
for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    # print(first_name[0])
'''

'''
'''
url2 = "https://reqres.in/api/users"

file = open('C:\\Users\\Kunal Talwar\\Desktop\\Python\\Create User.json', 'r')

json_input = file.read()
request_json = json.loads(json_input)

response2 = requests.post(url2, request_json)
assert response2.status_code == 201
print(response2.headers.get('Content-Length'))
response2_json = json.loads(response2.text)
id = jsonpath.jsonpath(response2_json, 'id')
print(id[0])

response3 = requests.get("http://216.10.245.166/Library/GetBook.php", params={'AuthorName':'Rahul Shetty2'})
print(response3.text)
dict_response3 = json.loads(response3.text)
print(dict_response3[0]['isbn'])
json_response3 = response3.json()
print(json_response3[0]['isbn'])
assert response3.status_code == 200
print(response3.headers)
assert response3.headers['Content-type'] == 'application/json;charset=UTF-8'
for actualbook in json_response3:
    if actualbook['isbn'] == 'RGHCC':
        print(actualbook)
        break
# requests.readthedocs.io, httpbin.org
'''
'''
addBook_response = requests.post("http://216.10.245.166/Library/Addbook.php", json=addBookPayload("as65sf")

#{"name":"Learn Appium Automation with Java",
#"isbn":"bcdf7",
#"aisle":"227f",
#"author":"John foe"}

, headers= {"Content-Type": "application/json"},
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
'''