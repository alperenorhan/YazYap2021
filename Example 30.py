# Klavyeden 10 tane tamsayı girilmesini isteyen ve bu girilen tamsayılardan kaç tanesinin negatif olduğunu bulan programı kodlayınız.

sayac = 0

for i in range(10):
    sayi = int(input("Sayı giriniz giriniz: "))
    if sayi < 0:
        sayac += 1
    else:
        continue

print("Girdiğiniz 10 sayının", sayac, "tanesi negatif.")
