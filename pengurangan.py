#Nama file : pengurangan.py 
#Deskripsi : Pengurangan dua bilangan bulat
#Pembuat : Adiba Justinian
#Tanggal : 27 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#minus : 2 integer > 0 ---> integer 
#   minus(x,y) mengurangkan x dan y
#   minus(x,y) = x - y
#              = minus(x,y-1) - 1

#REALISASI
def minus(x,y):
    if y == 0: #basis 0
        return x
    else: #rekurens
        return minus(x,y-1) - 1
    
#APLIKASI
print (minus(2,0))
print (minus(5,2))
print (minus(3,7))