#Sebatien Reed
#CS104

names = []
for i in range(10):
    acceptedName = input("enter name: ")
    names.append(acceptedName)
print(names)
for i in range(len(names)):
    print(names.pop(0))
print(names)
