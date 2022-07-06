import random

list = []

print('Welcome to Randomizer - It will andomly choose one option for you.')

def validate(message):
    while True:
        try:
            data = int(input(f'Please insert {message}'))
            return data
        except ValueError:
            print(f"It must be a number. Try Again ")

choice = validate(f'how many options you have: ')

for i in range(choice):    
    list.append(str(input('Insert your option: ')))   


def select_random(x):
    return random.choice(x)


result = select_random(list)
print(f'The choice is: {result}')


