print('Hello, do you want to play a game?')

answer = input('Yes or No? ')

if answer == 'Yes':
    print('Great, let\'s play!')
else:
    print('Oh well, your loss!!')
    quit()

football = input('What is your favorite football team? ')

print('Your favorite football team is ' + football + '.')