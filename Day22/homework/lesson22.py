#შექმენით range-ის კოპიო ფუნქცია - my_range. მას გადაეცემა start, end, step. ფუნქციაში შემდეგ შექმენით სია, სადაც გექნებათ start-სა და end-ს შორის არსებული რიცხვები, გაითვალისიწინეთ step. არ გამოიყენოთ range()

# def my_range(start, stop, step):
#     while start < stop:
#         start += step
#         print(start)
        
# my_range(20, 40, 2)


#დავალება2: შექმენით ფუნქცია სახელად my_filter, რომელსაც გადაეცემა ერთი სია და სიმბოლო, რომელიც სიიდან ამოიშლება. საბოლოოდ დააბრუნეთ სია, სადაც არ იქნება არც ერთი ეს სიმბოლო








#დავალება3: შექმენით ფუნქცია, რომელსაც გადაეცემა სია. თქვენი დავალებაა, რომ ამ სიის დადებითი რიცხვების ნამრავლი დააბრუნოთ


# def product_of_positive_numbers(lst):
#     product = 1
#     for num in lst:
#         if num > 0:
#             product *= num
#     return product


# numbers = [32, -29, -12, 85, 64, 86, -79, 100]
# result = product_of_positive_numbers(numbers)
# print("Product of positive numbers:", result)




#დავალება4: შექმენით ფუნქცია სახელად greet, რომელსაც გამოძახებისას გადასცემთ მომხმარებლის სახელს - დაბეჭდავს "Welcome მომხმარებლის სახელი აქ!".



# def welcome(name):
#     print("hello", name)

# welcome('Gio')






#დავალება5: შექმენით ფუნქცია, რომელსაც გადაეცემა ერთი სია. ამ სიაში უნდა გაიგოთ კენტი რიცხვების ჯამი. საბოლოოდ კი მიღებული შედეგი გამოიყენეთ ფუნქციის გარეთ, მიუმატეთ 5 და დაბეჭდეთ

def sum_odd_number(numbers):
    odd_sum = 0
    for number in numbers:
        if number % 2 != 0:
            odd_sum += number
            return odd_sum
        

print(sum_odd_number([1,2,3,4,5,6,7,8,9,10])+5)        