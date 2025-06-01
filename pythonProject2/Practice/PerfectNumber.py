import pdb
import pprint
import random
from array import *

'''
str1 = input("Type Word")

def reversify(str1):
    if len(str1) == 1:
        return str1
    else:
        return reversify(str1[1:]) + str1[0]

str2 = reversify(str1)
print(str2)
print(''.join(list(reversed(str1))))

'''
'''
sum = 0
for i in range(1,5):
    sum = sum +i
print(sum)
'''
'''
num = int(input("enter number"))
result = 0
for i in range(1, num):
    if (num % i) == 0:
        result = result + i

    #else:
    #    break
if result == num:
    print("perfect") 
'''
# -------------------------------------------------------
'''
# self tried
num1 = int(input("enter number"))
arr = []
for i in range(0, num1):
    arr.append(1)
print(arr)
for i in range(1, num1):
    for j in range(1, i):
        if num1 % i == 0:
        #print(i)
        #arr.append(i)
            arr[i - 1] = i
        #else:
         #  del arr[4]
         #   arr.pop(i-1)
print(arr)
print(arr[1:])

for c in range(1, len(arr)):
    for m in arr[1:]:
        print(m)
        z = arr.index(m)
        print("index value is {}".format(z))
        if m == 1:

            print(arr)
            arr.pop(z)
            #arr[1:].remove(1)
            print(arr)
            c = 1
        else:
            pass
print(arr)

#------------------------------------------------------------------------------------------------
'''
'''
num1 = int(input("enter number"))
num2 = int(input("enter number"))
com1 = 1
com2 = 1
arr = []
for i in range(1, num1):
    if num1 % i == 0:
        # print(i)
        arr.append(i)
        arr[i - 1] = i
        print(arr)
    else:
        break
        #arr[0] = i
        # print(arr[i - 1])
        #print(arr[0])
'''

'''
        def array():
            arr[i - 1] = i
            print(arr[i - 1])
            return arr[i - 1]

for k in range(1, num2):
    if num2 % k == 0:
        print("Hi")
        '''

# ----------------------------------------------------------------
'''
str1 = input("reverse")

def reversify(str1):
    if len(str1) == 1:
        return str1
    else:
        return reversify(str1[1:]) + str1[0] 

str2 = reversify(str1)
print(str2) 
print(''.join(list(reversed(str1))))
'''
'''
s = "Kunal"
# print(len(s))
for i in range(1, len(s) + 1):
    #    s[0] = s[-1]
    #    print(s)
    print(s[-i])
'''
'''
str1 = input('type word')
str2 = ''
for i in str1:
    str2 = i + str2
print(str2)

'''
# ------------------------------------------------------------------
'''
lis = [2, 3, 6, 7, 9, 12, 8, 4]
def reve(l):
    return l[::-1]
print(reve(lis))
'''
# --------------------------------------------------------------------
'''
list1 = [56, 3, 2, 0, 7, 20]
# l = len(list1)
'''
'''
def swap(list1):
    if len(list1)==1:
        return list1
    else:
        for i in range(0, len(list1)-1):
            list1[i] = min(list1)
            return swap(list1[i+1:])  # +list1[0]
        print(list1)
#-----------------------------------------------------------------------------------

ask = [9,5, 1, 2, 3 ,4 , 6, 6 ,8]
for j in range(0, len(ask)):
    for i in range(0, len(ask)-1):
        if ask[i] > ask[i+1]:
            ask[i], ask[i+1] = ask[i+1], ask[i]
print(ask)


#---------------------------------------------------------------------------
'''
'''
def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


nums = [56, 3, 2, 0, 7, 20]
sort(nums)
print(nums)
'''
'''
#        print(list1)
list2 = swap(list1)
print(list2)
'''
'''
for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val)
    list1[i], list1[min_ind] = list1[min_ind], list1[i]
print(list1)
'''
'''
list2 = [56, 3, 2, 0, 7, 20]
list3 = []
while list2:
    minimum = list2[0]
    for x in list2:
        if x > minimum:
            minimum = x
    list3.append(minimum)
    list2.remove(minimum)
print(list3)
'''

# -------------------------------------------------------------

'''
def num_coins(cents):
    coins = [1, 2, 5, 10, 20]
    count = 0
    for coin in coins:
        while cents >= coin:
            cents = cents - coin
            count = count + 1
    return count


print(num_coins(32))
'''
# -------------------------------------------------------------------
'''
inte = [2, 3, 6, 7, 9, 12, 8, 4, ]
count = 0
var = 'ABC'
newvar = ''
for c in var:
    newvar += c * 2
print(newvar)

for i in inte:
    if i % 2 == 0:
        count += 1
print(count)
'''

# -----------------------------------------------------------------
'''
for num in range(100, 202):
    if all(num % i != 0 for i in range(2, num)):
        print(num)
'''
'''
for num in range(100, 202):
    for i in range(2, num):
        if num % i != 0:
            print(i)

for num in range(100, 202):
    if num % 1 == 0 and num % num == 0 and (num % i != 0 for i in range(1, num + 1)):
        print(num)
'''

# --------------------------------------------------------------------------
'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(0, 16):
    print(fib(i))
'''
# -------------------------------------------------------------------------------
'''
num = int(input("enter"))
a = 0
b = 1
print(a)
print(b)

for i in range(num):
    c = a + b
    a = b
    b = c
    print(c)
'''
'''
f = 0
g = 1
h = []
for i in range(7):
    h.append(f)
    h.append(g)
    print(h)
    f = f + g
    g = f + g
'''
# -----------------------------------------------------
# shit
'''
def fun(n):
    if n == 0:
        print(0)
        print(1)
        return 0
    elif n == 1:
        return fun(0)
    else:
        return fun(n - 1)


for i in range(6):
    fun(i)
    
'''

# -----------------------------------------------------


'''
num_array = array('i', range(11, 19))
print("num_array before the reverse: {}".format(num_array))
print("Reverse num_array using slice operator: {}".format(num_array[::-1]))
print("Reverse num_array using List comprehension: {}".format(array('i', [num_array[n] for n in range(len(num_array) - 1, -1, -1)])))

'''

# --------------------------------------------------------------------------
'''
num_array = array('f', range(0, 10))
print("num_array before deletion: {}".format(num_array))
del num_array[len(num_array)-1]
print("num_array after removing the last element: {}".format(num_array))
'''
# --------------------------------------------------------------------------
'''
from array import *

def print_Result(iter, orig):
    print("Original: ", orig)
    print("Reversed: ", end="")
    for it in iter:
        print(it, end=' ')


def reverse_Array(in_array):
    result = reversed(in_array)
    print_Result(result, in_array)

# Declare an array of 8 numbers
in_array = array('i', range(11, 19))

reverse_Array(in_array)

in_array = [2, 3, 6, 7, 9, 12, 8, 4, ]
in_array.reverse()
print(in_array)

# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)

'''
'''
from array import *

def print_result(iter):
    for it in iter:
        print(it, end=' ')
        #print(it)


in_array = array('i', range(11, 19))

iter = reversed(in_array)
print_result(iter)
'''
# --------------------------------------------------------------------------
'''
def palindrome(s):

     rev = ''.join(reversed(s))
     if s== rev:
         return True
     return False

palindrome('madam')
'''
'''
s = 'Madam'
s2 = [s]

def palin(s3):
     s1 = s2
     s1.reverse()
     s1 = ''.join(s1)
     return s1

palin('Madam')

if s == s3:
    print("True")
'''
# -------------------------------------------------------------------------
'''
l = [1, 2, 3, 4, 5, 6, 7, 4, 2, 3]

print(set([x for x in l if l.count(x) > 1]))
'''
# ---------------------------------------------------------------------------
'''
s = 'Why thi Kolaveri DI'
print(s.split())
'''

# -------------------------------------------------------------------------
'''
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


s = ['Geeks', 'for', 'Geeks']
print(listToString(s))
# ----------------------------------------------------------------------

enter = input("enter message").lower()
b = []
def fun(s):
    for j in range(0, len(enter)):

        if s[j] == 'a':
            b.append('z')
        if s[j] == 'b':
            b.append('y')
        if s[j] == 'c':
            b.append('x')
        if s[j] == 'd':
            b.append('w')
        if s[j] == 'e':
            b.append('v')
        if s[j] == 'f':
            b.append('u')
        if s[j] == 'g':
            b.append('t')
        if s[j] == 'h':
            b.append('s')
        if s[j] == 'i':
            b.append('r')
        if s[j] == 'j':
            b.append('q')
        if s[j] == 'k':
            b.append('p')
        if s[j] == 'l':
            b.append('o')
        if s[j] == 'm':
            b.append('n')
    print(''.join(b))

fun(enter)

#------------------------------------------------------------------------

s1 = 'abcdefghijklmnopqrstuvwxyz'
i = 0
mp = {}
for i in range(26):
    mp[s1[i]] = s1[-i - 1]
print(mp)


#------------------------------------------------------------------------
'''
'''
import math

def shift_to_right(x, y):
    while y > 0:
        z = 2 ** y
        return math.floor(x / z)
'''
'''
# instance and class variables have different purpose, one is attached to object, other is not attached
# new keyword is not required when creating an object

class Calculator:
    num = 100
    
    def __init__(self, a, b):
        self.aa = a
        self.bb = b
        print("Automatically called when object of class is created")

    def data(self):
        print("print Hi")

    def add(self):
        return self.aa + self.bb + Calculator.num


obj = Calculator(2, 3).data()
obj2 = Calculator(2,3).add()
print(obj2)

obj1 = Calculator(3, 4)
obj1.data()
obj3 = Calculator(3,4).add()
print(obj3)
'''
'''
str1 = "ABC"
str2 = "ABCD"
str3 = "DEFG"
str4 = " QWERTY "

print(str1 in str3)
print(str1.split("B"))
print(str4.strip()) #strips of spaces
print(str4.lstrip(), str4.rstrip())
'''
'''
file = open('text.txt')
#print(file.read())
#print(file.read(5))
#print(file.readline()) # will read from the character where focus is after the previos line,
# use either read or readline, readline reads a single line at a time
#print(file.readline(3))
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

lst = ["abc", "bcd"," egh", "ijk"]
for line in file.readlines():
    print(line) 

file.close()
'''

'''
cartitems = 0
if cartitems != 2:
    raise Exception("Products in cart not matching")
if cartitems != 2:
    pass
assert(cartitems == 2)       
'''

'''
try:
    with open(filelogs.txt) as reader: # filelogs named file does not exist, so it will, so kept in try block
        reader.read()
except: #except keyword instead of catch keyword
#except Exception as e:
    #print(e)
    print(" Reached because error in try block ")
finally:
    print(" will be printed whether or not try except fails, #use it with try n except block")
'''
# -------------------------------------------------------------------

'''
import random

def is_success():
    lists = [True, True, False, False, False, False, False, False, False]
    for return_answer in random.choices(lists):
    #return_answer = random.choice(lists)
        print(return_answer)
        return return_answer


while not is_success():
    #print(is_success())
    continue
'''
# -------------------------------------------------------------------
'''
import time
def is_status_success():
    print("Checking the status of process")
    lists = [True, True, False, False, False, False, False, False, False]
    bool_to_return = random.choice(lists)

    return bool_to_return

def retry_with_counter_until_is_success(max_retry=10, sleep_time=3):
    counter = 0
    is_success = False
    while counter < max_retry:
        counter += 1
        print(f"Retry no:{counter}")
        is_success = is_status_success()
        print(f"The success status is {is_status_success()}")
        if is_success:
            print("The Process is success")
            break
        else:
            time.sleep(sleep_time)
    #if not is_success:
    else:
        raise Exception(f"process did not succeed after trying for {max_retry * sleep_time} seconds")

retry_with_counter_until_is_success()
'''
# ------------------------------------------------------------------------
'''
import random
import string
import pdb
list_of_domains = ['gmail.com', 'outlook.com', 'onedrive.com', 'yahoo.com', 'bing.com']
letters = string.ascii_lowercase
length_of_email = 10
all_emails = []
output_file = 'random_emails_output.csv'

for domain in list_of_domains:
    for i in range(20):
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
        #email = random_string + '@' + domain
        email = '{}@{}'.format(random_string, domain)
        all_emails.append(email)
#print(all_emails)
pdb.set_trace()

with open(output_file, 'w') as my_f:
    #for mails in all_emails:
        #my_f.write(mails)
        #my_f.write(', \n')
    my_f.write(',\n'.join(all_emails))
'''
# -------------------------------------------------------------------------------
'''
import random
import string
import pdb

list_of_domains = ['gmail.com', 'outlook.com', 'onedrive.com', 'yahoo.com', 'bing.com']
letters = string.ascii_lowercase
length_of_email = 10
total_no_of_emails = 100
all_emails = []
output_file = 'random_emails_output.csv'

for i in range(100):
    rand_domain = random.choice(list_of_domains)
    # rand_domain = random.sample(list_of_domains, 100)
    random_string = ''.join(random.choice(letters) for i in range(length_of_email))
    rand_email = random_string + '@' + rand_domain
    all_emails.append(rand_email)

with open(output_file, 'w') as my_f:
    my_f.write(',\n'.join(all_emails))
'''
# -------------------------------------------------------------------------------
'''
all_trades_raw = "data in raw format"
result_file_path = "complete path of file like path of folder/output file name which is to be created.csv"


def create_trades_files(output_path, trades): 
    with open(output_path, 'w') as f:
        f.write("symbol,trade_type,entry_price,stop_loss_price,target\n")
        for i in trades:
            f.write(f" {i['symbol']}, {i['trade_type']}, {i['entry_price']}, {i['stop_loss_price']}, {i['target']}\n") 


def raw_string_to_dictionary(input_string):
    input_as_a_list = input_string.split('\n\n') 
    all_trades = []
    for trade in input_as_a_list:
        trade_split = trade.split()
        symbol = trade_split[0]
        trade_type = trade_split[1]
        entry_price = trade_split[2]
        stop_loss_price = trade_split[5]
        target = trade_split[7]
        trade_dictionary = {
            'symbol': symbol,
            'trade_type': trade_type,
            'entry_price': entry_price,
            'stop_loss_price': stop_loss_price,
            'target': target
        } 
        all_trades.append(trade_dictionary)
    # print(all_trades)
    # pprint.pprint(all_trades)
    return all_trades
    # pdb.set_trace()
    # pdb.set_trace()


all_trades_formatted = raw_string_to_dictionary(all_trades_raw)
create_trades_files(result_file_path, all_trades_formatted) 
'''
# -----------------------------------------------------------------------------------------------------
'''

tuple_element1 = (1, 2, 3, 4, "Python", 1, 2, 3, 4)
a = "python" in tuple_element1
print(a)

tuple_element2 = (5, 6, 7)
c = tuple_element1 + tuple_element2
print(c)

d = {1: 5, 3: 7, 6: 8}
print(d[3])
# update values in dictionary
d[3] = 11
print(d[3])
# append values in dictionary
d[9] = 14
d[11] = 17
print(d)
for i in d.values():
    print(i)
for i, j in d.items():
    print(i, "and", j)
# remove some values
d.pop(11)
print(d)
# clear values
# d.clear(), print(d)
a = {1,2,3}
b ={4,5,6,1,2}
c = a.union(b)
print(c)
e = 7 in c
print(e)
f = 6 in c
print(f)

x = lambda a: a+10
print(x(5))
x = lambda a,b: a+b+10
# print(x(5,7))
'''
'''
from array import *

def print_Result(iter, orig):
    print("Original: ", orig)
    print("Reversed: ", end="")
    for it in iter:
        print(it, end=' ')


def reverse_Array(in_array):
    result = reversed(in_array)
    print_Result(result, in_array)

# Declare an array of 8 numbers
in_array = array('i', range(11, 19))

reverse_Array(in_array)

'''

'''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''

for i in range(nr_letters+nr_symbols+nr_numbers):
    r = random.randint(0,2)
    if r == 0:
        password += random.choice(letters)
    elif r ==1:
        password += random.choice(numbers)
    else:
        password +=random.choice(symbols)
print(password)


'''
'''

my_dict = {'a':1,'b':2,'c':3}

def get_key(my_dict, value):
    for key, val in my_dict.items():
        if val == value:
            print(key)
            return key
    return None

get_key(my_dict,2)

for key in my_dict:
    print(key)
    print(my_dict[key])


print(my_dict[0])


'''

# Random Pratice codes Hacker Earth

'''
# Hacker Earth Zoos

name = input()
z = o = 0
for i in name:
    if i.lower()=='z':
        z += 1
        # print(z)
    elif i.lower() == 'o':
        o +=1
if 2*z == o:
    print("Yes")
else:
    print("No")

'''

'''

# Hacker Earth Hidden Treasure
def solve(n, nums):
    l = []
    for i in nums:
        i = str(i)
        first_digit = int(i[0])
        second_digit = int(i[1])
        sum_of_digits = first_digit+second_digit
        # print(sum_of_digits)
        l.append(sum_of_digits)
    print(l)

    count = 0
    frequency = {}
    for i in l:
        frequency[i] = l.count(i)
        # print(f" {l.count(i)} pairs have sum of {i} ")
    print("#### FREQUENCY ####")
    print(frequency)
    for key, val in frequency.items():
        # print(f"{key} is repeated {val} times")
        if val == 2:
            # print(f"{key} is repeated {val} times")
            count += 1
    return count

n = int(input())
nums = list(map(int, input().split()))
out_ = solve(n, nums)
print(out_)

# 51 71 13 61 33 22 45 72 41 35 30 11
'''
# Number Guessing Game

game_number = random.randint(1,100)
# print(game_number)
def hard():
    count = 5
    while count > 0:
        your_number = int(input("Make a guess: "))
        if your_number == game_number:
            print(f"You Won, Correct number was {game_number}")
            break
        elif your_number > game_number:
            print("Too High")
            count -= 1
        elif your_number < game_number:
            print("Too Low")
            count -= 1
    if count == 0:
        print("You Lose")
        print(f"Correct Number was {game_number}")

def easy():
    count = 10
    while count > 0:
        your_number = int(input("Make a guess: "))
        if your_number == game_number:
            print(f"You Won, Correct number was {game_number}")
            break
        elif your_number > game_number:
            print("Too High")
            count -= 1
        elif your_number < game_number:
            print("Too Low")
            count -= 1
    if count == 0:
        print(f"Correct Number was {game_number}")


level = input("Choose level: ")

if level.lower() == 'hard':
    hard()
elif level.lower() == 'easy':
    easy()








'''
from appium.webdriver.appium_service import AppiumService

# Step 2 : Create object for Appium Service class
appium_service = AppiumService()

# Step 3 : Call Start method by using Appium Service class object

# Step 5 : To Call stop method by using Appium Service class object
appium_service.stop()

print("Done...")

'''