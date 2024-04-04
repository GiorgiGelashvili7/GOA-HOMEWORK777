# even_numbers_list = [2,4,6,8,10,12,14,16,18,20]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(numbers[:11:2])



# even_numbers = []
# odd_numbers = []

# for i in range(1,10 + 1):
#     if i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)

# print(even_numbers)
# print(odd_numbers)

#შექმენით პროგრამა, სადაც მოხმარებელს შეეკითხებით ხუთ რიცხვს. ლუწები ერთ სიაში, ხოლო კენტები მეორეში დაამატეთ

# odd_list = []
# even_list = []

# for i in range(5):
#     user_num = int(input("Enter number: "))
    
#     if user_num % 2 == 0:
#         even_list.append(user_num)
#     else:
#         odd_list.append(user_num)
        
# print(odd_list)
# print(even_list)


#შექმენით პროგრამა სადაც გექნებათ ორი სია. პირველ სიაში 10-იდან 20-ის ჩათვლით ლუწი რიცხვები, ხოლო მეორეში კენტები დაამატეთ. 
 

odd_list = []
even_list = []

for i in range(10, 21):
    if i %2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
        
print(odd_list)
print(even_list)