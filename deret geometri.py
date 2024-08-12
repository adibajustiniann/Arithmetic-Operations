#Nama file : deret geometri.py 
#Deskripsi : Menghitung deret geometri
#Pembuat : Adiba Justinian
#Tanggal : 30 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#S : integer > 0 ---> integer > 0
#   S(n) = 1 + 3 + 9 + ... + n
#        = 1 + 3 * S(n-1)

#REALISASI 
def S(n):
    if n == 0: #basis 0
        return 0
    else:
        return 1 + 3 * S(n-1)

#APLIKASI
print (S(0))
print (S(1))
print (S(2))
print (S(3))
print (S(4))
print (S(17))
print (S(42))