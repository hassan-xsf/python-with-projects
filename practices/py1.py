# # Sqrs of numbers using python

# nums = [1,2,3,4,5]

# for i in nums: 
#     print(i ** 2)


# # Calculator using python

# firstNum = 10
# secondNum = 25

# operand = "/"

# if operand == "/": 
#     print(f"The division of {firstNum} with {secondNum} is {firstNum / secondNum}")
# elif operand == "*": 
#     print(f"The multiplication of {firstNum} with {secondNum} is {firstNum * secondNum}")
# elif operand == "+": 
#     print(f"The sum of {firstNum} with {secondNum} is {firstNum + secondNum}")
# elif operand == "-": 
#     print(f"The difference of {firstNum} with {secondNum} is {firstNum + secondNum}")
# else:
#     print("Invalid operand found!")


# # reverse a string in python

# theString = "This is a string that must be reversed"

# for s,i in enumerate(theString):
#     print(f"{s} and {i}")


# numbers = [1,2,3,4,5,6,7]


# evenList = filter(lambda x: x % 2 == 0 , numbers)
# print(list(evenList))


# # Creating a list from range

# nums = [n for n in range(5)]

# # Squaring a list from the range

# nums = [n ** 2 for n in nums]

# nums = [n for n in nums if n % 2 == 0]

# print(nums)

# Handling 2D Lists

# lists = [[1, 2], [3, 4], [5, 6]]


# # flattened = []
# # for x in lists:
# #     for y in x:
# #         flattened.append(y)

# flattened = [y for x in lists for y in x]

# print(flattened)

# # Combining two iterables

# list1 = [1, 2]
# list2 = [3, 4]


# list = [[x,y] for x in list1 for y in list2]
# print(list)


# Practice 1:
# Create a list of squares of all odd numbers between 1 and 20 (inclusive).


squares = [n ** 2 for n in range(1 , 20) if n % 2 == 1]

print(squares)


# Practice 2:
# From the list words = ["apple", "banana", "cherry", "date"], create a new list that contains only the words with more than 5 characters.

lists = ["apple", "banana", "cherry", "date"]

lists = [x for x in lists if len(x) > 5]
print(lists)



# Practice 3:
# Given a list of tuples coordinates = [(1, 2), (3, 4), (5, 6)], create a new list that contains the sum of each pair of coordinates (e.g., 1+2, 3+4, etc.).


tuples = [(1, 2), (3, 4), (5, 6)]

sumOfTuples = [(x+y) for pair in tuples for x,y in [pair]]

print(sumOfTuples)



