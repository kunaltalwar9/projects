import requests

# http://rahulshetty.acacdemy.com

cookie = {'visit-month': 'February'}
response = requests.get('http://rahulshetty.acacdemy.com',allow_redirects= False,cookies= cookie, timeout= 1)
# after putting allow redirects to false,  it will not show status code as 200 and will show 301, because we have stopped the redirection after hitting
print(response.history) # for checking redirection
print(response.status_code)
se = requests.session()
se.cookies.update(cookie)
res = se.get('https://httpbin.org/cookies', cookies={'visit-year': '2022'})
res1 = requests.get('https://httpbin.org/cookies', cookies={'visit-year': '2022'})
print(res.text, res1.text)

# Sending attachment in API response

files = {'file':open('C:\\Users\\Kunal Talwar\\Desktop\\WWG.txt', 'rb')}
url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage' #9843217 is petID
r = requests.post(url, files = files)
print(r.status_code, r.text)