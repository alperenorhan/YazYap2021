# Kullanıcıdan alınan 50 sayının toplamını gösteren programı kodlayınız.

toplam = 0

for i in range(50):
    sayi = int(input("Sayı Giriniz: "))
    toplam += sayi

print("Girdiğiniz sayıların toplamı: ", toplam)
