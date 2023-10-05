import re
from data import descriptions
from story_automaton import dfa
from validations import validate
from interactions import generateDialog

class Core:
  def __init__(self, story, dialogs, descriptions):
    func = dfa._transition_function
    self.story = story
    self.dialogs = dialogs
    self.descriptions = descriptions
  
  def storyPoint(self, point):
    if point!='q0':
      print()

    print(self.story[point][0])

    if (point in dfa._final_states):
      return
    else:
      self.decide(point, [])

  def decide(self, point, exclude):
    while True:
      choice = input()
      choice = validate(choice)
      match choice:
        case 2:
          self.storyPoint(self.func(point, '1')[0].value)
        case 3:
          self.storyPoint(self.func(point, '2')[0].value)
        case 8:
          if 3 not in exclude:
            if point in descriptions:
              print(descriptions[point])
            else:
              print('No encuentras pistas en este momento')
            self.decide(point, exclude.append(3))
          else:
            self.decide(point, exclude)
        case 1:
          if 4 not in exclude:
            print(generateDialog());
            self.decide(point, exclude.append(4))
          else:
            print('Nadie está de humor para hablar ahora mismo')
        case _:
          print("Ingresa un cadena valida")
      
      if (choice==2 or choice == 3 or choice==8 or choice==1):
        break