alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(unknown_text, shift_num, function_direction):
    complete_text = ""
    for letter in unknown_text:
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    # TODO-3: What happens if the user enters a number/symbol/space?
    # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    # e.g. start_text = "meet me at 3"
    # end_text = "•••• •• •• 3"
      if letter in alphabet:
        position = alphabet.index(letter)
        if function_direction == "encode":
          new_position = position + shift_num
          if new_position > 25:
            offside = new_position % 26
            complete_text += alphabet[offside]
          elif new_position < 0:
            reduction = new_position % 26
            reduction * -1
            complete_text += alphabet[reduction]
          else:
            complete_text += alphabet[new_position]
        elif function_direction == "decode":
          orig_position = position - shift_num
          if orig_position < 0:
            reduction = orig_position % 26
            reduction * -1
            complete_text += alphabet[reduction]
          else:
            complete_text += alphabet[orig_position]
      else:
        complete_text += letter
    print(f"Here's the {function_direction}d result: {complete_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
game_over = False
while not game_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(unknown_text=text, shift_num=shift, function_direction=direction)
    # e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    # If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    # Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        game_over = True
        print("Goodbye")


