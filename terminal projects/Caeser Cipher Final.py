def caeser(direction,text,shift):
  cipher_text = ""
  
  for letter in text:
    if letter.isalpha():
        position = alphabet.index(letter)
        if direction=="encode":
            new_position = position + shift
        else:
            new_position = position - shift
        cipher_text += alphabet[new_position]
    else:
        cipher_text+=letter
  print(f"The {direction}d text is {cipher_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
choice="yes"
while choice=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caeser(direction,text,shift)
    choice=input("Type 'yes' if you want to go again. Otherwise type 'no'.")
