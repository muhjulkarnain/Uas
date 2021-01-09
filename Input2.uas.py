def getGapok(gol):
    if data [NIP]["gol"] == "A":
                 gaji = "Rp4.000.00)"
    elif data [NIP]["gol"] == "B" :
                   gaji = "Rp4.500.000"
    elif data [NIP]["gol"] == "C" :
                   gaji = "Rp5.000.000"
    return gaji

#buka file
file = open (r"D:\dataKaryawan.dat", "r")

data = []
for line  in file :
    nip, nama, alamat, gol, tglLahir, Usia = str(line).aplit("|")
   #mesin pencarian
print ("""=====================================
    MESIN PENCARIAM DATA
==================================""")
import time
repeat = "y"
while repeat == "y" or repeat == "Y" :
    #NIP yang tersedia berdasarkan data yang saya kirim  antara lain:
    #A01, A02, B01, B02, C01, C02
    #selain nip di atas maka data tidak di temukan


    NIP = str (input("Masukan NIP/ KODE karyawan :"))
    print()

    try:
        #cari data dengan nip,jika error maka data tidak ada
        #jika error maka masukan ke except...

        DATA = (data [NIP])


        print("Data ditemukan,sedang memangil...")
        #animasi simpel loding
        print ("Loding :",end='')
        time.sleep(1)
        print("=========", end='')
        time.sleep(1)
        print("============", end='')
        time.sleep(1)
        print("================", end='')
        time.sleep(1)
        print("""===================
    """)
        #profil
        print ("""  PROFIL KRYAWAN   :""")

        print ("Kode (NIP) karyawan  :",data [NIP]["nip"])
        print ("Nama karyawan        :",data [NIP]["nama"])
        print ("Alamat               :",data [NIP]["alamat"])
        print ("Golongan             :",data [NIP]["gol"])
        print ("Gaji pokok           :",getGapok[NIP]["gol"])
        print ("Tanggal lahir        :",data [NIP]["tglLahir"], "(Usia : ",data[NIP]["usia"] + "tahun")
    except KeyError :
        print ("Data tidak di temukan:")
    time.sleep(3)
    #input var perulangan
    print ("============================================")
    repeat = str (input ("ingin mencari lagi ? (y\n) "))
        


  
 
        
        














        
