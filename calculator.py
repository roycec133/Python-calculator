#!/usr/bin/env python

import math

class Calculation():

  def __init__(self, num1, operator, num2):
    self.num1 = num1
    self.operator = operator
    self.num2 = num2
  
  def calculate(self):
    if self.operator == "*":
        ans = self.num1 * self.num2
    elif self.operator == "**":
      ans = self.num1 ** self.num2
    elif self.operator == "+":
      ans = self.num1 + self.num2
    elif self.operator == "-":
      ans = self.num1 - self.num2
    elif self.operator == "/":
      if self.num2 == 0:
         ans= 'infinity (divided by zero)'
      else:
        ans = self.num1 / self.num2
    elif self.operator == "//":
      if self.num2 == 0:
        ans = 'error (divided by zero)'
      else:
          ans = self.num1 // self.num2
    return ans


while True:
  try:
    operation = input("input an operation (ex. 5 + 2) or press q to quit anytime: ")
    if operation == 'q':
      print('exiting calculator')

      break

    else:

      parts = operation.split(" ")

      if parts[0] == "sqrt":
        if int(parts[1]) >= 0:
          print(math.sqrt(int(parts[1])))
        else:
          print("Error: entered sqaure root of a negative")
      else:
        num1 = float(parts[0])

        num2 = float(parts[2])

        operator = parts[1]

        currentcalc = Calculation(num1, operator, num2)

        print(currentcalc.calculate())

      

  except ValueError:
    print('Invalid number entered. Please make sure to enter something like: 5 + 2')
  
  















