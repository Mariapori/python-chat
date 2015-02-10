# käyttää sokettia
from socket import *
# soketti, bindays, kuuntelu, vastaanotto ja lähetys

HOST = '127.0.0.1' # Localhost
PORT = 8001
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    message = raw_input("Sinun viestisi: ")
    s.send(message)
    print "Odotetaan vastausta.."
    reply = s.recv(1024)
    print "Vastaanotettu! ", repr(reply)
	
s.close()
