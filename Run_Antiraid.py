import amino
import lumusServer
import getpass

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
chats = sub_user.get_chat_threads()

chat_id = []
for i in range(len(chats.title)):
    chat_id.append(chats.chatId[i])

    if chats.title[i] is None:
        print(str(i) + ' ' + 'Безымянный чат')

    else:
        print(str(i) + ' ' + chats.title[i])

chat_num = int(input())

current_chat_id = chat_id[chat_num]

while True:
	count = 4
    new_messages = sub_user.get_chat_messages(current_chat_id, 4)

    if count != len(new_messages.content):
            count = len(new_messages.content) - 1

    current_iteration = []

    for t in range(count):
        first_part = new_messages.author.nickname[t] + ': '

        if new_messages.content[t] is None:
            full_message = first_part + 'НЕ ТЕКСТОВОЕ СООБЩЕНИЕ ТИПА ' + str(new_messages.type[t])

        else:
            full_message = first_part + new_messages.content[t]

        current_iteration.append([full_message, new_messages.author.userId[t], new_messages.messageId[t]])

    current_iteration.reverse()
    
    lumusServer.span_check(current_iteration, count + 1, chat_id, sub_user)
