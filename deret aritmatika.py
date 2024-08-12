#Nama file : deret aritmatika.py 
#Deskripsi : Menghitung deret aritmatika
#Pembuat : Adiba Justinian
#Tangal : 30 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#S : integer > 0 ---> integer > 0
#   S(n) = 3 + 6 + 9 + ... + n
#        = 3 * n + S(n-1)

#REALISASI
def S(n):
    if n == 0: #basis 0
        return 0
    else: #rekurens
        return 3 * n + S(n-1)

#APLIKASI
print (S(0))
print (S(1))
print (S(2))
print (S(3))
print (S(4))
print (S(7))
print (S(12))
    