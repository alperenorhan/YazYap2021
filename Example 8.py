# Girilen sayı 0 dan büyük ise “pozitif” küçük ise “negatif” sıfıra eşit ise ”sıfır” mesajını verdiren programı kodlayınız.

girilenSayi = int(input("Bir sayı giriniz: "))

if girilenSayi < 0:
    print("Sayı negatif.")
elif girilenSayi > 0:
    print("Sayı pozitif.")
else:
    print("Sayı sıfır.")
