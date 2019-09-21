number=int(input("Please Enter a Number"))
if number<0:
    if number%2==0:
        print("Negative, Even Number")
    else:
        print("Negative, Odd Number")
else:
    if number%2==0:
        print("Positive, Even Number")
    else:
        print("Positive, Odd Number")

import sys
#Bir Devlet Yardımı Hesaplayan Program Yaptım
#Yardımı Almak için; 18 yaş ve üstünde isen 2500 tl altı maaş gerekiyor
#18 yaş altı ise engelli olmalı yada Not Ortalaması 4 ve Üzeri Olmalı

print("") #Devlet yardımı alıp alamayacağınızı görmek için, lütfen gerekli koşullara sahip olup olmadığınızı onaylayınız.
salary=int(input("Please Enter Your Salary"))
age=int(input("Plase Enter Your Age"))
disabled=str(input("Are you disabled? Y/N"))
note=int(input("Please enter you note"))
if disabled=="N" or disabled=="n" or disabled=="Y" or disabled=="y":
    if age>=18 and salary<2500:
        print("") # Devlet Yardımı Alabilirsiniz
    elif age<18 :
        if disabled=="Y" or disabled=="y":
            print("") # Devlet Yardımı Alabilir
        elif note>=4:
            print("")#Devlet Yardımı Alabilir
        else:
            print("a")#Devlet Yardımı Alamaz

    else:
        print("a")#Devlet Yardımı Alamazsınız
else:
    print("Please use N/Y")

