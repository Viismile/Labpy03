r = int(input("Masukkan Nilai N:"))

jumlah = r+1
start = 1
stop = jumlah
for i in range(start, stop):
    from random import random
    a = random()
    print("Data ke", i, "=>", a)
print("Selesai")
