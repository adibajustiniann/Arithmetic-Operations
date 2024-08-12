#Nama file : pembagian.py 
#Deskripsi : Pembagian dua bilangan bulat
#Pembuat : Adiba Justinian
#Tanggal : 28 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#div : 2 integer ---> integer
# div(x,y) membagi x dengan y
#   jika x = 0 : div(x,y) = 0
#   jika y = 0 : div(x,y) = "Infinite"
#   jika x = y : div(x,y) = 1
#   jika x > 0 dan y > 0 : div(x,y) = 1 + div(x-y,y)
#   jika x < 0 dan y < 0 : div(x,y) = 1 + div(x-y,y)
#   jika x < 0 dan y > 0 atau x > 0 dan y < 0 : div(x,y) = div(x+y,y) -  1

#REALISASI
def div(x,y):
    if x == 0:
        return 0
    elif y == 0:
        return "Infinite"
    elif x == y:
        return 1
    elif x > 0 and y > 0:
        return 1 + div(x-y,y)
    elif x < 0 and y < 0:
        return 1 + div(x-y,y)
    else:
        return div(x+y,y) -  1

#APLIKASI
print (div(0,3))
print (div(5,0))
print (div(3,3))
print (div(8,2))
print (div(-15,-3))
print (div(-9,3))
print (div(35,-5))