#!/usr/bin/env python
# simple port scanner
# author arie.kolmteist
# hargai karya orang lain dengan tidak mengganti watermark.
import socket
import subprocess
import sys
from datetime import datetime

# Membersihkan layar
subprocess.call('clear', shell=True)

# Perintah
remoteServer    = raw_input("Masukan alamat host untuk dicari: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Menampilkan banner dengan informasi alamat host yang akan di cari
print "-" * 60
print "Tunggu , sedang melakukan pencarian", remoteServerIP
print "-" * 60

# Cek waktu memulai pencarian
t1 = datetime.now()

# 

# 

try:
    ports = [22,445,80,443,3389,21,25,23,53,194,3306,110,119,123,143,161,162,20,67,68,69,137,138,139,179,389,636,989,990,]
    for port in ports:  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Terbuka".format(port)
        sock.close()

except KeyboardInterrupt:
    print "-Dihentikan"
    sys.exit()

except socket.gaierror:
    print 'Hostname tidak bisa di temukan. Keluar'
    sys.exit()

except socket.error:
    print "Tidak bisa terkoneksi ke Server"
    sys.exit()

# Cek Waktu
t2 = datetime.now()

#Kalkulasi perbedaan waktu, untuk melihat berapa lama waktu untuk menjalankan script
total =  t2 - t1

# Menampilkan informasi ke layar
print 'Mencari Selesai di: ', total
