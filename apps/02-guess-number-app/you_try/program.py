import random as r

print('------------------------')
print('Guess the number App')
print('------------------------')

random_num = r.randint(0, 100)
user_guess = -1

while(user_guess != random_num):
    print('Take a guess at the number (0-100): ')
    user_guess = int(input())

    if(user_guess > random_num):
        print('You guessed {}, which is too high'.format(user_guess))

    elif(user_guess < random_num):
        print('you guessed {}, which is too low'.format(user_guess))

    else:
        print('you guessed right! the number was {}'.format(random_num))
