import random

def game():
    print("Welcome to the game\nI chose a number from 1 to 50(it is an integer)")
    random_number = random.randint(1,50)
    # print(random_number)     # for testing
    chances = 5
    
    while chances > 0:
        user_guess = int(input("enter your number: "))
        if user_guess > random_number:
            print('too high')
            chances -= 1
        elif user_guess < random_number:
            print('too low')
            chances -= 1
        else:
            print(f'correct,answer is {random_number}')
            break    

    if chances == 0:
        print('game over\n')
        input123 = input('retry or not(yes/no):')
        if input123 == 'yes':
            game()
        else:
            print('thanks for playing')
            

if __name__ == '__main__':
    game()      
        