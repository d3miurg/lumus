def spam_check(messages, items, chat_id, sub_user):
    for i in range(0, items):
        if messages[i][3] != 2:
            for t in range(i, items):
                if (messages[i][0] == messages[t][0]):
                    if (messages[i][2] != messages[t][2]):
                        for g in range(t, items):
                            if (messages[t][0] == messages[g][0]):
                                if (messages[t][2] != messages[g][2]):
                                    try:
                                        sub_user.edit_chat(chat_id, viewOnly = True)

                                    except:
                                        print('Приватное сообщество. Рейд остановлен, но лучше позвать админов')

                                    spam_user = messages[i][1]
                                    spam_user_name = sub_user.get_user_info(spam_user).nickname
                                
                                    all_users_name = sub_user.get_chat_users(chat_id, size = 500).nickname
                                    if spam_user_name in all_users_name:
                                        try:                           
                                            sub_user.kick(spam_user, chat_id, True)
                                            print(f'{spam_user_name} исключён из чата')

                                        except:
                                            print('Пользователь является ведущим этого чата')

                                    try:
                                        sub_user.edit_chat(chat_id, viewOnly = False)

                                    except:
                                        print('Всё нормально, работаем')

def queue_handler(sub_user, queue, chat_id):
	while True:
		if queue.qsize() > 4:
			sub_user.edit_chat(chat_id, viewOnly = True)

		if queue.qsize() < 4:
			sub_user.edit_chat(chat_id, viewOnly = False)