# Klavyeden girilen iki pozitif tamsayıdan birincisinin, ikincisi cinsinden kuvvetini alan programı kodlayınız.

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

sonuc = sayi1**sayi2

if (sayi1 < 0) | (sayi2 < 0):
    print("Geçersiz sayı girdiniz.")
else:
    print(sonuc)
