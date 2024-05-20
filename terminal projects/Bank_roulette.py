import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
total_people=len(names)
print(total_people)
index=random.randint(0,total_people-1)
print(index)
print(f"{names[index]} is going to buy the meal today!")
