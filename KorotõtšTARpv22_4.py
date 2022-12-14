print("Tere! Olen sinu uus sõber - Python!") # info ekraanile, välijundlause
nimi=input("Mis sinu nimi on? ") #sisend lugemine jaoks
print() #tühi rida
print(f"{nimi}, oi kui ilus nimi!")
v=float(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
if v==0:
    quit()
elif v==1:
    m = float (input("Sinu mass: "))
    h = float (input("Sinu pikkus: "))
    h = h/100 #переводим в метры
    index_mass = float(m / (h*h)) # формула из википедиа

#Условия, сокращение до 2х знаков после запятой:
    if float(index_mass) < 16:
        print ("Sinu keha indeks on:", "%.2f" % index_mass, "mass/pikkus²", "Tervisele ohtlik alakaal")
    elif float(index_mass) >= 16 and float(index_mass) <= 19:
        print ("Sinu keha indeks on:", "%.2f" % index_mass, "mass/pikkus²", "Alakaal")
    elif float(index_mass) >= 19 and float(index_mass) <= 25:
        print ("Sinu keha indeks on:", "%.2f" % index_mass, "mass/pikkus²", "Normaalkaal")
    elif float(index_mass) >= 25 and float(index_mass) <= 30:
        print ("Sinu keha indeks on:", "%.2f" % index_mass, "mass/pikkus²", "Ülekaal")
    elif float(index_mass) >= 30 and float(index_mass) <= 35:
        print ("Sinu keha indeks on:", "%.2f" % index_mass, "mass/pikkus²", "Rasvumine")
    elif float(index_mass) >= 35 and float(index_mass) <= 40:
        print ("Sinu keha indeks on:", "%.2f" % index_mass, "mass/pikkus²", "Tugev rasvumine")
    elif float(index_mass) >= 40:
        print ("Sinu keha indeks on:", "%.2f" % index_mass, "mass/pikkus²", "Tervisele ohtlik rasvumine")
print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
