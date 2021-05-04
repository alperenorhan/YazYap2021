# Üniversite için vize final notları yapılmaktadır. Bir öğrencinin dersten geçme şartı vizenin %30 ile final notunun %70 in toplamı 50 ve üzeri ve final notunun 50 ve daha yüksek olmasıdır. Buna uygun programı kodlayınız.

vizeNot = int(input("Vize Notunu Giriniz: "))
finalNot = int(input("Final Notunu Giriniz: "))

ortalamaNot = (vizeNot*3/10) + (finalNot*7/10)

if finalNot < 50:
    print("Dersten kaldınız.")
elif ortalamaNot < 50:
    print("Dersten kaldınız.")
else:
    print("Dersten geçtiniz.")
