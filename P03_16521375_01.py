#NIM/Nama :16521375/Felisa Aidadora Darmawan
#Tanggal  :3 November 2021
#Deskripsi:Program akan menentukan berapa maksimum hari yang dapat Tuan Dip gunakan untuk menonton TV sesuai aturan yang berlaku

#Kamus
#n,k,max,y=int
#array=list

#Algorithma
n=int(input("Masukkan jumlah hari (N): "))
k=int(input("Masukkan jumlah koin Tuan DIp (k): "))
max=0
array=[0 for i in range(0,1000)]

for i in range(0,n):
    biaya=int(input("Biaya hari ke "+str(i+1)+": "))
    array[biaya]+=1

y=0
for i in range (0,1000):
  if array[i] != 0 and i <= k:
      for j in range (0, array[i]):
          k -= i
          y+=1
          if k < array[i]:
              break

if y>0:
    print("Maksimalnya adalah "+str(y)+" hari.")
else:
    print("Tuan Dip tidak bisa menonton TV ):")
