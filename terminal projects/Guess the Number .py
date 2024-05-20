class TooSmallException(Exception):
    pass
class TooLargeException(Exception):
    pass
number=10
current_chance=1
max_chance=3

while current_chance<=max_chance:
    try:
        n=int(input("Enter a number:"))
        if n<number:
            remaining_chance=max_chance-current_chance
            raise TooSmallException
        elif n>number:
            remaining_chance=max_chance-current_chance
            raise TooLargeException
    except TooSmallException:
        print("oops ! the entered number is smaller\n Remaining Chances={}".format(remaining_chance))
        
    except TooLargeException:
        print("oops ! the entered number is Greater\n Remaining Chances={}".format(remaining_chance))
       
    else:
        print("Great ! You Guessed it correctly")
        
    finally:
        current_chance+=1
