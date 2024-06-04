#https://www.codewars.com/kata/558fc85d8fd1938afb000014


# def sum_two_smallest_numbers(numbers):
   
#     sorted_numbers = sorted(numbers)
   
#     return sorted_numbers[0] + sorted_numbers[1]


# numbers = [5, 8, 12, 18, 22]
# print(sum_two_smallest_numbers(numbers))




#https://www.codewars.com/kata/5aba780a6a176b029800041c



# def max_multiple(divisor, bound):
#     return bound - (bound % divisor)


# divisor = 3
# bound = 10
# print(max_multiple(divisor, bound)) 



#  https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9


# def row_weights(array):
#     row1_weight = 0
#     row2_weight = 0
#     for i, weight in enumerate(array):
#         if i % 2 == 0:  
#             row1_weight += weight
#         else:
#             row2_weight += weight
#     return row1_weight, row2_weight