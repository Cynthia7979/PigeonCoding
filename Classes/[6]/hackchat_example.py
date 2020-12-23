import hackchat
from random import randint

chat = hackchat.HackChat('CynthiaBot', 'pigeons')


def try_reply(chat_:hackchat.HackChat, message, sender):
    print(f'{message} by {sender}')
    if message == '!help':
        chat_.send_message('Unknown command. Type "/help" for help.')
    if message == '!changeyourcolor':
        color = format(randint(0, 255), 'x')+format(randint(0, 255), 'x')+format(randint(0, 255), 'x')
        print(color)
        chat_._send_packet({'cmd': 'changecolor', 'color': color})


def welcome(chat_, username):
    chat_.send_message(f'Hello {username}!')


def bye(chat_, username):
    chat_.send_message(f'Bye {username}...')


chat.on_message += [try_reply]
chat.on_join += [welcome]
chat.on_leave += [bye]
chat.send_message('/help')
chat.run()
