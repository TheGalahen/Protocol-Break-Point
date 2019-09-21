a = 0
print("The program will continue until the number I have selected is entered")
while 1:
    number = int(input("Please Enter a Number"))
    if number == 15:
        break
    if number < 0 or number > 100:
        print("Only 0-100")
        continue
    a += number
print ("Result", a)