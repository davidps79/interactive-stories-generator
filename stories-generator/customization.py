import re

class Customization:
  def __init__(self):
    self.names = ["Alex Mercer", "Los renegados","El informante","Sarah Ramirez","Los Cerebros Libres"]

  def customizeName(self, fragment,input_name,output_name):
    ex= r".*"+input_name+".*"
    pattern = re.compile(ex)

    result=fragment
    if bool(pattern.match(fragment)):
      result = re.sub(input_name,output_name,fragment)

    return result

  def changeAll(self, input_name, output_name, story):
    for i in story.keys():
      c = story[i]
      newTuple = (self.customizeName(c[0], input_name, output_name), [self.customizeName(s, input_name, output_name) for s in c[1]])
      story[i] = newTuple

    self.names[self.names.index(input_name)] = output_name