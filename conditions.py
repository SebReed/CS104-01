#CS104
#Sebastien Reed
#conditions.py

temp = "a"
temp.lower()
while temp != "end" :
    temp = input("Please enter the curent temperature:")
    if int(temp) > 90:
        print("Wear Shorts")
    elif int(temp) > 70:
        print("Short sleeves are fine")
    elif int(temp) > 50:
        print("Wear a jacket")
    elif int(temp) > 32:
        print("Wear a heavy jacket")
    elif int(temp) <= 32:
        print("Stay inside")
