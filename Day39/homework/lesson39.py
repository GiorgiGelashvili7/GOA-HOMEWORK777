#https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python


# def narcissistic(value):
#     num_digits = len(str(value))
#     total = 0
#     for digit in str(value):
#         total += int(digit) ** num_digits
#     return total == value

#https://www.codewars.com/kata/514b92a657cdc65150000006/train/python


# def solution(number):
    # return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


#https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python


# def find_odd(arr):
#     counts = {}
#     for num in arr:
#         counts[num] = counts.get(num, 0) + 1
#     for num, count in counts.items():
#         if count % 2 != 0:
#             return num


#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

# def duplicate_encode(word):
#     word = word.lower()
#     encoded = ''
#     for char in word:
#         if word.count(char) > 1:
#             encoded += ')'
#         else:
#             encoded += '('
#     return encoded