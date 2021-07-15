import socket #Lib para sockets em python
from validador import validate_CPF

Host = 'localhost'
Port = 50000

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind((Host,Port))
# sock.listen()
# print('Waiting for Client')
# connect, adress = sock.accept()
# print('Connected in {}'.format(adress))


while True:    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:            
        sock.bind((Host, Port))        
        sock.listen()    
        print('Waiting for Client')            

        connected_port, address_port = sock.accept()
        print('Connected in {}'.format(address_port))
        with connected_port:                               
            while True:
                data = connected_port.recv(1024)                
                if not data:                    
                    break
                else:
                    data = data.decode()
                    if(validate_CPF(data) == 1):
                        anwser = 'CPF Validado'                        
                        connected_port.sendall(anwser.encode())
                    else:
                        anwser = 'Não é um CPF plausivel de validação'                        
                        connected_port.sendall(anwser.encode())
