# Python 100 day challenge

'''
# Reeborg Hurdle 4

while not at_goal():
    if wall_in_front():
        turn_left()
        while not right_is_clear():
            if right_is_clear():
                jump()
            else:
                move()
        while front_is_clear():
            move()
            if front_is_clear() != True:
                turn_left()
    else:
        move()

while not at_goal():
    while not wall_in_front():
        move()
        if front_is_clear() != True:
            turn_left()
    if wall_in_front():
        turn_left()
        while not right_is_clear():
            if right_is_clear():
                jump()
            else:
                move()
    else:
        move()


'''
import random

'''
# Hangman

import random

word_list = ['banana', 'frog', 'apple', 'camel', 'donkey', 'papaya']
placeholder = ''
word = random.choice(word_list)
print(f'Word is {word} and lenth of word is {len(word)}')

placeholder = []
display = ''

for i in range(len(word)):
    placeholder = ['_'] * len(word)
    display += '_ '
    # placeholder += '_ '
    # placeholder = '_ ' * len(word) ,placeholder = ['_'] * len(word), print(' '.join(placeholder))
print(placeholder)
print(display)

for i in range(0, len(word)):  # Total 5 attempts
    guess_letter = input(f"type {i} letter").lower()

    if word[i] == guess_letter:
        # display.replace('_',i)
        # print(display)
        placeholder[i] = guess_letter
        print(placeholder)
        # print(f"correct at position {i+1}")
    else:
        placeholder[i] = '+'
        print(placeholder)
        # print("Incorrect choice")
        # print(f"incorrect at position {i+1}")
'''
'''
    for i in word:
        if i == guess_letter:
            display += i
        else:
            display += '_'
    print(display)
'''
'''
    for i in range(0, len(word)):
        if word[i] == guess_letter:
            display = ['_ '] * len(word)
            display[i] = guess_letter
            display = ''.join(display)
            print(display)    
            # print(f"correct at position {i+1}")
        else:
            print("Incorrect choice")
            # print(f"incorrect at position {i+1}")
'''

'''
# Hangman Contd.
import random

word_list = ['banana', 'frog', 'apple', 'camel', 'donkey', 'papaya']
word = random.choice(word_list)
placeholder = ['_'] * len(word)
print(f'Word is {word} and length of word is {len(word)}')
print(' '.join(placeholder))

for j in range(len(word)):
    guess_letter = input(f"Type letter {j+1}: ").lower()
    for i in range(len(word)):
        if word[i] == guess_letter:  # Correct comparison
            placeholder[i] = guess_letter
    print(placeholder)
    print(' '.join(placeholder))
    

'''

# Love Calculator

'''
def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    t1=t2=r1=r2=u1=u2=e1=e2=l1=l2=o1=o2=v1=v2=0
    combined_name= name1 + name2
    for i in combined_name:
        if i == 't':
            t1 += 1
    # print(f"T occurs {t1} times")
    for i in combined_name:
        if i == 'r':
            r1 += 1
    # print(f"R occurs {r1} times")
    
    for i in combined_name:
        if i == 'u':
            u1 += 1
    # print(f"U occurs {u1} times")
    for i in combined_name:
        if i == 'e':
            e1 += 1
    # print(f"E occurs {e1} times")
    
    total1 = t1+r1+u1+e1
    # print(f"Total:  {total1}")
    
    for i in combined_name:
        if i == 'l':
            l1 += 1
    # print(f"L occurs {l1} times")
    for i in combined_name:
        if i == 'o':
            o1 += 1
    # print(f"O occurs {o1} times")
    for i in combined_name:
        if i == 'v':
            v1 += 1
    # print(f"V occurs {v1} times")
    for i in combined_name:
        if i == 'e':
            e2 += 1
    # print(f"E occurs {e2} times")
    
    total2 = l1+o1+v1+e2
    # print(f"Total:  {total2}")
    
    print(str(total1)+str(total2))
    
    
    
calculate_love_score("Angela Yu", "Jack Bauer")

'''
# Caesar Cipher

'''
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26

shift = int(input("Shift "))
encrypted_word_list = []
def crypt(name, crypt_type):
    name= str(name.lower())
    for i in name:
        if i == 'a':
            i = 1
        elif i == 'b':
            i = 2
        elif i == 'c':
            i = 3
        elif i == 'd':
            i = 4
        elif i == 'e':
            i = 5
        elif i == 'f':
            i = 6
        elif i == 'g':
            i = 7
        elif i == 'h':
            i = 8
        elif i == 'i':
            i = 9
        elif i == 'j':
            i = 10
        elif i == 'k':
            i = 11
        elif i == 'l':
            i = 12
        elif i == 'm':
            i = 13
        elif i == 'n':
            i = 14
        elif i == 'o':
            i = 15
        elif i == 'p':
            i = 16
        elif i == 'q':
            i = 17
        elif i == 'r':
            i = 18
        elif i == 's':
            i = 19
        elif i == 't':
            i = 20
        elif i == 'u':
            i = 21
        elif i == 'v':
            i = 22
        elif i == 'w':
            i = 23
        elif i == 'x':
            i = 24
        elif i == 'y':
            i = 25
        elif i == 'z':
            i = 26
        #else:
        #    continue



        if crypt_type == 'e':
            i += shift-1
            i = (i % 26)+1
        elif crypt_type == 'd':
            i -= shift+ 1
            i = (i % 26)+1
      #  print(i)

        if i == 1:
            i = 'a'
        elif i == 2:
            i = 'b'
        elif i == 3:
            i = 'c'
        elif i == 4:
            i = 'd'
        elif i == 5:
            i = 'e'
        elif i == 6:
            i = 'f'
        elif i == 7:
            i = 'g'
        elif i == 8:
            i = 'h'
        elif i == 9:
            i = 'i'
        elif i == 10:
            i = 'j'
        elif i == 11:
            i = 'k'
        elif i == 12:
            i = 'l'
        elif i == 13:
            i = 'm'
        elif i == 14:
            i = 'n'
        elif i == 15:
            i = 'o'
        elif i == 16:
            i = 'p'
        elif i == 17:
            i = 'q'
        elif i == 18:
            i = 'r'
        elif i == 19:
            i = 's'
        elif i == 20:
            i = 't'
        elif i == 21:
            i = 'u'
        elif i == 22:
            i = 'v'
        elif i == 23:
            i = 'w'
        elif i == 24:
            i = 'x'
        elif i == 25:
            i = 'y'
        elif i == 26:
            i = 'z'
        #else:
        #    i = i


#        print(i)
        encrypted_word_list.append(i)
#    print(encrypted_word_list)
    print(''.join(encrypted_word_list))


crypt("kunal talwar9", crypt_type= 'e')
'''

'''
# 
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key, val in student_scores.items():
    if student_scores[key] > 90 and student_scores[key]< 100:
        student_grades[key] = 'Outstanding'
    elif student_scores[key] > 80 and student_scores[key]< 90:
        student_grades[key] = 'Exceeds Expectations'
    elif student_scores[key] > 70 and student_scores[key]< 80:
        student_grades[key] = 'Acceptable'
    elif student_scores[key] < 70:
        student_grades[key] = 'Fail'

print(student_grades)


'''
"""
# Blackjack
import random

def card():
    return random.randint(1, 10)


game = True
while game:
    print("######## New Game ########")
    # Step 1: Draw two cards each
    first_card = card()
    second_card = card()
    your_total = first_card + second_card
    computers_first_card = card()

    print(f"Your Cards:[{first_card}, {second_card}]")
    print(f"Your total:{your_total}")
    print(f"Computer's first Card: {computers_first_card}")

    if (first_card == 1 and second_card == 10) or (first_card == 10 and second_card == 1):
        print("Blackjack!, You Won")
        game = False
        break

    choice = input("Next Card?, Yes or No: ")
    # Step Two: If you chose No
    if choice == 'no':
        computers_second_card = card()
        print(f"Computer's Second Card: {computers_second_card}")
        if (computers_first_card == 1 and computers_second_card == 10) or (computers_first_card == 10 and computers_second_card == 1):
            print("Blackjack!, Dealer Won, You Lose")
            game = False
            break
        computers_total = computers_first_card + computers_second_card
        print(f"Computer's Total: {computers_total}")

        while computers_total< 17:
            computer_next_card = card()
            print(f"Computer's next card is {computer_next_card}")
            computers_total += computer_next_card
            print(f"Computer's Total: {computers_total}")

        if computers_total > 21:
            print("You Win")
            game = False
        elif computers_total > your_total:
            print("You Lose")
            game = False
        elif computers_total< your_total:
            print("You Win")
            game= False
        elif computers_total == your_total:
            print("Draw")
            game = False


    # Step 3: If you choose Yes
    elif choice == 'yes':
        while choice == 'yes':
            my_next_card = card()
            print(f"Your next card is {my_next_card}")
            your_total = your_total + my_next_card
            print(f"Your total:{your_total}")
            if your_total > 21:
                print("You Lose")
                game = False
                break
            choice = input("Next Card?, Yes or No: ")
            if choice == 'no':
                computers_second_card = card()
                print(f"Computer's Second Card: {computers_second_card}")
                computers_total = computers_first_card + computers_second_card
                print(f"Computer's Total: {computers_total}")

                while computers_total < 17:
                    computer_next_card = card()
                    print(f"Computer's next card is {computer_next_card}")
                    computers_total += computer_next_card
                    print(f"Computer's Total: {computers_total}")

                if computers_total > 21:
                    print("You Win")
                    game = False
                elif computers_total > your_total:
                    print("You Lose")
                    game = False
                elif computers_total < your_total:
                    print("You Win")
                    game = False
                elif computers_total == your_total:
                    print("Draw")
                    game = False

    next_game = input("Next Game?, Yes or No: ")
    if next_game == 'yes':
        game = True
    else:
        game = False
        print("##### END OF GAME #####")



'''

first_card = card()
second_card = card()
your_total = first_card + second_card
computers_first_card = card()
computers_total = computers_first_card

def win_or_lose(your_total,computers_total):
    if your_total > 21:
        print("You Lose")
    elif computers_total > 21:
        return "You win"

game = True
if your_total > 21:
    print("You Lose")
    game = False


def next(your_total,computers_total):
    choice = input("Next Card?, Yes or No: ")
    if choice.lower() == 'yes':
        print("###### NEXT CARDS ###### ")
        third_card = card()
        print(f"Your next card is {third_card}")
        computers_second_card = card()
        print(f"Computer's next card is {computers_second_card}")
        your_total += third_card
        computers_total += computers_second_card
        print(f"Your total:{your_total}")
        print(f"Compter's Total: {computers_total}")
        if your_total > 21:
            print("You Lose")

        # win_or_lose(your_total, computers_total)
        next(your_total,computers_total)
        game = False
    elif choice.lower() == 'no':
        print(f"Your Final Hand: [{first_card}, {second_card}]")
        computers_third_card = card()
        print(f"Computer's Final Hand: {computers_first_card}, {computers_third_card}")
        computers_total += computers_third_card
        print(f"Compter's Total: {computers_total}")
        if your_total > computers_total:
            print("You Win")
        elif your_total < computers_total:
            print("You Lose")
        elif your_total == computers_total:
            print("Draw")
        elif computers_total > 21:
            print("You Win")

        # win_or_lose(your_total, computers_total)
        #next(your_total,computers_total)
    # choice = input("Next Card?, Yes or No: ")
        game = False

print(f"Your Cards:[{first_card}, {second_card}]")
print(f"Your total:{your_total}")
print(f"Computer's first Card: {computers_first_card}")
print(f"Compter's Total: {computers_total}")

while game:
    next(your_total,computers_total)


#while choice == 'yes':
#    choice(choice,your_total,computers_total)
'''
"""
"""
import random
data = [
    {
        'name' : 'Instagram',
        'follower_count':346,
        'description':'Social Media Platform',
        'country':'United States'

    },
    {
        'name' : 'Cristiano Ronaldo',
        'follower_count':215,
        'description':'Footballer',
        'country':'Portugal'

    },
    {
        'name' : 'Katty Perry',
        'follower_count':94,
        'description':'Musician',
        'country':'United States'
    },
    {
        'name' : 'Kevin Hart',
        'follower_count':89,
        'description':'Comedian',
        'country':'United States'

    },
    {
        'name' : 'Kourtney',
        'follower_count':98,
        'description':'TV Personality',
        'country':'United States'


    },

    {
        'name' : 'Ellen Degenres',
        'follower_count':87,
        'description':'Comedian',
        'country':'United States'


    }

]

def choose(a,b):
    # print(f"First time a and b are {a} and {b}")
    if b != a:
        a = a
        #print(f"A is {a}")
        #print(f"B is {b}")
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print("######### AGAINST ########")
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
        return a['follower_count'],b['follower_count']
    else:
        b = random.choice(data)
        print("Both choices were same so re-ran now")
        # return choose(random.choice(data), b)
        return choose(a, b)
        # print(f"Second b is {b}")


def who_is_greater():
    continue_game = True
    count = 0
    while continue_game:
        a = random.choice(data)
        b = random.choice(data)
        c = choose(a, b)
        a_or_b = input("Who has more followers: Type 'A' or 'B': ")
        if a_or_b.lower() == 'a':
            if c[0] > c[1]:
                count += 1
                print(f"A ({a['name']}) followers are {a['follower_count']} which is greater than B's({a['name']}) {a['follower_count']}")
                print(f"You're right! Current score: {count}")
                previous_a = a
                a = b
                b = random.choice(data)
                while b != previous_a:
                    choose(a,b)
                else:
                    choose(a, random.choice(data))
            else:
                print(f"B ({b['name']}) followers are {b['follower_count']} which is greater than A's({b['name']}) {b['follower_count']}")
                print(f"Sorry, that's wrong. Final score: {count}")
                continue_game = False

        elif a_or_b.lower() == 'b':
            if c[1] > c[0]:
                count += 1
                print(f"B ({b['name']}) followers are {b['follower_count']} which is greater than A's({b['name']}) {b['follower_count']}")
                print(f"You're right! Current score: {count}")
                previous_a = a
                a = b
                b = random.choice(data)
                while b != previous_a:
                    choose(a,b)
                else:
                    choose(a, random.choice(data))
            else:
                # print("A followers are greater than B")
                print(f"A ({a['name']}) followers are {a['follower_count']} which is greater than B's({a['name']}) {a['follower_count']}")
                print(f"Sorry, that's wrong. Final score: {count}")
                continue_game = False


who_is_greater()

#print(type(choose(random.choice(data),random.choice(data))))
#print(choose(random.choice(data),random.choice(data)))
#print(choose(random.choice(data),random.choice(data))[0])
#print(choose(random.choice(data),random.choice(data))[1])





# Higher Lower Game

'''
from itertools import count

# Take Two Numbers A and B, Compare, If B > A, Continue the game and A becomes B,
# and B becomes a new number C
import random
data = [
    {
        'name' : 'Instagram',
        'follower_count':346,
        'description':'Social Media Platform',
        'country':'United States'

    },
    {
        'name' : 'Cristiano Ronaldo',
        'follower_count':215,
        'description':'Footballer',
        'country':'Portugal'

    },
    {
        'name' : 'Katty Perry',
        'follower_count':94,
        'description':'Musician',
        'country':'United States'
    },
    {
        'name' : 'Kevin Hart',
        'follower_count':89,
        'description':'Comedian',
        'country':'United States'

    },
    {
        'name' : 'Kourtney',
        'follower_count':98,
        'description':'TV Personality',
        'country':'United States'


    },

    {
        'name' : 'Ellen Degenres',
        'follower_count':87,
        'description':'Comedian',
        'country':'United States'


    }

]
a = random.choice(data)
print(a['name'])
b = random.choice(data)
print(b['name'])

def play(a, b):
    count = 0

    if a != b:
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print("######### AGAINST ########")
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        a_or_b = input("Who has more followers: Type 'A' or 'B': ")
        if a_or_b.lower() == 'a':
            if a['follower_count'] > b['follower_count']:
                count += 1
                print(f"You're right! Current score: {count}")
                c = a
                a = b
                b = random.choice(data)
                if b == c:
                    b = random.choice(data)
                print("############ NEXT ROUND ###########")
                play(a,b)
            else:
                print(f"Sorry, that's wrong. Final score: {count}")
        elif a_or_b.lower() == 'b':
            if b['follower_count'] > a['follower_count']:
                count += 1
                print(f"You're right! Current score: {count}")
                c = a
                a = b
                b = random.choice(data)
                if b == c:
                    b = random.choice(data)
                print("############ NEXT ROUND ###########")
                play(a, b)
            else:
                print(f"Sorry, that's wrong. Final score: {count}")



    else:
        a = random.choice(data)
        b = random.choice(data)
        play(a,b)

play(a, b)

'''
'''
a = random.choice(data)
print(a['name'])
b = random.choice(data)
print(b['name'])
count = 0

def play(a, b, count):

    if a != b:
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print("######### AGAINST ########")
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        a_or_b = input("Who has more followers: Type 'A' or 'B': ")
        if a_or_b.lower() == 'a':
            if a['follower_count'] > b['follower_count']:
                count += 1
                print(f"You're right! Current score: {count}")
                a = b
                b = random.choice(data)
                print("############ NEXT ROUND ###########")
                play(a,b, count)
            else:
                print(f"Sorry, that's wrong. Final score: {count}")
        elif a_or_b.lower() == 'b':
            if b['follower_count'] > a['follower_count']:
                count += 1
                print(f"You're right! Current score: {count}")
                a = b
                b = random.choice(data)
                print("############ NEXT ROUND ###########")
                play(a, b, count)
            else:
                print(f"Sorry, that's wrong. Final score: {count}")



    else:
        a = random.choice(data)
        b = random.choice(data)
        count = 0
        play(a,b, count)


play(a, b, count)

'''

'''
def play():
    num1 = random.randint(0, len(data) - 1)
    num2 = random.randint(0, len(data) - 1)
    print(data[num1], data[num2])
    count = 0
    while num2 != num1:
        print(f"Compare A: {data[num1]['name']}, a {data[num1]['description']}, from {data[num1]['country']}")
        print("######### AGAINST ########")
        print(f"Compare B: {data[num2]['name']}, a {data[num2]['description']}, from {data[num2]['country']}")
        a_or_b = input("Who has more followers: Type 'A' or 'B': ")
        if a_or_b.lower() == 'b':
            if data[num2]['follower_count'] > data[num1]['follower_count']:
                num3 = num2
                count += 1
                print(f"You're right! Current score: {count}")
            play()
        else:
            print(f"Sorry, that's wrong. Final score: {count}")
            break

    else:
        print("Choose New Number")
        num2 = random.randint(0, len(data) - 1)
'''
'''
def play():
    count = 0
    game = True
    while game:
        num1 = random.randint(0, len(data) - 1)
        num2 = random.randint(0, len(data) - 1)
        while num2 != num1:
            print(f"Compare A: {data[num1]['name']}, a {data[num1]['description']}, from {data[num1]['country']}")
            print("######### AGAINST ########")
            print(f"Compare B: {data[num2]['name']}, a {data[num2]['description']}, from {data[num2]['country']}")
            a_or_b = input("Who has more followers: Type 'A' or 'B': ")

            if a_or_b.lower() == 'b':
                if data[num2]['follower_count'] > data[num1]['follower_count']:
                    num3 = num2
                    count += 1
                    print(f"You're right! Current score: {count}")
                    play()
            else:
                print(f"Sorry, that's wrong. Final score: {count}")
                game = False
                break

        else:
            print("Choose New Number")
            num2 = random.randint(0, len(data) - 1)

'''
'''
        if a_or_b.lower() == 'a':
            if data[num1]['follower_count'] > data[num2]['follower_count']:
                print(f"Sorry, that's wrong. Final score: {count}")
                game = False
        elif a_or_b.lower() == 'b':
            if data[num1]['follower_count'] > data[num2]['follower_count']:
                count += 1
                print(f"You're right! Current score: {count}")
                play()
'''

"""
"""
# Coffee Machine

MENU = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappucino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def calculate_money(q,d,n,p):
    q = q*0.25
    d = d*0.1
    n= n*0.05
    p = p*0.01
    total = q + d + n + p
    print(f"Total money you gave: {total}")
    return total

def make_coffee(coffee_type, money,water=None, milk=None, coffee=None):
    global resources
    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']
    change_amount = money

    if coffee_type.lower() == 'latte' or coffee_type.lower() == 'l':
        water_left = water_left - MENU['latte']['ingredients']['water']
        milk_left = milk_left - MENU['latte']['ingredients']['milk']
        coffee_left = coffee_left - MENU['latte']['ingredients']['coffee']
        print(f"Water Left {water_left}, Milk Left {milk_left}, Coffee Left {coffee_left}")
        #change_amount = change_amount - MENU['latte']['cost']
        #print(f"Change Amount is {change_amount}")
    elif coffee_type.lower() == 'espresso' or coffee_type.lower() == 'e':
        water_left = water_left - MENU['espresso']['ingredients']['water']
        milk_left = milk_left
        coffee_left = coffee_left - MENU['espresso']['ingredients']['coffee']
        print(f"Water Left {water_left}, Milk Left {milk_left}, Coffee Left {coffee_left}")
        #change_amount = change_amount - MENU['latte']['cost']
        #print(f"Change Amount is {change_amount}")
    elif coffee_type.lower() == 'cappucino' or coffee_type.lower() == 'c':
        water_left = water_left - MENU['cappucino']['ingredients']['water']
        milk_left = milk_left - MENU['cappucino']['ingredients']['milk']
        coffee_left = coffee_left - MENU['cappucino']['ingredients']['coffee']
        print(f"Water Left {water_left}, Milk Left {milk_left}, Coffee Left {coffee_left}")
    else:
        print(f"Water Left {water_left}, Milk Left {milk_left}, Coffee Left {coffee_left}")
        #print(f"Change Amount is {change_amount}")
        #print(f"Water Left {resources['water']}, Milk Left {resources['milk']}, Coffee Left {resources['coffee']}")
        #print(f"Game Over, Left water is {water_left}")

    resources['water'] = water_left
    resources['milk'] = milk_left
    resources['coffee'] = coffee_left
    #print(f"Change Amount is {change_amount}")
    # print(f"Water Left {resources['water']}, Milk Left {resources['milk']}, Coffee Left {resources['coffee']}")
    return (water_left, milk_left, coffee_left)


continue_game = True
while continue_game:
    coffee_type = input("Which Coffee? ")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    make_coffee(coffee_type, money = calculate_money(quarters,dimes,nickels,pennies))
    next_game = input("Next Game? ")
    if next_game.lower() == 'y':
        continue_game = True
    elif next_game.lower() == 'n':
        make_coffee('q', None)
        continue_game = False
"""
"""
# Quiz game

question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

number= 0
score = 0
false = ''
true = ''

for i in question_data:
    text = i['text']
    answer = i['answer']
    number += 1
    print(f"Q{number} is: {text} (True/False)")
    check = input()
    '''
    if check.lower() == 't':
        check = 'True'
    elif check.lower() == 'f':
        check = 'False'
    '''
    if (check in ['t', 'T', 'true', 'True'] and answer == 'True') or (check in ['f', 'F', 'false', 'False'] and answer == 'False'):
    #if check == answer:
        score +=1
        print(f"You got it right!\nThe correct answer was {answer}\nYour Current Score {str(score)}/{str(number)}")
    else:
        print(f"You got it wrong!\n The correct answer was {answer}\nYour Current Score {str(score)}/{str(number)}")

"""

# Turtle

#from turtle import Turtle, Screen
import time

#tim = Turtle()
#screen = Screen()
#screen.exitonclick()
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "gray",
    "brown", "cyan", "magenta", "lime", "teal", "olive", "maroon", "navy", "silver", "gold",
    "lightgray", "darkgray", "lightgreen", "lightblue", "lightyellow", "lightpink", "turquoise",
    "violet", "indigo", "beige", "coral", "khaki", "orchid", "sienna"] # "white"

"""
# Draw Different Shapes with different colors
'''
no_of_sides = 3

for i in range(6):
    for j in range(no_of_sides):
        angle = 360 / no_of_sides
        tim.forward(100)
        time.sleep(1)
        tim.left(angle)
        time.sleep(1)
    no_of_sides += 1
    tim.color(random.choice(colors))
    
    # Draw Dashed Line
   #timmy.penup()
   #timmy.forward(20)
   #timmy.pendown()
   #time.sleep(2)
    # timmy.left(90)

'''
'''
# Random Walk
#tim = t.Turtle()
#t.colormode(255)
choice = [tim.left(random.choice([0,90,180,270])), tim.right(random.choice([0,90,180,270]))]#, tim.distance(random.randint(0,15),random.randint(0,15)),tim.setx(random.randint(0,15)), tim.sety(random.randint(0,15))]


for _ in range(200):
    tim.width(5)
    tim.forward(15)
    tim.setheading(random.choice([0,90,180,270]))
    #tim.forward(15)
    tim.color(random.choice(colors))
    time.sleep(1)
'''
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "white", "gray",
    "brown", "cyan", "magenta", "lime", "teal", "olive", "maroon", "navy", "silver", "gold",
    "lightgray", "darkgray", "lightgreen", "lightblue", "lightyellow", "lightpink", "turquoise",
    "violet", "indigo", "beige", "coral", "khaki", "orchid", "sienna"
]
# Spirograph
angle = 0
for i in range(360):
    tim.speed('fastest')
    tim.circle(50)
    angle += 1
    print(angle)
    tim.left(angle)
    tim.color(random.choice(colors))
"""
'''
# 10 by 10 dot drawing
for j in range(8):
    tim.right(90)
    for i in range(8):
        tim.speed(0)
        tim.circle(5)
        tim.color(random.choice(colors))
        tim.penup()
        tim.forward(30)
        tim.pendown()
        tim.circle(5)
    tim.left(90)
    tim.penup()
    tim.forward(30)
    tim.pendown()
    tim.circle(5)
    tim.left(90)
    time.sleep(3)
    
    
for i in range(3):
    tim.speed(0)
    tim.dot(5, random.choice(colors))
    tim.penup()
    tim.forward(30)
    tim.pendown()
    tim.setheading(90)
    time.sleep(2)
    tim.forward(30)
    tim.setheading(180)
'''
'''
# Etch a Sketch
tim.speed(0)
def move_forward():
    tim.forward(10)
def move_backward():
    tim.back(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.reset()
def undo():
    tim.undo()
def space():
    tim.penup()
def pendown():
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clear, "c")
screen.onkey(undo, "u")
screen.onkey(space, "space")
screen.onkey(pendown, "m")

screen.exitonclick()
'''
"""
# Turtle Race

t_list = ['t1', 't2', 't3', 't4']

def move_forward():
    return random.randint(1,300)

y_cord = 100

for t in range(0, 4):
    t_list[t] = Turtle(shape='turtle')
    t_list[t].speed(0)
    t_list[t].color(colors[t])
    t_list[t].penup()
    t_list[t].setx(-250)
    t_list[t].sety(y_cord)
    y_cord -= 50

s1 = s2= s3 =s4 = 0

for i in range(3):
    r1 = move_forward()
    t_list[0].forward(r1)
    s1 = s1 + r1
    r2 = move_forward()
    t_list[1].forward(r2)
    s2 = s2 + r2
    r3 = move_forward()
    t_list[2].forward(r3)
    s3 = s3 + r3
    r4 = move_forward()
    t_list[3].forward(r4)
    s4 = s4 + r4


'''
for i in range(1):
    for j in t_list:
        r1 = move_forward()
        j.forward(r1)
        s1 = s1 + r1
        r2 = move_forward()
        s2 = s2 + r2
        r3 = move_forward()
        j.forward(r3)
        s3 = s3 + r3
        r4 = move_forward()
        j.forward(r4)
        s4 = s4 + r4

'''

print(f"Turtle1 final distance is {s1}")
print(f"Turtle2 final distance is {s2}")
print(f"Turtle3 final distance is {s3}")
print(f"Turtle4 final distance is {s4}")
k = []
k.append(s1)
k.append(s2)
k.append(s3)
k.append(s4)
print(k)


if k.index(max(s1, s2, s3, s4)) == 0:
    print(f"Winner is Turtle1")
elif k.index(max(s1, s2, s3, s4)) == 1:
    print(f"Winner is Turtle2")
elif k.index(max(s1, s2, s3, s4)) == 2:
    print(f"Winner is Turtle3")
elif k.index(max(s1, s2, s3, s4)) == 3:
    print(f"Winner is Turtle4")

screen.exitonclick()


'''
t1 = Turtle()
t1.color('yellow')
t1.shape('turtle')
t1.penup()
t1.setx(-250)
t1.sety(50)
#t1.setheading(160)
#t1.forward(215)
#t1.left(200)
t2 = Turtle()
t2.color('red')
t2.shape('turtle')
t2.penup()
t2.setx(-250)
#t2.setheading(180)
#t2.forward(200)
#t2.left(180)
t3 = Turtle()
t3.color('blue')
t3.shape('turtle')
t3.penup()
t3.setx(-250)
t3.sety(-50)
t4 = Turtle()
t4.color('green')
t4.shape('turtle')
t4.penup()
t4.setx(-250)
t4.sety(-100)

class MOVE:
    def __init__(self):
        random.randint(1,3)

for i in range(300):
    t1.forward(random.randint(1,2))
    t2.forward(random.randint(1, 2))
    t3.forward(random.randint(1, 2))
    t4.forward(random.randint(1, 2))
'''

"""
""""""
# SNAKE GAME
from turtle import Turtle, Screen
import time
screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#starting_positions = [(0,0),(-20,0),(-40,0)]
#like = -40
ALIGNMENT = 'center'
FONT = ("Arial",8,"normal")
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments =[]
        #self.head = self.segments[0]
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("blue")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.refresh()
        #self.shapesize(0.5)

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score is {self.score} High Score: {self.high_score}",align= ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()




#snake = Snake()
'''
class Actions:
    def move_forward(self):
        turt.forward(10)
    def move_backward(self):
        turt.back(10)
    def move_left(self):
        turt.left(10)
    def move_right(self):
        turt.right(10)
    def clear(self):
        turt.clear()
        turt.reset()
    def undo(self):
        turt.undo()
    def space(self):
        turt.penup()
    def pendown(self):
        turt.pendown()

turt = Turtle()

actions = Actions()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(actions.clear, "c")
screen.onkey(actions.undo, "u")
screen.onkey(actions.space, "space")
screen.onkey(actions.pendown, "m")
'''
'''
screen.listen()
screen.onkey(actions.move_forward, "Up")
screen.onkey(actions.move_backward, "Down")
screen.onkey(actions.move_right, "Right")
screen.onkey(actions.move_left, "Left")
screen.onkey(actions.clear, "c")
screen.onkey(actions.undo, "u")
screen.onkey(actions.space, "space")
screen.onkey(actions.pendown, "m")
'''
'''

def move_forward():
    tim.forward(10)
def move_backward():
    tim.back(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.reset()
def undo():
    tim.undo()
def space():
    tim.penup()
def pendown():
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clear, "c")
screen.onkey(undo, "u")
screen.onkey(space, "space")
screen.onkey(pendown, "m")
'''
#segments = []
'''
for i in starting_positions:
    turt = Turtle(shape="square")
    turt.penup()
    turt.color("blue")
    turt.goto(i)
    segments.append(turt)
'''

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        screen.title(f"Score is: {scoreboard.score}")
        scoreboard.update_scoreboard()
        scoreboard.increase_score()
        snake.extend()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        # print("You hit the Wall, Game Over!")
        # game_is_on = False
        # scoreboard.game_over()

    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            print("You hit the Tail, Game Over!")
            game_is_on = False
            scoreboard.reset()
            #scoreboard.game_over()
    '''
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            print("You hit the Tail, Game Over!")
            game_is_on = False
            scoreboard.game_over()
    '''



'''
while game_is_on:
    screen.update()
    #for seg_num in range(start=2, stop=0, step=-1):
    #for seg_num in range(2, 0,-1):
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
        '''
'''    
    for seg_num in segments:
        new_x = segments[-1].xcor()
        new_y = segments[-1].ycor()
        seg_num.goto(new_x,new_y)
'''
'''
    segments[0].forward(20)
    segments[0].left(90)

    #for seg in segments:
    #    seg.forward(20)
        #screen.update()
'''


screen.exitonclick()

"""
# PING PONG

from turtle import Turtle, Screen
screen = Screen()
screen.screensize(800, 600, "black")
#screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
#score1 = score2 =0

class Paddle(Turtle):
    def __init__(self, poistion):
        super().__init__()
        self.shape("square")
        #self.paddle = Turtle("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(poistion)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        #self.r_paddle_score = 0
        #self.l_paddle_score = 0
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1
        #self.setheading(90)
        #self.forward(10)
        #self.setheading(ball.START_ORIENTATION + 90)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def rest_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 45, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 45, "normal"))

    def l_point(self):
        #self.clear()
        self.l_score +=1
        self.write(self.l_score, align="center", font=("Courier", 45, "normal"))
        self.update_scoreboard()
        #screen.update()

    def r_point(self):
        #self.clear()
        self.r_score +=1
        self.write(self.r_score, align="center", font=("Courier", 45, "normal"))
        self.update_scoreboard()
        #screen.update()


'''

paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(280,0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

'''
l_paddle = Paddle((-280, 0))
r_paddle = Paddle((280, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    #time.sleep(ball.move_speed*0.9)
    #time.sleep(ball.move_speed - 0.01 while ball.move_speed> 0)
    screen.update()
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()> 240 or ball.distance(l_paddle) < 50 and ball.xcor()< -240:
    #if r_paddle.distance(ball) < 50 and ball.xcor()> 240:
        ball.bounce_x()

    # Detect R Paddle Miss
    if ball.xcor() > 300:
        ball.rest_position()
        scoreboard.l_point()
        #scoreboard.l_score += 1
        #ball.l_paddle_score += 1
        #ball.write(f"Left Score {ball.l_paddle_score}")
        screen.update()

    # Detect L Paddle Miss
    if ball.xcor() < -300:
        ball.rest_position()
        scoreboard.r_point()
        #scoreboard.r_score +=1
        #ball.r_paddle_score += 1
        #ball.write(f"Right Score {ball.r_paddle_score}")
        screen.update()

''' 
class Actions:

    def __init__(self, turt):
        self.turt = turt
    def up(self):
        self.turt.setheading(90)
        self.turt.forward(10)
    def down(self):
        self.turt.setheading(270)
        self.turt.forward(10)

bat1 = Turtle("square")
bat1.speed(0)
bat1.shapesize(2)
bat1.penup()
bat1.goto(-280, 0)
action = Actions(bat1)
screen.listen()
screen.onkey(action.up, "Up")
screen.onkey(action.down, "Down")

ball = Turtle("circle")
ball.shapesize(0.5)
ball.speed('slowest')
ball.penup()

def move_back():
    ball.goto(260,-260)

x = True
while x:
    if bat1.distance(ball) > 100:
        ball.goto(-280, random.randint(-260, 260))
    elif bat1.distance(ball) < 100:
        move_back()
    if ball.xcor() < -260:
        score2 += 1
        ball.write(f"Score2: {score2}",align= "Left", font=("Arial",24,"normal"))
        screen.update()

'''

screen.exitonclick()

"""
"""
from turtle import Turtle, Screen
screen = Screen()

# Turtle Cross

class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(random.randint(-240, 240), random.randint(-240, 240))
        self.continous_move = 10
        #self.move()

    def move(self):
        new_x= self.xcor() + self.continous_move #self.increment()
        self.goto(new_x,self.ycor())

    def increment(self):
        self.continous_move += 10

    '''
    # #def increment(self):
    #     for i in range(50):
    #         self.continous_move += 10'''

class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -240)
        self.setheading(90)
        self.speed(0)
    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

class PrintOnScreen(Turtle):
    def __init__(self,print_statement):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("Red")
        self.goto(-80, 220)
        self.write(print_statement,font=("Arial", 20, "normal"))



tim = Tim()

screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.move_right, "Right")
screen.onkey(tim.move_left, "Left")

blocks = []  # List to store all blocks

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    new_block = Blocks()
    blocks.append(new_block)
    '''
    # Chance to create a new block
    #if random.randint(1, 2) == 1:   # Roughly every 2 frames
    #    new_block = Blocks()
    #    blocks.append(new_block)
    '''
    # Move all blocks
    for block in blocks:
        block.move()

        if block.distance(tim) < 15:
            print_on_screen = PrintOnScreen("Game Over!")
            game_is_on = False



    screen.update()


screen.exitonclick()

'''
    frame_count += 1
    if frame_count % 50 == 0:
        blocks.increment()
'''
"""