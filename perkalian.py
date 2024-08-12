#Nama file : perkalian.py 
#Deskripsi : Perkalian dua bilangan bulat
#Pembuat : Adiba Justinian
#Tanggal : 27 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#mul : 2 integer > 0 ---> integer > 0
#   mul(x,y) mengalikan x dan y
#   mul(x,y) = x * y 
#            = x + mul(x,y-1)
            
#REALISASI
def mul(x,y):
    if x == 0 or y == 0: #basis0
        return 0
    else: #rekurens
        return x + mul(x,y-1)

#APLIKASI
print (mul(0,5))
print (mul(3,0))
print (mul(2,7))
print (mul(9,3))