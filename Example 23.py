# Suyun sıcaklık derecesine göre katı,sıvı veya gaz halinde olduğu bulan ve ekrana yazan programı kodlayınız.

sicaklikDerecesi = int(input("Sıcaklık derecesini giriniz: "))

if sicaklikDerecesi >= 100:
    print("Gaz")
elif 0 < sicaklikDerecesi < 100:
    print("Sıvı")
else:
    print("Katı")
