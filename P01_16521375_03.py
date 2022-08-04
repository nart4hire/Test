#NIM/Nama :16521375/Felisa Aidadora Darmawan
#Tanggal  :6 Oktober 2021
#Deskripsi:Program akan menghitung tarif parkir yang harus dibayar.

#Kamus
#waktu:int
#harga:int
#jam:float

#Algorithma
#input
waktu=int(input("Masukkan waktu parkir: "))
#proses
if waktu<=15:
    harga=0
elif 15<waktu<60:
    harga=5000
elif 60<=waktu<=1440:
    waktu=waktu-60
    jam=waktu/60
    if jam==0:
        y=0
    elif 0<jam<1:
        y=1
    elif 1<=jam<2:
        y=2
    elif 2<=jam<3:
        y=3
    elif 3<=jam<4:
        y=4
    else:
        y=5
    extra=3000*y
    harga=5000+extra
else:
    print("Waktu tidak boleh melebihi 24 jam.")
#output
print("Tarif yang harus dibayar Tuan Ric sebesar", harga, "rupiah.")
    
