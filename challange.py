
name_list = []

while True:
    name = input("Skriv ditt namn eller \"exit\": ")
    if name != "exit":
        name_list.append(name)
    else:
        break


name_string = ""

for name in name_list:
    name_string += name + " "

print(name_string)

