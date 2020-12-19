import hackchat

chat = hackchat.HackChat('CynthiaBot', 'pigeons')


def try_reply(chat_, message, sender):
    print(f'{message} by {sender}')
    if message == '/help':
        chat_.send_message('Unknown command. Type "/help" for help.')


def welcome(chat_, username):
    chat_.send_message(f'Hello {username}!')


def bye(chat_, username):
    chat_.send_message(f'Bye {username}...')


chat.on_message += [try_reply]
chat.on_join += [welcome]
chat.on_leave += [bye]
chat.run()
