import socket

Host = '127.0.0.1'
Port = 50000


while True:
    cpf = input('Digite por favor o numero de CPF a ser validado sem . e -  \n OU \nDigite zero para sair do programa: ')
    if cpf == '0':
        quit()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((Host, Port))
        cpf = cpf.encode()
        sock.sendall(cpf)
        data = sock.recv(1024)
        

    print('Resultado:', repr(data.decode()))
    print('\n')