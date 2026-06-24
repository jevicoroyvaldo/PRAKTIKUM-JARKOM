from socket import *

# Identifikasi identitas server tujuan
serverName = 'localhost'
serverPort = 12000

# Inisiasi socket UDP klien
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Meminta input teks dari pengguna
message = input('Masukkan pesan huruf kecil: ')

# Mengirimkan data instan tanpa proses handshake terlebih dahulu
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Membaca balasan dari server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('Hasil Balasan Server: ', modifiedMessage.decode())

# Menutup socket klien
clientSocket.close()