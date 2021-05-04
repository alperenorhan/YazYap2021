# Kullanıcıdan alınan 5 sayının toplamını ve ortalamasını veren programı kodlayınız.

toplam = 0

for i in range(5):
    sayi = int(input("Sayı giriniz: "))
    toplam += sayi

ortalama = toplam / 5

print("Girdiğiniz sayıların toplamı:", toplam)
print("Girdiğiniz sayıların ortalaması:", ortalama)
