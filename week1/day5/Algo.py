# // Write a function that takes in a string of lowercase letters
# // and returns the index of the string's first non-repeating character.
# // If the input string does not have any non-repeating characters,
# // your function should return -1.



import re


letters = 'bbacb'
# counter = {}

# for letter in letters:
#     if letter not in letters:
#         counter[letter] = 0
#     counter[letter] += 1
#     for key in counter:
    


# print(counter)

# def repeating(string):
#     counter= {}
#     for char in string:
#         counter[char] = counter.get(char,0) +1
#     for char in counter:
#         if counter[char] == 1:
#             index = list(string).index(char)
#             print(index)
#             return print(char + ' is the first nonrepeating character and is at index')
#     return print('-1')

# repeating(letters)


# def firstnonrepeat(string):
# hash = {}
# for letter in string:
#     if letter not in hash:
#         hash[letter] = 0
#         hash[letter]


redList = [5,5,3,9,2]
blueList = [3,6,7,2,1]
blueRed = []
anotherList = 0

def maxSpeed(redList, blueList, anotherList):
    for i in range(len(redList)):
        blueRed = redList + blueList
        anotherBlueandRed = sorted(blueRed)
        anotherBlueandRed.reverse()
    for i in range(len(redList)):
        anotherList = anotherList + anotherBlueandRed[i]
    print(anotherList)
maxSpeed(redList, blueList, anotherList)

# def minSpeed(redList,blueList,anotherList):



list1 =[1,2,3,4]
list2 = [2,3,7,8]

def tandem(list1,list2, fastest):
    list1 =[1,2,3,4]
    list2 = [2,3,7,8]
    speed = []
            #8732
    if fastest:
        list2.reverse()
    for i in range(len(list1)):
        #val = list1[i]
        #val2 = list2[i]
        if list1[i] > list2[i]:
            speed.append(list1[i])
        if list1[i] == list2[i]:
            speed.append(list1[i])
        if list1[i] < list2[i]:
            speed.append(list2[i])
    return sum(speed)

