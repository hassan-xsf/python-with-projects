

# def linear_search(numbers, target):
#     return next((i for i , x in enumerate(numbers) if x == target), -1)



# # Test the function
# numbers = [1, 2, 3, 4, 5]
# target = 2
# result = linear_search(numbers, target)
# print(result)  # Output: 2 (Index of 3)

def binary_search(numbers , target):
    l = 0
    r = len(numbers) - 1
    while l <= r:
        m = (r + l) // 2
        if numbers[m] > target:
            r = m - 1
        elif numbers[m] < target:
            l = m + 1
        else:
            return m
    return -1

# Test the function
sorted_numbers = [1, 2, 3, 4, 5]
target = 4
result = binary_search(sorted_numbers, target)
print(result)  # Output: 3 (Index of 4)