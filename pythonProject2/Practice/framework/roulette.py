import statistics
from statistics import mode
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter,OrderedDict

import pylab as pl

all_numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5,
               24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

drawn_numbers = [28,33,13,5,25,35,12,4,0,4,10,36,27,34,12,36,13,14,32,10,7,0,24,27,21,1,3,4,25,9,5,16,31,11,34,23,13,17,15,26,29,29]

print('{} {}'.format("The length of list is",len(drawn_numbers)))
print('{}{}'.format("Counter list of drawn numbers is as follows: \n",Counter(drawn_numbers)))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# First Number should be that from which left turn starts


def run_all_numbers_left():
    all_list = []

    for i in range(0, len(drawn_numbers) - 1):
        difference = all_numbers.index(drawn_numbers[i + 1]) - all_numbers.index(drawn_numbers[i])
        if difference > 0:
            all_list.append(difference)
        else:
            all_list.append(37 + difference)
    print("All Run list is as follows:")
    print(all_list)
    print(len(all_list))
    print("Counter list of All is as follows: ")
    print(Counter(all_list))

    data = dict(Counter(all_list))
    number_drawn= list(data.keys())
    frequency = list(data.values())
    plt.figure(figsize=(11, 3))
    plt.bar(number_drawn,frequency)
    x = np.arange(0, 38, 1)
    plt.xticks(x)
    plt.xlabel("Gap")
    plt.ylabel("Frequency of Gap")
    plt.title("Gap analysis of All Run")
    # mng = plt.get_current_fig_manager()
    # mng.full_screen_toggle()
    plt.show()

    sort_dict = dict(Counter(all_list))
    new_dict = sorted(sort_dict.items(), key=lambda x:x[1], reverse=True)
    print("Sorted All Run list is: " + str(new_dict))

    j = 0
    secondary_list = all_list
    for i in secondary_list:
        if i == 21:
            print("{} {}".format("Index values of desired numbers are:", (secondary_list.index(i) + j)))
            j = j + 1
            secondary_list.remove(i)
    '''my_counter = Counter(all_list)
        i = 0
        while i < len(all_list):
            print(all_list[i], ":", my_counter[all_list[i]])
            i += 1'''
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return all_list


def run_numbers_left():
    all_list = []

    for i in range(1, len(drawn_numbers) - 1, 2):
        difference = all_numbers.index(drawn_numbers[i + 1]) - all_numbers.index(drawn_numbers[i])
        if difference > 0:
            all_list.append(difference)
        else:
            all_list.append(37 + difference)

    print("Left Run list is as follows:")
    print(all_list)
    print("Counter list of Left Runs is as follows: ")
    print(Counter(all_list))

    data = dict(Counter(all_list))
    number_drawn = list(data.keys())
    frequency = list(data.values())
    plt.figure(figsize=(11, 3))
    plt.bar(number_drawn, frequency)
    x = np.arange(0, 38, 1)
    plt.xticks(x)
    plt.xlabel("Gap")
    plt.ylabel("Frequency of Gap")
    plt.title("Gap analysis of Left Run")
    plt.show()


    sort_dict = dict(Counter(all_list))
    new_dict = sorted(sort_dict.items(), key=lambda x: x[1], reverse=True)
    print("Sorted Left Run list is: " + str(new_dict))

    j = 0
    secondary_list = all_list
    for i in secondary_list:
        if i == 21:
            print("{} {}".format("Index values of desired numbers are:", (secondary_list.index(i) + j)))
            j = j + 1
            secondary_list.remove(i)
    '''my_counter = Counter(all_list)
    i = 0
    while i < len(all_list):
        print(all_list[i], ":", my_counter[all_list[i]])
        i += 1'''
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    return all_list


def run_numbers_right():
    all_list = []

    for i in range(0, len(drawn_numbers) - 1, 2):
        difference = all_numbers.index(drawn_numbers[i]) - all_numbers.index(drawn_numbers[i + 1])
        if difference > 0:
            all_list.append(difference)
        else:
            all_list.append(37 + difference)

    print("Right Run list is as follows:")
    print(all_list)
    print("Counter list of Right Runs is as follows: ")
    print(Counter(all_list))

    data = dict(Counter(all_list))
    number_drawn = list(data.keys())
    frequency = list(data.values())
    plt.figure(figsize=(11, 3))
    plt.bar(number_drawn, frequency)
    x = np.arange(0, 38, 1)
    plt.xticks(x)
    plt.xlabel("Gap")
    plt.ylabel("Frequency of Gap")
    plt.title("Gap analysis of Right Run")
    plt.show()

    sort_dict = dict(Counter(all_list))
    new_dict = sorted(sort_dict.items(), key=lambda x: x[1], reverse=True)
    print("Sorted Right Run list is: " + str(new_dict))

    j = 0
    secondary_list = all_list
    for i in secondary_list:
        if i == 20:
            print("{} {}".format("Index values of desired numbers are:", (secondary_list.index(i) + j)))
            j = j + 1
            secondary_list.remove(i)
    '''my_counter = Counter(all_list)
        i = 0
        while i < len(all_list):
            print(all_list[i], ":", my_counter[all_list[i]])
            i += 1'''
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return all_list


# these functions will return the values of spaces/gap on the wheel between two consecutive numbers drawn


run_all_numbers_left()
run_numbers_left()
run_numbers_right()



'''
def left_run_analysis(list):
    left_list = list
    # print("Counter list is as follows: ")
    # print(Counter(left_list))
    
    for i in range(0, 37):
        # len(left_list)-left_list.count(max(set(list), key=left_list.count))-1
        print("The original list of Gap is: \n" + str(left_list))
        print("The most frequent number in the list of Gap is :" + str(mode(left_list)))
        print("The most frequent number appears: " + str(
            (left_list.count(max(set(list), key=left_list.count)))) + " times in the list")
        # print("The length of list of Gap is : " + str(len(left_list)))
        item = max(set(left_list), key=left_list.count)
        c = left_list.count(item)
        for j in range(c):
            left_list.remove(item)

        print("List after removing the most frequent gap: \n" + str(left_list))
        print(" Next Iteration ++++++++++++++++++++++++++++")


left_list = run_numbers_left()

if __name__ == "__main__":
    left_run_analysis(left_list)


'''
'''
def most_frequent(list):
    print("The most frequent number is :" + str(mode(list)))
    #return mode(list)
    print("The most frequent number appears: " + str((list.count(max(set(list),key= list.count)))) + "times")
    return max(set(list),key= list.count)




def remove_most_frequent(list, item):
    c = list.count(item)
    for i in range(c):
        list.remove(item)
    return list


if __name__ == "__main__":
    left_list = run_numbers_left()
    # most_frequent(left_list)
    item = most_frequent(left_list)
    print("The original list is: \n" +str(left_list))
    res = remove_most_frequent(left_list, item)
    print("List after removing the most frequent gap: \n" + str(res))


'''

'''

def concurrent(list):
    # left_list = run_numbers_left()
    for i in range(0, 2):
        def most_frequent(list):
            print("The most frequent number is :" + str(mode(list)))
            print("The most frequent number appears: " + str((list.count(max(set(list), key=list.count)))) + "times")
            return max(set(list), key=list.count)

        def remove_most_frequent(list, item):
            c = list.count(item)
            for i in range(c):
                list.remove(item)
            return list

        if __name__ == "__main__":
            left_list = run_numbers_left()
            # most_frequent(left_list)
            item = most_frequent(left_list)
            print("The original list is: \n" + str(left_list))
            res = remove_most_frequent(left_list, item)
            print("List after removing the most frequent gap: \n" + str(res))

            return concurrent(res)


if __name__ == "__main__":
    concurrent(left_list)
'''

'''
for i in range(0,9):
        print(drawn_numbers.index(i))
        print(drawn_numbers.index(i+1))
'''

# index_numbers = []
# for i in drawn_numbers:
# pass
# index_numbers.append(all_numbers.index(i) + 1)
# print(index_numbers)

'''
for i in drawn_numbers:
        print(all_numbers.index(i))
        print(all_numbers.index(i+1))
'''

# right_list = run_numbers_right()
# left_list = run_numbers_left()

# print(OrderedDict(sorted(Counter(all_list).items())))

'''
35,29,4,28,25,28,3,22,33,9,1,3,30,0,36,21,31,2,2,0,36,18,2,29,30,15,34,4,18,27,15,16,8,7,25,18,
                 24,3,6,17,3,23,12,9,29,10,8,26,23,26,0,35,2,3,25,16,3,36,24,10,2,22,13,0,36,21,7,15,1,29,
                 3,31,6,10,4,25,35,20,22,20,19,13,12,5,22,5,26,36,18,20,0,7,19,24,12,19,36,25,14,7,22,29,
                 1,25,13,5,7,36,1,17,23,33,0,36,12,19,10,36,30,7,23,12,21,4,33,16,12,24,30,3,12,0,34,32,
                 30,12,34,26,1,33,27,3,17,23,8,27,1,5,8,16,24,35,24,11,0,3,19,33,24,36,24,26,8,33,19,26,4,
                 19,4,12,32,14,11,20,8,31,20,2,15,16,9,15,24,8,11,16,16,25,30,6,2,2,9,17,7,17,19,10,19,15,
                 2,31,13,29,13,33,2,9,3,1,28,13,16,33,23,4,1,6,32,20,11,15,21,14,25,27,21,12,0,3,18,23,27,
                 4,34,36,7,1,3,24,0,28,13,3,4,2,36,19,10,4,33,34,24,13,10,3,3,24,29,25,4,18,9,18,11,34,28,
                 17,11,3,30,8,19,3,5,16,9,34,30,31,14,36,9,24,2,11,13,6,3,31,27,10,24,22,11,19,18,17,4,26,
                 8,0,8,3,22,19,27,27,29,14,3,19,1,35,16,8,22,19,22,3,23,11,20,2,8,9,0,21,26,15,2,33,11,19,35,
                 8,23,35,36,15,12,16,9,35,25,0]
                 
drawn_numbers = [3, 26, 29, 35, 5, 11, 20, 25, 6, 10, 12, 7, 23, 33, 7, 9, 1, 35, 25, 33, 27, 21, 28, 17, 5, 23, 32,
                 30, 36, 22, 3, 27, 21, 10, 9, 16, 15, 7, 1, 12, 30, 19, 31, 23, 33, 22, 12, 3, 8, 7, 15,
                 27, 25, 4, 22, 4, 1, 6, 9, 2, 2, 4, 18, 26, 21, 12, 26, 16, 30, 32, 11, 14, 10, 36, 16,
                 34, 8, 17, 20, 27, 0, 22, 30, 32, 24, 6, 7, 5, 29, 1, 8, 4, 23, 30, 5, 31, 16, 17, 2,
                 34, 35, 9, 27, 18, 3, 16, 23, 2, 27, 28, 33, 6, 31, 26, 5, 4, 14, 6, 27, 15, 27, 27, 1, 6, 23, 36, 1,
                 5, 31, 9, 6, 4, 7, 1, 18, 20, 11, 24, 25, 16, 26, 25, 5, 22, 1, 20, 35, 30, 10, 34, 36, 17, 25, 14, 16,
                 8, 29,
                 28, 20, 19, 6, 6, 34, 32, 15, 19, 36, 21, 16, 4, 18, 18, 9, 14, 27, 20, 0, 3, 11, 22, 17, 26, 15, 29,
                 35, 8, 20, 21, 30,
                 35, 30, 16, 29, 19, 24, 14, 30, 4, 21, 6, 22, 8, 32, 21, 24, 10, 29, 17, 8, 19, 33, 33, 6, 17,
                 26, 5, 18, 17, 27, 2, 9, 23, 29, 34, 23, 4, 28]

Adarsh
26,2,6,30,15,14,18,23,8,7,19,12,5,7,14,21,20,11,19,23,16,23,29,10,1,25,36,18,7,4,36,5,31,24,11,14,32,28

Vicky
33,3,29,2,30,17,7,34,27,30,7,14,20,0,12,18,20,19,0,4,22,27,30,32,36,18,16,9,15,10,36,29,24,15,27,15,24,15,36,22,34,19,22,9,1,5

'''

