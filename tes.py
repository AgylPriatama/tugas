welcome = '''
==========Selamat Datang==========
===========Di Cek Gaji===========
'''
nama = ("Agyl Priatama")
print(welcome)
print("Isi Data Dibawah Ini Untuk Menentukan Gaji Anda")
hari_kerja = int(input ("Masukkan Hari Kerja Anda Dalam 1 bulan : "))
hari_kerja_perbulan = int (20)
hari_lembur_perhari = int (input ("Masukkan Hari Lembur Anda Dalam 1 Bulan : "))
gaji_pokok = 15000000
uang_lembur_perhari = 200000
print ("Nama Karyawan",nama)

total_gaji = int ((hari_kerja/hari_kerja_perbulan)*gaji_pokok+(hari_lembur_perhari*uang_lembur_perhari))
print ("Gaji Yang Anda Dapatkan Bulan Ini Rp. {:,}".format (total_gaji))