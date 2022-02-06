#Latihan konversi suhu
#Konversi celcius ke satuan lain

print("\nProgram konversi temperatur celcius\n")

celcius = float(input("Masukkan suhu (dalam celcius) : "))

print("Suhu adalah", celcius, "Celcius")

#reamur (4/5 Celcius)
reamur = (4/5)*celcius
print("Suhu dalam reamur adalah", reamur, "reamur")

#fahreinheit
fahreinheit = ((9/5)*celcius)+32
print("Suhu dalam fahreinheit adalah", fahreinheit, "fahreinheit")

#kelvin
kelvin = celcius + 273.5
print("Suhu dalam kelvin adalah", kelvin, "kelvin")

print("=====================DONE===================")

#Konversi reamur ke satuan lain

print("\nProgram konversi temperatur reamur\n")

reamur = float(input("Masukkan suhu (dalam reamur) : "))

print("Suhu adalah", reamur, "reamur")

#celcius (5/4 reamur)
reamur = (5/4)*reamur
print("Suhu dalam celcius adalah", reamur, "reamur")

#fahreinheit
fahreinheit = ((9/4)*reamur)+32
print("Suhu dalam fahreinheit adalah", fahreinheit, "fahreinheit")

#kelvin
kelvin = (5/4) + 273.5
print("Suhu dalam kelvin adalah", kelvin, "kelvin")

print("=====================DONE===================")

#Konversi fahreinheit ke satuan lain

print("\nProgram konversi temperatur fahreinheit\n")

fahreinheit = float(input("Masukkan suhu (dalam fahreinheit) : "))

print("Suhu adalah", fahreinheit, "fahreinheit")

#celcius (5/9 fahreinheit)
celcius = (5/9)* fahreinheit - 32
print("Suhu dalam celcius adalah", celcius, "celcius")

#reamur
reamur = ((4/9)*fahreinheit) - 32
print("Suhu dalam reamur adalah", reamur, "reamur")

#kelvin
kelvin = (5/9) + 273.5 - 32
print("Suhu dalam kelvin adalah", kelvin, "kelvin")

print("=====================DONE===================")

#Konversi kelvin ke satuan lain

print("\nProgram konversi temperatur kelvin\n")

kelvin = float(input("Masukkan suhu (dalam kelvin) : "))

print("Suhu adalah", kelvin, "kelvin")

#celcius (5/9 kelvin)
celcius = kelvin - 273.5
print("Suhu dalam celcius adalah", celcius, "celcius")

#reamur
reamur = ((4/5)*kelvin) - 273.5
print("Suhu dalam reamur adalah", reamur, "reamur")

#fahreinheit
fahreinheit = (9/5) - 273.5 + 32
print("Suhu dalam fahreinheit adalah", fahreinheit, "fahreinheit")

print("=====================DONE===================")