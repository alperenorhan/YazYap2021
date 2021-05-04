# Çarpma kullanmadan klavyeden girilen sayının n katını bulan programı kodlayınız.

sayi = int(input("Sayı giriniz: "))
nSayisi = int(input("Sayının kaç katı hesaplansın?: "))

toplam = 0

for i in range(nSayisi):
    toplam += sayi

print("Girdiğiniz sayının", nSayisi, "Katı:", toplam)
