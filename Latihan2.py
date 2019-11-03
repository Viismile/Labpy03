a = int()
b = 0

while a >= 0:
    a = int(input("Masukkan Bilangan: "))
    if a == 0:
        break
    if a > b:
        b = a
print("Bilangan terbesar adalah :", b)
print("Selesai")
