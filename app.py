# 1.  Skriv ut beräkningar med alla räknesätt (+, -, *, /, **, //). Skriv en kommentar om vad %, // och ** gör

x = 10
y = 3

addition = x+y
subtraction = x-y
multiplication = x*y
division = x/y
exponent = x**y
division_rounded = x//y


print(f"{x} + {y} = {addition}")
print(f"{x} - {y} = {subtraction}")
print(f"{x} * {y} = {multiplication}")
print(f"{x} / {y} = {division}")
print(f"{x} ^ {y} = {exponent}")
print(f"{x} // {y} = {division_rounded}")


# 2. Bygg vidare på välkomstprogrammet med att be om användarens ålder - skriv ut både namn och ålder sen

name = input("Skriv ditt namn: ")
age = int(input("Skriv din ålder: "))

print(f"Hej {name}!, du är {age} år gammal")


# 3. Gör en miniräknare som multiplicerar två olika tal som användaren matar in

number_1 = float(input("Skriv tal 1 (ex. 20.1): "))
number_2 = float(input("Skriv tal 2 (ex. 20.1): "))

answer = number_1*number_2

print(f"{number_1} * {number_2} = {answer}")

# 4. BMI-kalkylator

weight = float(input("Skriv din vikt i kg: "))
height = float(input("Skriv din längd i m: ")) 

bmi = weight/(height**2)

print(f"Din BMI är {bmi}")


# 5. ”Livet i veckor”

age2 = int(input("Skriv din ålder i år: "))
weeks = age2*52
print(f"Din ålder i veckor är {weeks} veckor gammal")

# 6. Viktomvandlare (från kg till lbs)

weight_kg = float(input("Skriv din vikt i kg: "))
weight_lbs = weight_kg*2.2

print(f"Din vikt i pounds är {weight_lbs}lbs")