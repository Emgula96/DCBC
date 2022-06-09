
# nums = [1,2,-2,-5,-7,3,4,5,6,7,8]

# print(sum(nums))

# print(nums[-1]) or print(nums.sort()) -->

# print(nums[0]) or print(nums.sort())

# for i in nums:
#     if i%2 == 0:
#         print(i)

# for item in nums:
#     if item % 2 ==0:
#         print(item, end=" ")


# 
# for i in nums:
#     if i > 0:
#  print(i)

# list2 = []
# for i in nums:
#     if i >= 0:
#         list2.append(i)
# print(list2)


#multiply a list

# num2 = [1, 2, 3, 4, 5, 6]

# multipliedList = [item * 2 for item in num2]
# print(multipliedList)



# nums.reverse()
# print(nums)

# reverse = nums[::-1]
# print (reverse)



# Square the numbers in this list
numbers = [1, 2, 3, 4, 5, 6, 7]
# Output [1, 4, 9, 16, 25, 36, 49]

# multipliedList = [item * 2 for item in numbers]
# print (multipliedList)

# Remove all empty strings in this list
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# output ["Mike", "Emma", "Kelly", "Brad"]

# while "" in list1:
#     list1.remove ("")
# print(list1)


# Add new item to list after a specified item
list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# output [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]


list2[2][2].append(7000)
print(list2)
# Replace list's item with new value if found
list3 = [5, 10, 15, 20, 25, 50, 20]
# output [5, 10, 15, 200, 25, 50, 20]


# list3[1] = 15
# print(list3)

# Remove all occurrences of a specific item from a list.
list4 = [5, 20, 15, 20, 25, 50, 20]
# output [5, 15, 25, 50]

# while 20 in list4: list4.remove(20)
# print(list4)


# for item in list4:
#     if item == 20:
#         list4.remove(20)
# print(list4)


# nums = [2, 7, 11, 15]

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             result = nums[i]+nums[j]
#             if result == target:
#                 return [i,j]
#     return []

# print(twoSum(nums,26))