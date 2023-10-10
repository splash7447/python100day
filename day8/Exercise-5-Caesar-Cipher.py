alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(unknown_text, shift_num, function_direction):
  complete_text = ""
  for letter in unknown_text:
      position = alphabet.index(letter)
      if function_direction == "encode":
          new_position = position + shift_num
          if new_position > 25:
              offside = new_position - 26
              complete_text += alphabet[offside]
          elif new_position < 0:
              reduction = new_position + 26
              complete_text += alphabet[reduction]
          else:
              complete_text += alphabet[new_position]
      elif function_direction == "decode":
          orig_position = position - shift_num
          if orig_position < 0:
              reduction = orig_position + 26
              complete_text += alphabet[reduction]
          else:
              complete_text += alphabet[orig_position]
  print(f"The {function_direction} text is {complete_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(unknown_text=text, shift_num=shift, function_direction=direction)