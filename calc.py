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


precedence = {
  '+': 1,
  '-': 1,
  '*': 2,
  '/': 2
}

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


def tokenize(expression):
  tokens = expression.split(" ")

  if tokens[0] == "-":
    tokens[0:2] = [f"-{tokens[1]}"]
    
  i = 1

  while i < len(tokens) - 1:
    if tokens[i] == "-" and (tokens[i-1] in ["+", "-", "*", "/"]):
      tokens[i:i+2] = [f"-{tokens[i+1]}"]
    else:
      i += 1

  ops = []

  stack = []

  for item in tokens:
    if is_number(item):
      stack.append(float(item))
    elif item in ["+", "-", "*", "/"]:
      while ops and precedence[item] <= precedence[ops[-1]]:
        stack.append(ops.pop())
      ops.append(item)
  while ops:
    stack.append(ops.pop())

  evaluate = []

  for item in stack:


    if is_number(item):
      evaluate.append(item)
    elif item in ["+", "-", "*", "/"]:
      num1 = evaluate.pop()
      num2 = evaluate.pop()
  
      if item == "+":
        evaluate.append(num2 + num1)
      if item == "-":
        evaluate.append(num2 - num1)
      if item == "*":
        evaluate.append(num2 * num1)
      if item == "/":
        evaluate.append(num2 / num1)
  return evaluate[0]



  




























































