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


class Trigcalculation(Calculation):
  def trigcalculate(self):
    if self.operator == "cos":
      return math.cos(math.radians(self.num1))
    elif self.operator == "sin":
      return math.sin(math.radians(self.num1))
    elif self.operator == "tan":
      return math.tan(math.radians(self.num1))


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
      elif parts[0] in ["cos", "sin", "tan"]:

        operator = parts[0]

        num1 = float(parts[1])

        currentcalc = Trigcalculation(num1, operator, 0)

        print(currentcalc.trigcalculate())
      else:
        num1 = float(parts[0])

        num2 = float(parts[2])

        operator = parts[1]

        currentcalc = Calculation(num1, operator, num2)

        print(currentcalc.calculate())
  except ValueError:
    print('Invalid number entered. Please make sure to enter something like: 5 + 2')
  
  















