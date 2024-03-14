

#დავწეროთ ალგორითმი რომელიც დაბეჭდავს დადებითია, უარყოფითი თუ ნულის ტოლი მომხმარებლის მიერ შემოტანილი რიცხვი.


# num = 20


# if num > 0:
#     print("possitive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")


#დავწეროთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი. მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი.

# num = input("please choose the operation. 1 kilometer-mile. 2 mile-kilometer : " )
# convert = float(input("Enter the numerical value for convert : "))


# if num == "1" :
#     result = convert * 0.6 # kolometer-mile
#     print(result)
# elif num == "2" :
#     result = convert * 1.6 #mile-kilometer
#     print(result)


#შევქმნათ რეგისტრაციის ალგორითმი. მომხმარებელს შევეკითხოთ სახელი, გვარი, ასაკი და მეილი, საბოლოოდ კი ერთ წინადადებაში გამოვიტანოთ მიღებული ინფორმაცია.

# first_name = input("please enter your first name : ")
# last_name = input("please eneter your last name : ")
# age = input("please enter your age : ")
# mail = input("please enter your mail : ")

# print(first_name + " " + last_name + " " + age + " " + mail)


#მომხმარებელს სამჯერ შევეკითხოთ რიცხვითი მნიშვნელობა და დავბეჭდოთ მათი საშუალო არითმეტიკული.

# age = input("please enter your age : ")
# month = input("which month were you born : ")
# year = input("which year were you born : ")


# from statistics import mean

# my_list = [16,9,2007]
# avarage = mean(my_list)
# print(avarage)

#მომხმარებელს შევეკითხოთ 1-იდან 9-ის ჩათვლით რომელიმე რიცხვი. შემდეგ გამოვიყენოთ for ციკლი და გამოვიტანოთ ამ რიცხვის ჯერადები 1-იდან 50-მდე დიაპაზონში.

#num = input("choose number from 1 to 9 : ")

#დავუშვათ მომხმარებელმა აირჩია ციფრი 5

# i = 1
# sum = 0

# while i <= 50:
#     print(i)
#     sum = sum + 1 
#     i = i + 5

# მომხმარებელს შემოვატანინოთ რიცხვი და დავბეჭდოთ მისი ციფრთა ჯამი.

# age = input("enter your age : ")

# print(6 + 1)

#მომხმარებელს შევეკითხოთ სამი რიცხვი და შევამოწმოთ არიან თუ არა პითაგორას რიცხვები.

# age = input("please enter your age : ")
# month = input("which month were you born : ")
# year = input("which year were you born : ")

# if age >= 3:
#     print("pythagorean triples")
# elif month <= 12:
#     print("pythagorean triples")
# else:
#     print("not pythagorean triples")

#დავწეროთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი 1-დან 5-ის ჩათვლით. თუ რიცხვი არის 1-ზე ნაკლები ან 5-ზე მეტი, დავბეჭდოთ "Invalid input". თუ რიცხვი 1-დან 5-ის ჩათვლითაა, დავბეჭდოთ "Valid input".

# number = input("please enter the bumber from 1 to 5 : ")
# number = 2

# if number < 1:
#     print("invalid input")
# elif number > 5:
#     print("invalid input")
# else:
#     print("valid input")
