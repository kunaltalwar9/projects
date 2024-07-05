'''
#!/bin/python3

import math
import os
import random
import re
import sys
import array
from array import *
'''
#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
#
'''
def sorting(stringss):
for i in range(0, len(arr1)):
    for j in range(i+1, len(arr1)):
        if arr[0]!="f":
'''

'''
arr1= ["f","r","a","m","e","r"]
aar2= ["r","e","m","f","a","r"]
arr4= array('k', ["a","a","g","m","n","r","s"])
#arr4=array()

def funWithAnagrams(text):
    arr1= ["f","r","a","m","e","r"]
    aar2= ["a","a","g","m","n","r","s"]
   # arr3=[e,a,f,m,r,r]

    # Write your code here
if arr4[0]!="a":
    arr4[0]="a"
    return arr4


if arr4[1]!="n":
    arr2[1]="n"

print(arr4)

if __name__ == '__main__':
'''

'''
def sorts(arrs):
    if not arrs:
        return []
    return (sorts([x for x in arrs[1:] if x< arrs[0]])    
            + arrs[0]+ sorts([x for x in arrs[1:]]) if x>= arrs[0])
'''
#----------------------------------------------------------------------------------------------
'''

arr4 = array('k', ["a", "a", "g", "m", "n", "r", "s"])
if arr4[0] != "a":
    arr4[0] = "a"

print(arr4[0])
'''
#--------------------------------------------------------------------------
'''
String= ("I am a Tester, Would have appreciated if questions would have been from Testing and not coding, "
         "though I am still trying to learn coding. Grateful for the opportunity given" and "whatever is tried, copied or"
        " modified from variou sorces, as still learning! and will learn within a specified time for sure, "
        "test me after some months :)")

fptr = open(os.environ['OUTPUT_PATH'], 'w')

text_count = int(input().strip())

text = []

for _ in range(text_count):
    text_item = input()
    text.append(text_item)

result = funWithAnagrams(text)

fptr.write('\n'.join(result))
fptr.write('\n')

fptr.close()
'''
#----------------------------------------------------------------------------------------------
'''
driver = webdriver.Firefox(executable_path=r"C:\\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
time.sleep(4)
links=driver.find_elements(By.TAG_NAME, "a")
print("Number of links",len(links) )
for link in links:
    tags = link.tag_name
    for ta_gs in tags:
        #ta_gs= tags is not None
        var = ta_gs != None
        print("Text of Link", link.text,"Tag of Link", ta_gs)
'''