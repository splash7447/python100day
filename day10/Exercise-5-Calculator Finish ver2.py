from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  continue_calculation = True
  num1 = float(input("What's the first number?: "))

  for symbol in operation:
    print(symbol)

  while continue_calculation:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    answer = operation[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    result = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.: ")
    if result == 'y':
      num1 = answer
    elif result == 'n':
      continue_calculation = False
      calculator()

calculator()