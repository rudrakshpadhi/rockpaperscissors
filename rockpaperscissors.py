#game of rock paper scissors
import random
list=['rock','paper','scissors'] 
i=0
j=0

while i<1:
    players = int(input('how many players do you have(1/2) \n'))
    if players==1:
        bot_option=random.choice(list)
        user_option=input('enter rock,paper or scissors: \n').lower()
        print('\n'*50)
        if user_option!='rock' and user_option!='paper' and user_option!='scissors':
            print('you can only enter rock,paper or scissors')
    

        if user_option=='scissors' and bot_option=='paper':
            print('The computer chose: ',bot_option)
            print('You chose: ',user_option)
            print('The user has won')
        elif user_option=='paper' and bot_option=='scissors':
            print('The computer chose: ',bot_option)
            print('You chose: ',user_option)
            print('The computer has won')
        elif user_option=='rock' and bot_option=='scissors':
            print('The computer chose: ',bot_option)
            print('You chose: ',user_option)
            print('The user has won')
        elif user_option=='scissors' and bot_option=='rock':
            print('The computer chose: ',bot_option)
            print('You chose: ',user_option)
            print('The computer has won')
        elif user_option=='paper' and bot_option=='rock':
            print('The computer chose: ',bot_option)
            print('You chose: ',user_option)
            print('The user has won')
        elif user_option=='rock' and bot_option=='paper':
            print('The computer chose: ',bot_option)
            print('You chose: ',user_option)
            print('The computer has won')
        elif user_option==bot_option:
            print('The computer chose: ',bot_option)
            print('You chose: ',user_option)
            print('it is a draw')
        else:
            print('Something has gone wrong')
        


    elif players==2:
        user1_option=input('User 1, enter rock,paper or scissors: \n').lower()
        print('\n'*50)
        if user1_option!='rock' and user1_option!='paper' and user1_option!='scissors':
            print('you can only enter rock,paper or scissors')
        else:
            user2_option=input('User 2,enter rock,paper or scissors: \n')
            print('\n'*50)
            if user1_option!='rock' and user1_option!='paper' and user1_option!='scissors':
                print('you can only enter rock,paper or scissors')
            else:
                if user1_option=='scissors' and user2_option=='paper':
                    print('User 1 chose: ',user1_option)
                    print('User 2 chose: ',user2_option)
                    print('User 1 has won')
                elif user1_option=='paper' and user2_option=='scissors':
                    print('User 1 chose: ',user1_option)
                    print('User 2 chose: ',user2_option)
                    print('User 2 has won')
                elif user1_option=='rock' and user2_option=='scissors':
                    print('User 1 chose: ',user1_option)
                    print('User 2 chose: ',user2_option)
                    print('User 1 has won')
                elif user1_option=='scissors' and user2_option=='rock':
                    print('User 1 chose: ',user1_option)
                    print('User 2 chose: ',user2_option)
                    print('User 2 has won')
                elif user1_option=='paper' and user2_option=='rock':
                    print('User 1 chose: ',user1_option)
                    print('User 2 chose: ',user2_option)
                    print('User 1 has won')
                elif user1_option=='rock' and user2_option=='paper':
                    print('User 1 chose: ',user1_option)
                    print('User 2 chose: ',user2_option)
                    print('User 2 has won')
                elif user1_option==user2_option:
                    print('User 1 chose: ',user1_option)
                    print('User 2 chose: ',user2_option)
                    print('it is a draw')
                else:
                    print('Something has gone wrong')
    else:
        print('enter a valid number of players ')
    play_again=input('do you want to play again? (yes/no)\n').lower()
    print('\n'*50)
    if play_again=='no':
        break
    elif play_again=='yes':
        pass












