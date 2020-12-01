PASSWORD = '000000'

print('Cynthia\'s Vault Security System')
if input('Enter Password: ') == PASSWORD:
    print('Correct Password. You opened the vault!')
    print('There are $100,000,000,000 in vault.')
    print('[1] Take all')
    print('[2] Leave')
    answer = input('What would you do? ')
    if answer == '1':
        print('You stole all the money.')
    elif answer == '2':
        print('You left the money where it is. You\'re a good person!')
    else:
        print('You chose an unavailable choice, the police came and captured you.')
else:
    print('Incorrect password!! Calling police...')

and_ = 123
print(and_)
