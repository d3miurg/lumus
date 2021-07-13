def spam_check(messages, chat_id, sub_user):
    if messages[0][0] == messages[1][0]:
        if messages[1][0] == messages[2][0]:
            try:
                sub_user.edit_chat(chat_id, viewOnly = True)

            except:
                print('Приватное сообщество. Рейд остановлен, но лучше позвать админов')

            spam_user = messages[2][1]
            spam_user_name = sub_user.get_user_info(spam_user).nickname
            
            try:                           
                sub_user.kick(spam_user, chat_id, True)
                print(f'{spam_user_name} исключён из чата')

            except:
                print('Пользователь является ведущим этого чата')

            try:
                sub_user.edit_chat(chat_id, viewOnly = False)

            except:
                print('Всё нормально, работаем')
