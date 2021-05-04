# Kullanıcının klavyeden girdiği sayı 3’ e ve 5’ e tam bölünüyorsa ekrana tam bölünüyor uyarısı yazan, bölünmüyorsa bölünmüyor uyarısı yazan programı kodlayınız.

sayi = int(input("Sayı giriniz: "))

if sayi % 3 == 0 & sayi % 5 == 0:
    print("Sayı 3 ve 5'e tam bölünüyor.")
else:
    print("Sayı 3 ve 5'e tam bölünmüyor.")
