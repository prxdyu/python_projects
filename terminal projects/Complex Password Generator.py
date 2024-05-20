import random
password=""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))               # storing number of letters in nr_letters
nr_symbols = int(input(f"How many symbols would you like?\n"))                                   # storing number of symbols in nr_symbols
nr_numbers = int(input(f"How many numbers would you like?\n"))                                 # storing number of numbers in nr_nr_numbers

letter_lst=random.sample(letters,k=nr_letters)                                                          # selecting k no of letters from letter list using sample method
#print(letter_lst)

number_lst=random.sample(numbers,k=nr_numbers)                                                  # selecting k no o f numbers from number list using sample method
#print(number_lst)

symbol_lst=random.sample(symbols,k=nr_symbols)                                                    # selecting k no of symbols from symbol list using sample method
#print(symbol_lst)

merged_lst=letter_lst+number_lst+symbol_lst                                                         # combining above three list and storing as a single list called merged list
#print("Merged List=",merged_lst)
random.shuffle(merged_lst)
#print("Shuffled List=",merged_lst)                                                                          # shuffling the merged list using shuffle method which shuffles a list (shuffle method modifies the original list)
password="".join(merged_lst)                                                                                 # combining all elements in the shuffle list using join method which returns a string                                                                                 
print("Generated Password: ",password)


