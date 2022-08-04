#NIM/Nama :16521375/Felisa Aidadora Darmawan
#Tanggal  :6 Oktober 2021
#Deskripsi:Program akan menentukan nilai mahasiswa Tuan Ric lulus atau tidak

#Kamus
#satu:int
#dua:int
#tiga:int
#empat:int
#rata:float

#Algorithma
#input
satu=int(input("Masukkan nilai ujian 1: "))
dua=int(input("Masukkan nilai ujian 2: "))
tiga=int(input("Masukkan nilai ujian 3: "))
empat=int(input("Masukkan nilai ujian 4: "))
#proses
rata=(satu+dua+tiga+empat)/4
if satu>=50 and dua>=50 and tiga>=50 and empat>=50:
    if rata>=70:
        print("Tuan Kil lulus kelas Tuan Ric.") #output
    else:
        print("Tuan Kil tidak lulus kelas Tuan Ric.") #output
else:
    print("Tuan Kil tidak lulus kelas Tuan Ric.") #output
