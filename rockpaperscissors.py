#game of rock paper scissors
import random
import getpass
list=['rock','paper','scissors']
def winner_bot(a,b):
    if a=='rock'and b=='scissors':
        return True
    elif a=='paper'and b=='rock':
        return True
    elif a=='scissors'and b=='paper':
        return True
    elif b=='rock'and a=='scissors':
        return False
    elif b=='paper'and a=='rock':
        return False
    elif b=='scissors'and a=='paper':
        return False
def winner(a,b):
    if a=='rock'and b=='scissors':
        return True
    elif a=='paper'and b=='rock':
        return True
    elif a=='scissors'and b=='paper':
        return True
    elif b=='rock'and a=='scissors':
        return False
    elif b=='paper'and a=='rock':
        return False
    elif b=='scissors'and a=='paper':
        return False
players=int(input('do you want to play 1 player or 2 players(1/2)\n'))
i=0
j=0
num_wins_user1=0
num_wins_user2=0
num_wins_bot=0
num_wins_user=0
if players==1:
    while i<5 and num_wins_user<3 and num_wins_bot<3: 
        bot_option=random.choice(list)
        user_input=input('enter rock,paper or scissors:\n').lower()
        user_input=user_input.replace(' ','')
        if user_input in list:
            if winner_bot(bot_option,user_input)==False:
                print('you chose '+user_input+' the bot chose '+bot_option)
                num_wins_user=num_wins_user+1
                i=i+1
            elif winner_bot(bot_option,user_input)==True:
                print('you chose '+user_input+' the bot chose '+bot_option)
                num_wins_bot=num_wins_bot+1
                i=i+1
            elif bot_option==user_input:
                print('it is a draw')
            print('the score betweeen you and the bot is',num_wins_user,'-',num_wins_bot)
        else:
            print('you did not enter one of the given options')
    if num_wins_user==3:
        print('the user has won the best of 5')
    elif num_wins_bot==3:
        print('the bot has won the best of 5')
    
elif players==2:
    user1=input('User 1, enter your name\n')
    user2=input('User 2, enter your name\n')
    while j<5 and num_wins_user1<3 and num_wins_user2<3:
        user1_input=getpass.getpass(user1+' enter rock,paper or scissors:\n')
        user1_input=user1_input.replace(' ','')
        print('\n'*50)
        user2_input=getpass.getpass(user2+' enter rock,paper or scissors:\n')
        user2_input=user2_input.replace(' ','')
        if user1_input and user2_input in list:
            if winner(user1_input,user2_input)==True:
                print(user1+' chose '+user1_input+' and '+user2+' chose '+user2_input)
                num_wins_user1=num_wins_user1+1
                j=j+1
            elif winner(user1_input,user2_input)==False:
                print(user1+' chose '+user1_input+' and '+user2+' chose '+user2_input)
                num_wins_user2=num_wins_user2+1
                j=j+1
            elif user1_input==user2_input:
                print('it is a draw')
            print('the score betweeen',user1,'and',user2,'is',num_wins_user1,'-',num_wins_user2)
        else:
            print('you did not enter one of the given options')
    if num_wins_user1==3:
        print('the user has won the best of 5')
    elif num_wins_user2==3:
        print('the bot has won the best of 5')












