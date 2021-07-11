import amino
import socket
import lumusServer
import getpass

socket = socket.socket()
socket.bind(('localhost', 605))

user = amino.Client()

email = input('Почта: ')
password = getpass.getpass(prompt = 'Пароль: ')
user.login(email, password)

comms = user.sub_clients()

com_id = []
for i in range(len(comms.name)):
    com_id.append(comms.comId[i])
    print(str(i) + ' ' + comms.name[i])

com_num = int(input())

sub_user = amino.SubClient(comId = com_id[com_num], profile = user.profile)