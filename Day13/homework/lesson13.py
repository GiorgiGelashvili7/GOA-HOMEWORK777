# დავწეროთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს


# age = int(input("how old are you : "))

# if age < 18:
#     print("you are a minor")
# elif age > 18 and age < 65:    
#     print("you are an adult")
# elif age >= 65:
#     print("you are senior citizen")


#შევქმნათ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს რიცხვი ლუწია თუ კენტი.

# month = int(input("which month were you born : "))

# if month > 1 and month < 3:  
#     print("this is even")
# elif month > 3 and month < 5:
#     print("this is even")
# elif month > 5 and month < 7: 
#     print("this is even")
# elif month > 7 and month < 9:
#     print("this is even")
# elif month > 9 and month < 11:
#     print("this is even")
# else:
#     print("this is odd")


#დავწეროთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით.


# grade = input("please enter your grade : ")

# if grade == "A":
#    print("Excellent")
# elif grade == "B":
#    print("good job") 
# elif grade == "C":
#    print("you passed")
# elif grade == "D":
#    print("you can do better")
# elif grade == "F":
#    print("you failed") 
# else:
#    print("try again")


# დავწეროთ პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 10-მდე while ციკლის გამოყენებით.

# i = 0
# while i < 10:
#     i = i + 1
#     print(i)


#შევქმნათ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. გამოვიყენოთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს. 
#დავუშვათ ეს რიცხვია 7


# num = int(input("choose the number : "))


# if num > 6 and num < 8:
#     print("true")
# elif num < 6:
#     print("false")
# else:
#     print("try again")    


# დავწეროთ პროგრამა, რომელიც დაბეჭდავს მოცემული რიცხვის (მაგ 5) პირველ 10 ჯერადს for loop-ის გამოყენებით.

# for i in range(0,50,5):
#     print(i)



#შევქმნათ პროგრამა, რომელიც ბეჭდავს უკუთვლას 10-დან 1-მდე for loop-ის გამოყენებით.


sum = 10
for i in range(10):
    sum = sum - 1
    print(sum)
    