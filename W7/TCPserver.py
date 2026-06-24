from socket import *

serverPort = 12000

# Membuat socket berbasis TCP (SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

# Mengaktifkan mode mendengar dengan kapasitas antrean maksimal 1 klien
serverSocket.listen(1)

print("Server TCP beroperasi dan menantikan koneksi client...")

while True:
    # Memblokir eksekusi hingga handshake selesai dan membuat socket khusus sesi
    connectionSocket, addr = serverSocket.accept()
    
    # Membaca kiriman data dari socket sesi yang eksklusif
    sentence = connectionSocket.recv(2048).decode()
    capitalizedSentence = sentence.upper()
    
    # Mengirimkan balasan langsung lewat jalur yang sudah mapan
    connectionSocket.send(capitalizedSentence.encode())
    
    # Memutus jalur sesi klien setelah transaksi data tuntas
    connectionSocket.close()