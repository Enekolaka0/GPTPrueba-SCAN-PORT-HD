import socket

# Creamos un socket para escuchar conexiones entrantes
s = socket.socket()

# Especificamos la dirección IP y el puerto que deseamos escanear
ip_address = "192.168.0.1"
port = 80

# Intentamos conectarnos al puerto especificado en la dirección IP especificada
try:
    s.connect((ip_address, port))
    print("El puerto", port, "de la dirección IP", ip_address, "está abierto")
except:
    print("El puerto", port, "de la dirección IP", ip_address, "está cerrado")

# Cerramos el socket
s.close()
