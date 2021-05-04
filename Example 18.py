# ax²+bx+c=0 şeklinde verilen 2. derece denklemin köklerini bulan programı kodlayınız.

a = int(input("a sayısını giriniz: "))
b = int(input("b sayısını giriniz: "))
c = int(input("c sayısını giriniz: "))

delta = (b*b) - (4*a*c)

x1 = (-b-delta**0.5)/(2*a)
x2 = (-b+delta**0.5)/(2*a)

print("Birinci Kök:", x1)
print("İkinci Kök:", x2)
