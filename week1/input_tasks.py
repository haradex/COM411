# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")


print("Please enter a character for the eye")
eye = input()
print("##########")
print(f"#  {eye}  {eye} #")
print("#  ----  #")
print("##########")

print()
print("What is your name?")
name = input()
print("How old are you? (in years)")
age = int(input())
print("How tall are you? (in meters)")
height = float(input())
print("How much do you weigh (in Kilogram)")
weight = float(input())
bmi = weight/height**2
print("Daniel you are 37 years old and bmi 21.6")