import random as rd


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# π¨ Don't change the code above π

# Write your code below this line π
choice = rd.randint(0, len(names)-1)
print(names[choice], "κ° λͺ¨λ  μμκ°μ λ€ λ΄μΌνλ€.")
