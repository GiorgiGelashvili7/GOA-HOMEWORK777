# numbers = [3,6,-1,2,8,9,4,5,7,-2]

# max_number = numbers[0]

# for number in numbers:
#     if max_number < number:
#         max_number = number

# print(max_number)

# def my_range(start, end, step = 1):
#     numbers = [start]

#     counter = start

#     # if end < start and step >= 0:
#     #     return [start,end]

#     # for num in numbers:
#     #     counter = counter + step
#     #     if counter == end:
#     #         return numbers
#     #     numbers.append(counter)

# print(my_range(10,0))

numbers = []

for i in range(12, 50 + 1, 4):
    numbers.append(i)

# Second Part

reversed_list = []

for index in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[index])

print(numbers)
print(reversed_list)