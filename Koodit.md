# python-chat
Python 2.7.x Chatti


Client

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


Palvelin

# käyttää sokettia
from socket import *
# soketti, bindays, kuuntelu, vastaanotto ja lähetys

HOST = '127.0.0.1' # Localhost
PORT = 8001
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) #kuinka monta yhteyttä sallitaan?
conn, addr = s.accept()
print 'Yhdistetty osoitteesta' , addr
while True:
    data = conn.recv(1024)
    print "Vastaanotettu!"
    reply = raw_input("Vastaa: ")
    conn.sendall(reply)
	
conn.close()
