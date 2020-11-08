import re

logicalEnum = {
  '&&': 'AND',
  '||': 'OR'
}

class Parser:
  
  def __init__(self, input):
    self.input = input

  def printJSON(self):

    if not self.matchParentheses(self.input): 
      print("Invalid string")

    results = re.split("[()]+", self.input)
    outerSeparator = results.pop(2).strip()

    results = list(filter(None, results))
    mainDict = []
    for x in results:
      innerSeparator = self.getSeparator(x)
      mainDict.append({logicalEnum[innerSeparator] :dict((itm.split('=')[0].strip(), itm.split('=')[1].strip()) for itm in x.split(innerSeparator))})

    data = {
      'query': {
        logicalEnum[outerSeparator]: mainDict
      }
    }

    print(data)
  
  def getSeparator(self, str):
      pattern = re.compile("\s+(&&|\|\|)\s+")
      list = pattern.split(str)
      return list[1]

  def matchParentheses(self, str):
      count = 0
      for i in str:
          if i == "(":
              count += 1
          elif i == ")":
              count -= 1
          if count < 0:
              return False
      return count == 0

Parser("((A=2 && B=3) || (C=4 && D=5))").printJSON()