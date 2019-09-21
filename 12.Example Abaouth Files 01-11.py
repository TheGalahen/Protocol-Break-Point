notenumber=int(input("How many notes will you enter"))
i=1
total=0
while i<=notenumber:
    note=int(input("Please Enter Note"))
    if note>=1 and note<=100:
        total += note
        i += 1
    else:
        print("Note must be 1-100")
        print("Program will stop")
        break


result=total//notenumber
if result>=1 and result<=49:
    print("") #Sınıfta Kaldınız
elif result>=50 and result<=59:
    print("") #Sınıfı Kötü Not ile Geçtiniz
elif result>=60 and result<=69:
    print("") #Sınıfı Ortalama Not ile Geçtiniz
elif result>=70 and result<=84:
    print("") #Sınıfı Teşekkür Belgesi ile Geçtiniz
elif result>=85 and result<=100:
    print("") #Sınıfı Takdir Belgesi ile Geçtiniz
else:
    print("Result must be 1-100")