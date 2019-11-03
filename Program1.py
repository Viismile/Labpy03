modal = 100000000
laba = 0
untung = 0

for i in range(1, 9):
    if i < 3:
        laba = 0
        untung = untung + laba
    elif i < 5:
        laba = modal*1/100
        untung = untung + laba
    elif i < 8:
        laba = modal*5/100
        untung = untung + laba
    else:
        laba = modal*3/100
        untung = untung + laba
    print("Laba bulan ke", i, "sebesar:", laba)
print("Total laba adalah:", untung)
