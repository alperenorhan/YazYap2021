# Yarıçapı kullanıcıdan alınan bir dairenin çevresini ve alanını hesaplayan programı kodlayınız. (Pi = 3.14)

piSayisi = 3.14

yaricap = int(input("Dairenin Yarıçapını Giriniz: "))

cevre = 2 * piSayisi * yaricap
alan = piSayisi * yaricap * yaricap

print("Çemberin Çevresi:", cevre)
print("Dairenin Alanı:", alan)
