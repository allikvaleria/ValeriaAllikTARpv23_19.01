print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis sinu nimi on?")
print(nimi,"oi kui ilus nimi!")
vastus=input(nimi +  "Kas leian Sinu keha indeksi? 0-ei, 1-jah =>")
try:
    if vastus== "1" :
        pikkus=int(input("Kui pikk sa oled?"))
        mass=float(input("Mis on teie kaal?"))
        indeks = mass/(0.01 * pikkus)**2 #ошибка с float и str
        indeks = round(indeks,1)
        print(indeks)
        indeks = round(indeks,1)
        vastus=print(nimi , "! Sinu keha indeks on:" , indeks)
        if indeks<16:
                vastus="Tervisele ohtlik alakaal"
        elif 16<indeks<19:
                vastus="Alakaal"
        elif 19<indeks<25:
                vastus="Normaalkaal"
        elif 25<indeks<30:
                vastus="Ülekaal"
        elif 30<indeks<35:
                vastus="Rasvumine"
        elif 35<indeks<40:
                vastus="Tugev rasvumine"
        elif indeks>40:
                vastus="Tervisele ohtlik rasvumine"
        print(vastus)
    else:
        print("Kahju! See on väga kasulik info!")
except:
    print("ValueError")
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
