#დავალება: შექმენით პროგრამა სადაც ბოლოდან პირველ ოთხის ჯერად რიცხვს გამოიტანთ სიიდან, მაგ სიაში კი რიცხვები უნდა იყოს 10 დან 50 -ის ჩათვლით 

numbers = []

for i in range(10,50 + 1):
    numbers.append(i)


def func(numbers):
    for index in range(len(numbers) -1, -1, -1):
        if numbers[index] % 4 == 0:
            return numbers[index]
        

print(func(numbers))        
