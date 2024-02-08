name = "giorgi"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "giorgi" არის ცვლადისთვის მნიშვნელობა 

surname = "gelashvili"

#print(name)
#პრინტ ფუქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "giorgi"   # ეს არის str (string)  ტიპის ცვლადი
age = 16 # ეს არის int ( integer)  მთელი რიცხვი
height = 185  # ეს არის  float ტიპის ცვლადი (ათწილადი)
#boolean (bool) ტიპის ცვლადი

knows_programming = True   #True ან False
is_ugly = False  #snakecase (უბრალოდ წერის სტილი სტანდარტულად)

isUgly = False # ჯავასკრიპტული cameLcase


print(name + " " + surname)

#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები
#print(name + age)

#print(type(age))
#print(type(name))
#print(type(surname))
#print(type(height))
#print(type(knows_programming))

print(name + " " + surname + " " + str(age) + " " +  str(height) + " " + str(knows_programming))
