
# import time

# def timingCalculator(func):
#     def wrapper(*args , **kargs):
#         start_time = time.time()
#         result = func(*args , **kargs)
#         end_time = time.time();
#         print(f"The function took {end_time - start_time:.3f}")
#         return result

#     return wrapper


# @timingCalculator
# def sum(num1, num2):
#     time.sleep(2)
#     print(f"The sum of {num1} + {num2} is {num1+num2}")


# sum(50, 500)