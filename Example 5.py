# Vize notunu ve final notunu kullanıcıdan alan ve öğrencinin geçme durumunu gösteren programı kodlayınız.
# Vize %40, Final %60 etkili. Geçme Notu : 60

vizeNot = int(input("Vize Notunu Giriniz: "))
finalNot = int(input("Final Notunu Giriniz: "))

ortalamaNot = (vizeNot * 4/10) + (finalNot * 6/10)

if finalNot < 60:
    print("Dersten kaldınız.")
elif ortalamaNot < 60:
    print("Dersten Kaldınız.")
else:
    print("Dersten Geçtiniz.")
