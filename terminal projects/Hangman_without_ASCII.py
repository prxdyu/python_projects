import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list).lower()
blanked_word=""
for i in range(0,len(chosen_word)):
               blanked_word+="-"
print(blanked_word)
lst_chosen_word=list(chosen_word)
lst_blanked_word=list(blanked_word)
life=5
joined=""
end_of_game=False
while life>0 and end_of_game==False:
    guess=input("Guess the letter:")
    for j in range(len(lst_chosen_word)):
        if guess==lst_chosen_word[j]:
            lst_blanked_word[j]=guess
            joined="".join(lst_blanked_word)
            print(joined)
        else:
            pass
    if guess in joined:
        life+=0
    else:
        life-=1
        print(f"Caution You are left with {life} chances")
    if "-" not in lst_blanked_word:
        end_of_game=True
        print("You Won the Game Pal !")
        
   
            
       



