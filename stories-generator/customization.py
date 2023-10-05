import re
from data import story

def customizeName(fragment,input_name,output_name):
  ex= r".*"+input_name+".*"
  pattern = re.compile(ex)

  result=fragment
  if bool(pattern.match(fragment)):
    result = re.sub(input_name,output_name,fragment)

  return result

def changeAll(o, n):
  for i in story.keys():
    c = story[i]
    newTuple = (customizeName(c[0], o, n), [customizeName(s, o, n) for s in c[1]])
    story[i] = newTuple