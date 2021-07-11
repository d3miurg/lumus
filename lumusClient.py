def spam_handler(safe_chats_id, sub_user):
    while True:
        all_chats = sub_user.get_chat_threads()

        for i in all_chats.chatId:
            if not (i in safe_chats_id):
                current_chat = sub_user.get_chat_thread(i)
                creator_id = current_chat.creatorId
                #sub_user.flag('Спам в ЛС', 1)