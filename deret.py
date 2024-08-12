#Nama file : deret.py 
#Deskripsi : Menghitung suatu deret yang diberikan
#Pembuat : Adiba Justinian
#Tanggal : 30 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#S : integer > 0 ---> integer > 0
#   S(n) = 1 + 4 + 9 + ... + n
#        = n**2 + S(n-1)

#REALISASI
def S(n):
    if n == 0:
        return 0
    else:
        return n**2 + S(n-1)

#APLIKASI
print (S(0))
print (S(1))
print (S(2))
print (S(3))
print (S(4))
print (S(5))
print (S(18))
print (S(73))