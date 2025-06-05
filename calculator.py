#!/usr/bin/env python

def calculation(num1,operator,num2):
      if operator == "*":
        ans = num1 * num2
        print(ans)
      elif operator == "**":
        ans = num1 ** num2
        print(ans)
      elif operator == "+":
        ans = num1 + num2
        print(ans)
      elif operator == "-":
        ans = num1 - num2
        print(ans)
      elif operator == "/":
        if num2 == 0:
          print('infinity (divided by zero)')
        else:
          ans = num1 / num2
          print(ans)
      elif operator == "//":
        if num2 == 0:
          print('error (divided by zero)')
        else:
          ans = num1 // num2
          print(ans)

while True:
  operation = input("input an operation (ex. 5 + 2) or press q to quit anytime: ")
  if operation == 'q':
    print('exiting calculator')
    break
  else:

    parts = operation.split(" ")

    num1 = float(parts[0])

    num2 = float(parts[2])

    operator = parts[1]

    calculation(num1,operator,num2)















