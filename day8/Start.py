# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Simple Function
'''
def greet():
    print("Hello Aiden")
    print("How do you do Aiden Chen?")
    print("Isn't the weather nice today")
greet()
'''
#Function that allows for input
'''
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Aiden")
'''
#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
# greet_with("Aiden", "taiwan")
# vs.
# greet_with("taiwan", "Aiden")

# Functions with keyword arguments
greet_with(location = "taiwan", name = "aiden")