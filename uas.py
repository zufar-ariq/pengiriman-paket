import sys
import random
import csv

aa= 'Paket ini diasuransikan'
bb= 'Paket ini diasuransikan'
cc= 'Paket ini diasuransikan'
dd= 'Paket ini tidak diasuransikan'
iya= 'dan diberi kemasan pelindung'
tidak= 'dan tidak diberi lapisan pelindung'

print('\n','===Selamat Datang di Jasa Pengiriman Paket ANUGRAH SOLO===','\n')
print('...........................................................')
iterasi = True
a= True
b=True
c=True
d=True
e=True
f=True
g=True
h=True
i=True
hitung = 0
paket_jne = [1500, 1000, 500]
paket_tiki = [500,400,300]
paket_sc = [2000,1000,500]
dict_paket = {'A':paket_jne, 'B':paket_tiki, 'C': paket_sc}
total_biaya = 0
dict_ket1 = {'Y':iya, 'N':tidak}
dict_ket2 = {'1':aa, '2':bb, '3':cc, '4':dd}
from datetime import datetime
current = datetime.now()

tahun = current.year
bulan = current.month
hari = current.day
print('Masukkan Data Pengiriman')

while iterasi:
    hitung += 1
    print()
    print('===========================================================')
    print('BIODATA')
    print('===========================================================') 

    while a:
        try:
            nama_pengirim=''
            nama_pengirim=input('Nama pengirim: ')
            if nama_pengirim=='':
                raise ValueError
            else:
                a=False
        except Exception:
            print("\nError: Input tidak sesuai")
            nama_pengirim=str(input('Nama pengirim: '))
            if nama_pengirim=='':
                a=True
            else:
                a=False
    while b:
        try:
            nama_penerima=''
            nama_penerima=input('Nama penerima: ')
            if nama_penerima=='':
                raise ValueError
            else:
                b=False
        except Exception:
            print("\nError: Input tidak sesuai ")
            nama_penerima=str(input('Nama penerima: '))
            if nama_penerima=='':
                b=True
            else:
                b=False
    try:
        no_penerima=input('No Telp penerima: ')
        np= no_penerima.isalpha()
        if np != True:
            pass
        else:
            raise ValueError
    except Exception:
        while c:
            print("\nError: Harus diisi dengan angka ")
            no_penerima=input('No Telp penerima: ')
            np= no_penerima.isalpha()
            if np == True:
                c = True
                pass
            else :
                c=False
                    
    print()
    print('DETAIL ALAMAT PENERIMA')
    print('----------------------')
    while d:
        try:
            rt_rw=input('RT/RW: ')
            if rt_rw !='':
                d=False
            else:
                raise ValueError  
        except Exception:
            print("\nError: Harus diisi ")
            rt_rw=input('RT/RW: ')
            if rt_rw=='':
                d=True
            else:
                d=False
    while e:
        try:
            desa_jln=input('Desa/Jalan: ')
            if desa_jln!='':
                e=False
            else:
                raise ValueError
        except Exception:
            print("\nError: Harus diisi ")
            desa_jln=input('Desa/Jalan: ')
            if desa_jln=='':
                e=True
            else:
                e=False
        
    try:
        kecamatan=input('Kecamatan: ')
        kc=kecamatan.isalpha()
        if kc==True:
            pass
        else:
            raise ValueError
    except Exception:
        while f:
            print("\nError: Input tidak sesuai ")
            kecamatan=input('Kecamatan: ')
            kc=kecamatan.isalpha()
            if kc==True:
                f=False
            else:
                f=True
    try:
        kabupaten=input('Kabupaten: ').lower()
        with open ('daftardaerah.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row [1] == kabupaten:
                    print("Jarak(km) : ",row[2])
                    jarak= int(row[2])
        if kabupaten == '':
            raise ValueError
    except Exception:
        print("\nError: Harus diisi ")
        print("Contoh penulisan yang tepat: semarang ")
        kabupaten=input('Kabupaten: ')

    try:
        provinsi=input('Provinsi: ')
        if provinsi!='':
            pass
        else:
            raise ValueError
    except Exception:
        while g:
            print("\nError: Input tidak sesuai ")
            provinsi=input('Provinsi: ')
            if provinsi=='':
                g=True
            else :
                g=False
    try:
        kode_pos=int(input('Kode Pos: '))
        if kode_pos == (0,100000000):
            raise ValueError
    except Exception:
        print("\nError: Harus diisi dengan angka ")
        kode_pos=input('Kode Pos: ')

    jenis= input('Paket Surat (Y)/ Non Surat (N): ').upper()
    if jenis== 'Y':
        print()
        print('===========================================================')
        print('DETAIL PENGIRIMAN')
        print('===========================================================')
        print()
        print('Pilihan Jenis Agent Pengiriman:')
        print('A. Agent : JNE')
        print('B. Agent : TIKI')
        print('C. Agent : SiCepat')
        try:
            ja= input('pilih agent paket (A/B/C): ').upper()
            if ja == 'A'or'B'or'C':
                pass
            else:
                raise ValueError
        except Exception:
            print("\nTulis dengan format sesuai perintah, contoh:A")
            ja= input('pilih agent paket (A/B/C): ').upper()
        
        while True:
            print()
            print('Pilihan Paket Waktu Pengiriman:')
            print('1. Paket Kilat: 1-2 hari pengiriman')
            print('2. Paket Biasa: 3-4 hari pengiriman')
            print('3. Paket Santai: >=5 hari pengiriman')
            jp= input('pilih jenis paket(1/2/3): ')
            if jp == '1':
                total_ongkir = dict_paket[ja][0] * jarak
                break
            elif jp == '2':
                total_ongkir = dict_paket[ja][1] * jarak
                break
            elif jp == '3':
                total_ongkir = dict_paket[ja][2] * jarak
                break
        no_resi=random.randint(1000, 2000)
        print()
        print('===========================================================')
        print ('BERIKUT DATA PEMESANAN ANDA')
        print('===========================================================')
        print()
        print ('Nama pengirim:', nama_pengirim)
        print ('Nama penerima:', nama_penerima)
        print ('Alamat penerima:', desa_jln,',','RT/RW:', rt_rw,',',kecamatan,',',kabupaten,',',provinsi,',','Kode Pos: ', kode_pos)
        print('No Telp penerima:', no_penerima)
        print('Waktu Pengiriman: ',hari,':',bulan,':',tahun)
        print('No Resi: ',no_resi)
        print ('Jumlah ongkos kirim: Rp',total_ongkir)
        print('...........................................................')
        print ("Total transaksi hari ini: " + str(hitung),'\n')
        o_t= input('Ada traksaksi lain?(Y/N) ').upper()
        if o_t == 'Y':
            total_biaya += total_ongkir
            print()
            a=True
            b=True
            d=True
            e=True
            g=True
            pass
        elif o_t == 'N':
            total_biaya += total_ongkir
            iterasi = False
            
    if jenis== 'N':
        print()
        print('===========================================================')
        print('DETAIL BARANG')
        print('===========================================================')
        try:
            berat_paket= float(input('Berapa berat paket(dlm kg): '))
            if berat_paket < 0:
                raise ValueError
        except Exception:
            print("\nError: Input harus berupa angka tanpa satuan ")
            print("Contoh penulisan: 2 ")
            berat_paket= float(input('Berapa berat paket(dlm kg): '))
        try:
            panjang_paket= float(input('Berapa panjang paket(dlm cm): '))
            if panjang_paket <0:
                raise ValueError
        except Exception:
            print("\nError: Input harus berupa angka ")
            panjang_paket= float(input('Berapa panjang paket(dlm cm): '))
        try:
            lebar_paket= float(input('Berapa lebar paket(dlm cm): '))
            if lebar_paket <0:
                raise ValueError
        except Exception:
            print("\nError: Input harus berupa angka ")
            lebar_paket= float(input('Berapa lebar paket(dlm cm): '))
        try:
            tinggi_paket= float(input('Berapa tinggi paket(dlm cm): '))
            if tinggi_paket <0:
                raise ValueError
        except Exception:
            print("\nError: Input harus berupa angka ")
            tinggi_paket= float(input('Berapa tinggi paket(dlm cm): '))
        
        #durasi_kirim=int(input('Berapa lama paket sampai(dlm hari): '))
    
        berat_konversi= float(((panjang_paket)*(lebar_paket)*(tinggi_paket))/(6000))
        if berat_paket >= berat_konversi:
            berat= berat_paket
        elif berat_paket < berat_konversi:
            berat= berat_konversi
    
        print()
        print('===========================================================')
        print('DETAIL PENGIRIMAN')
        print('===========================================================')
        print()
        print('Pilihan Jenis Agent Pengiriman:')
        print('A. Agent : JNE')
        print('B. Agent : TIKI')
        print('C. Agent : SiCepat')
        ja= input('pilih agent paket (A/B/C): ').upper()
        while True:
            print()
            print('Pilihan Paket Waktu Pengiriman:')
            print('1. Paket Kilat: 1-2 hari pengiriman')
            print('2. Paket Biasa: 3-4 hari pengiriman')
            print('3. Paket Santai: >=5 hari pengiriman')
            jp= input('pilih jenis paket(1/2/3): ')
            if jp == '1':
                biaya = dict_paket[ja][0] * jarak
                break
            elif jp == '2':
                biaya = dict_paket[ja][1] * jarak
                break
            elif jp == '3':
                biaya = dict_paket[ja][2] * jarak
                break
            
        print()
        print('===========================================================')
        print('ASURANSI')
        print('===========================================================')   
        kemas= input('Paket mudah pecah/makanan? (Y/N): ').upper()
        if kemas== 'Y'or 'n':
            biaya_1 = biaya+500
            jumlah_ongkir = ((biaya_1*1)+biaya_1*((berat-1)*0.7))
            ket1 = dict_ket1[kemas]
        elif kemas =='N'or'n':
            biaya_1 =biaya
            jumlah_ongkir = round(((biaya_1*1)+biaya_1*((berat-1)*0.7)),1)
            ket1 = dict_ket1[kemas]
    
        print('\n')   
        print('Pilih jenis barang:')
        print('1. Elektronik Ringan: 1-2 kg')
        print('2. Elektronik Sedang: 3-4 kg')
        print('3. Elektronik Berat: >=5 kg')
        print('4. Non Elektronik')
        
        jb= input('Pilih jenis barang (1/2/3/4): ')      
        if jb== '1':
            total_ongkir = jumlah_ongkir+30000
            ket2 = dict_ket2[jb]
        elif jb== '2':
            total_ongkir = jumlah_ongkir+45000
            ket2 = dict_ket2[jb]
        elif jb== '3':
            total_ongkir = jumlah_ongkir+60000
            ket2 = dict_ket2[jb]
        elif jb== '4':
            total_ongkir = jumlah_ongkir
            ket2 = dict_ket2[jb]
        
        if berat >= 200:
            total_ongkir_1 = total_ongkir+(total_ongkir)
        elif berat >= 150:
            total_ongkir_1 = total_ongkir+(total_ongkir*0.5)
        elif berat >= 100:
            total_ongkir_1 = total_ongkir+(total_ongkir*0.35)
        elif berat >= 75:
            total_ongkir_1 = total_ongkir+(total_ongkir*0.25)
        else:
            total_ongkir_1 = total_ongkir
        
        no_resi=random.randint(1000, 2000)
        
        print()
        print('===========================================================')
        print ('BERIKUT DATA PEMESANAN ANDA')
        print('===========================================================')
        print()
        print ('Nama pengirim:', nama_pengirim)
        print ('Nama penerima:', nama_penerima)
        print ('Alamat penerima:', desa_jln,',','RT/RW:', rt_rw,',',kecamatan,',',kabupaten,',',provinsi,',','Kode Pos: ', kode_pos)
        print('No Telp penerima:', no_penerima)
        print('Waktu Pengiriman: ',hari,':',bulan,':',tahun)
        print('No Resi: ', no_resi)
        print ('Jumlah ongkos kirim: Rp',total_ongkir_1)
        print()
        print ('*Keterangan: ', ket2, ket1)
        print('...........................................................')
        print ("Total transaksi hari ini: " + str(hitung),'\n')
        o_t= input('Ada traksaksi lain?(Y/N) ').upper()
        if o_t == 'Y' :
            total_biaya += total_ongkir_1
            print()
            a=True
            b=True
            d=True
            e=True
            g=True
            pass
        elif o_t == 'N':
            total_biaya += total_ongkir_1
            iterasi = False

print()
print('...........................................................')
print()
print ('Jumlah transaksi hari ini: ' + str(hitung),'\n')
print ("Total transaksi hari ini: " + str(total_biaya),'\n')
print ('==========================================================')
print ('              Anda Telah Keluar dari Sistem               ')
print ('                    Semangat Bekerja                      ')
print ('==========================================================')

