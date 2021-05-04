# Saatte ortalama x km yol giden bir aracın, klavyeden girilen mesafeyi kaç saatte gideceğini hesaplayan programı kodlayınız.

aracSaatteKacKM = int(input("Araç saatte kaç km yol gidiyor? : "))
aracMesafe = int(input("Mesafeyi giriniz: "))

mesafeSure = aracMesafe / aracSaatteKacKM

print("Araç", aracMesafe, "KM yolu", mesafeSure, "saatte gider.")
