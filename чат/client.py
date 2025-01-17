import socket

def ser_ver():
    with socket.socket(type=socket.SOCK_DGRAM) as sock:
        while True:
            message = input()
            if message == 'exit':
                break
            sock.sendto(message.encode(), ('localhost', 9090))
            
 ser_ver()

#Для того, чтобы в случае ошибок сокет был закрыт - 100%, с помощью менеджера контекста объявляем сокет типа "UDP".
#В цикле производим запрос нового сообщения, где происходит проверка: желает ли пользователь выйти (сообщение - "exit").
#Если пользователь не желает выходить, то с помощью метода "sendto" отправляем сообщение, которое необходимо закодировать в байты (метод - "encode") и кортеж, с адресом и портом сервера.

