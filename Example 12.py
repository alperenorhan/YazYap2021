# Kullanıcıdan alınan 10 sayıdan çift olanları toplayan ve sonucu gösteren programı kodlayınız.

toplam = 0

for i in range(10):
    sayi = int(input("Bir Sayı Giriniz: "))
    if sayi % 2 == 0:
        toplam += sayi
    else:
        continue

print("Girdiğiniz sayılardan çift olanların toplamı:", toplam)
