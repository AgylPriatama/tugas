data_mahasiswa = {'Agyl': '1111','Putu': '22222','arridho': '00000','Atex': '7897','Rizal': '3456',
                  'Adib': '1235456','agung': '7777','destito': '1456','ilham': '2579','Ghatsu': '5893',}

welcome = '''
============================================================
============ Selamat Datang Di Simak Unkhair================
 ================== Silahkan Login =========================
============================================================
'''

print (welcome)

username = input ("Silahkan Masukan Username Anda : ")
password = input ("Masukan Password Anda : ")

if username in data_mahasiswa and data_mahasiswa[username] == password :
    print ("Anda Berhasil Login Ke SIMAK UNKHAIR")
    print ("Selamat datang Di Sistem Infotmasi Akademik Universitas Khairun Ternate")

else :
    print ("Login Gagal, Username Atau password Anda Salah")