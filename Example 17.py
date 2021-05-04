# Klavyeden girilen sayının faktöriyelini alan programı kodlayınız.

sayi = int(input("Sayıyı giriniz: "))
carpim = 1

while sayi > 0:
    carpim *= sayi
    sayi -= 1


print("Girdiğiniz Sayının Faktöriyeli:", carpim)
