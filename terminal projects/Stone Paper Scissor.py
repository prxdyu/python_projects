rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
i=1
player_score=0
computer_score=0
result=""
while i<=3:
    i+=1
    player_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    lst=[rock,paper,scissors]
    computer_choice=random.choice(lst)

    if player_choice==0:
      player_choice=rock
    elif player_choice==1:
      player_choice=paper
    elif player_choice==2:
      player_choice=scissors
    else:
        print("Please choose valid number")

    print(player_choice,"\n",computer_choice)

    if player_choice==rock:
      if player_choice==computer_choice:
        result="Draw !"
        print(result)
      elif computer_choice==paper:
        result="You Won !"
        print(result)
      elif computer_choice==scissors:
        result="You Won !"
        print(result)

        
    elif player_choice==paper:
      if player_choice==computer_choice:
        result="Draw !"
        print(result)
      elif computer_choice==rock:
        result="You Lost !"
        print(result)
      elif computer_choice==scissors:
        result="You Won !"
        print(result)

        
    elif player_choice==scissors:
      if player_choice==computer_choice:
        result="Draw !"
        print(result)
      elif computer_choice==paper:
        result="You Won !"
        print(result)
      elif computer_choice==rock:
        result="You Lost !"
        print(result)

    else:
        pass
    if result=="Draw !":
        player_score+=0
        computer_score+=0
    elif result=="You Won !":
        player_score+=1
        computer_score+=0
    elif result=="You Lost !":
        player_score+=0
        computer_score+=1
print(f" Your Score ={player_score}")
print(f" Computer Score ={computer_score}")
if player_score<computer_score:
    print("You Lost the Game !")
elif player_score>computer_score:
    print("You Won the Game !")
        

  






