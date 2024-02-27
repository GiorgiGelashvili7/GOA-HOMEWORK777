# required_weight = 50
# required_height = 170

# weight = int(input("please write your weight: "))
# height = int(input("Please write your height: "))


# print(weight == required_weight and height == required_height)
# print(weight > required_weight and height < required_height)
# print(weight <= required_weight or height >= required_height)
# print(weight < required_weight or height <= required_height)
# print(weight <= required_weight and height >= required_height)
# print(weight > required_weight or height < required_height)

required_pushups = 150
required_squats = 100

pushups = int(input("How much pushups do you do during the day: "))
squats = int(input("How much squats do you do during the day: "))

print(pushups == required_pushups and squats == required_squats)
print(pushups >= required_pushups and squats <= required_squats)
print(pushups == required_pushups or squats == required_squats)
print(pushups <= required_pushups or squats >= required_squats)
