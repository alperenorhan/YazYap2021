# Kullanıcıdan alınan 3 sayıdan, en büyük olanı gösteren programı kodlayınız.

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
sayi3 = int(input("Üçüncü sayıyı giriniz: "))

maxSayi = 0

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
    maxSayi = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
    maxSayi = sayi2
else:
    maxSayi = sayi3

print(sayi1, ",", sayi2, "ve", sayi3,
      "sayıları içinde en büyük olan sayı", maxSayi)
