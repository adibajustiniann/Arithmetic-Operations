#Nama file : perkalian dengan 3.py 
#Deskripsi : Menghitung hasil perkalian suatu bilangan bulat dengan 3
#Pembuat : Adiba Justinian
#Tanggal : 29 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#mul3 : integer > 0 ---> integer > 0
#   mul3(n) mengalikan n dengan 3
#   mul3(n) = n * 3
#           = 3 + mul3(n-1)

#REALISASI
def mul3(n):
    if n == 1: #baisis 1
        return 3
    elif n + 1 == n:
        return 3
    else: #rekurens
        return 3 + mul3(n-1)

#APLIKASI
print (mul3(1))
print (mul3(4))
print (mul3(25))