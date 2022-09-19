import json
with open('mahasiswa.json','r') as file:
    data = json.load(file)

jumlah_siswa = int(input("Masukkan Jumlah Mahasiswa Baru: "))

for i in range(0,jumlah_siswa):
    nama = input(str("Masukkan Nama Anda: "))
    jumlah_hobi = int(input("Masukkan Jumlah hobi: "))
    Biodata = {"Hobi":[], "Prestasi":''}
    hobii= []
    for j in range (0,jumlah_hobi):
        x = input("Masukkan Hobi ke-"+str(j+1)+': ')
        hobii.append(x)
    Biodata['Hobi'] = hobii
    prestasi = input("Masukkan Prestasi Anda: ")
    Biodata['Prestasi'] = prestasi
    data[nama]=[Biodata]
    with open('mahasiswa.json','w') as file:
        json.dump(data,file)
    print('=========Data Berhasil Ditambahkan=========')
