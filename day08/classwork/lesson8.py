executed_exercise = 5
Max_rest = 3



question1 = int(input("How long do you practice during the week: "))
question2 = int(input("How many days rest per week"))


print(question1 >= executed_exercise and Max_rest > question2)
print(question1 > executed_exercise or Max_rest <= question2)
print(question1 < executed_exercise and Max_rest >= question2)
print(question1 >= executed_exercise or Max_rest < question2)