#progrmam menyimpan data karyawan dalam file data Karyawan dat.

#def fungdi

def getUsia(tgllahir):
    from datetime import datetime
    now = datetime.date(datetime.now())
    lahir = datatime.atrptime (str(tgllahir), "#d-#m-#d").data()
    """menghitung usia,now.tahun -tgllahir.tahun"""
    hasil = now.year -lahir.year
    result =hasil
    return result
def addKaryawan (nip, nama, alamat, gol, tgllahir):
    file.write(str(nip).upper() +"|"+str(nama),upper()+"|"+str(alamat).upper()+"|"+str(gol).upper()+"|"+str(tgllahir).upper()+"|"+str(getUsia(tgllahir))+"\n")
#membuat file
file = open (r"D:\dataKaryawan.dat","w+")
print (""" DATA KARIWAN

input data""")
""" INPUT DATA dengan perulangan """
repeat = "y"
while repeat == "y" or repeat == "Y" :
    nip = str (input("Masukan NIP karyawan : "))
    nama = str (input("Masukan Nama karyawan : "))
    alamat = str (input("Masukan Alamat karyawan : "))
    gol = str (input("Masukan Golongan karyawan : "))
    tgllahir = str (input("Masukan Tanggal lahir : "))


    
    #war repeat
    repeat = str(input ("Masukan lagi : (y\n"))


print("======================================")
file.seek (0, 0)
isi = file.read()
print(isi)
file.close()








