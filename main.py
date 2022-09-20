import random

# #split string method
# names_string = input("Give me everybody's names, separated by a comma.: \n")
# names = names_string.split(", ")

# #random picker
# length=len(names)
# random_generator=random.randint(0,length-1)
# print("\n" + names[random_generator] + " is going to buy the meal today!")

names = input("Give me everybody's name, separated by a ', ' (comma): \n").lower().split(", ")
final_index = random.randint(0, len(names))
final_person = names[final_index]

print(f"{final_person.title()} is going to buy the meal today!")
