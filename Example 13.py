# Girilen iki sayı arasından büyük olan sayıyı gösteren programı kodlayınız.

sayi1 = int(input("Birinci Sayıyı Giriniz: "))
sayi2 = int(input("İkinci Sayıyı Giriniz: "))

if sayi1 == sayi2:
    print("Aynı sayıları girdiniz.")
elif sayi1 > sayi2:
    print("Büyük olan sayı: ", sayi1)
else:
    print("Büyük olan sayı: ", sayi2)
