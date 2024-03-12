# დავწეროთ პროგრამა, რომელიც ითვლის 10-დან 1-მდე, დაბეჭდავს თითოეულ რიცხვს და შემდეგ დაბეჭდავს "დრო ამოიწურა". 

# i = 10
# while i >= 0:
#     print(i)
#     i = i-1
#     print(time is up)

# დავწეროთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვებს განუწყვეტლივ, სანამ ისინი არ შეიყვანენ 0-ს.

# num = (input("please write number : "))

# lesson = 0

# if 1 > 0:
#     print("you enter the correct number")
# else:
#     print("write correctly")


#  დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. განაგრძეთ კითხვა, სანამ სწორი პაროლი არ იქნება შეყვანილი. დავუშვათ რომ სწორი პაროლი არის 12345678

# input("please write your password : ")

# password = 12345678

# if password == 12345678:
#     print("you are correct")
# elif password > 0:
#     print("the password's contains 8 number")    
# else: 
#     print("please write correctly")    
   

#დავწეროთ პროგრამა, რომელიც ბეჭდავს ყველა ლუწ რიცხვს 0-დან 20-მდე 

# i = 0

# for i in range(0,20 + 1):
#    if i%2==0:
#       print(i)

# შევამოწმოთ ლუწია თუ კენტი: დავწეროთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს და ბეჭდავს ლუწია თუ კენტი

# age = (input("write your age : "))
# if age >= 20:
#     print("odd")

# შევქმნათ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს. შემდეგ დავბეჭდოთ, იყოფა თუ არა 2-ზე, 3-ზე ან ორივეზე.

# age = 16
# input("please write your age : ")


# print(int(age) / int(3))
# print(int(age) / int(2))


#დავწეროთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოცდის ქულას. შემდეგ დავბეჭდოთ მათი ასოების შეფასება შემდეგი სკალის მიხედვით: A (90-100), B (80-89), C (70-79), D (60-69), F (< 60).x

# x = 100

 
# input("Write your test score : ")
# if x > 90: 
#     print("you got an A")
# else:
#     x < 89 or x > 80
#     print("you got a B")



#დავწეროთ პროგრამა, რომელიც სთხოვს მომხმარებელს ორ რიცხვს და შეადარებს მათ.

# year = 2007
# number = 77

# year = input("what year were you born : ")
# number = input("which number is your favourite : ")


# print(year > number)

#დავწეროთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი

# input("which month were you born : ")
 
# x = 13
# while x > 0:
#     x = x - 1
#     if x == 2:
#         break
#     print(x)


#შევქმნათ პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს. სანამ ეს რიცხვი არ იქნება ლუწი, შევეკითხოთ მომხმარებელს თავიდან.

# y = 16

# input("how old are you : ")

# while y == 16:
#     y = y - 2
#     if y == 15:
#         break
#     print(y)


#რიცხვების კლასიფიკაცია: შევქმნათ პროგრამა, სადაც 50-იდან 100-ის ჩათვლით გამოვიტანთ კენტ რიცხვებს. 

# i = 51
# sum = 0

# while i <= 100:
#     print(i)
#     sum = sum + 1 
#     i = i + 2

#მომხმარებელს შევეკითხოთ რიცხვი. სანამ ის ნაკლები იქნება მასზე 20-ით დიდ რიცხვზე, დავპრინტოთ ის და მასზე მოვახდინოთ იტერაცია 1-ით.
age = 16

input("what's your age : ")
while age <= 20:
    print(age)
    age = age + 1