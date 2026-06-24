from socket import *

serverName = 'localhost'
serverPort = 12000

# Membuat socket TCP klien
clientSocket = socket(AF_INET, SOCK_STREAM)

# Menjalankan proses 3-Way Handshake ke server target
clientSocket.connect((serverName, serverPort))

sentence = input('Masukkan pesan huruf kecil: ')

# Mengirim data langsung melalui pipa koneksi yang sudah terhubung
clientSocket.send(sentence.encode())

# Menangkap aliran data balik dari server
modifiedSentence = clientSocket.recv(2048)
print('Hasil Balasan Server TCP: ', modifiedSentence.decode())

# Terminasi koneksi secara bersih
clientSocket.close()