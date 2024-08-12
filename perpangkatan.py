#Nama file : perpangkatan.py 
#Deskripsi : Menghitung hasil pangkat suatu bilangan bulat
#Pembuat : Adiba Justinian
#Tanggal : 28 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#exp : 2 integer > 0 ---> integer > 0
#   exp(x,y) menghasilkan x**y, x != 0
#   exp(x,y) = x**y
#            = x * exp(x,y-1)

#REALISASI
def exp(x,y):
    if y == 0: #basis0
        return 1
    else: #rekurens
        return x * exp(x,y-1)

#APLIKASI
print (exp(2,0))
print (exp(5,1))
print (exp(4,8))

