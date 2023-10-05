import re
from data import descriptions
from story_automaton import dfa
import interactions

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
    choice = input()
    match choice:
      case '1':
        self.storyPoint(self.func(point, '1')[0].value)
      case '2':
        self.storyPoint(self.func(point, '2')[0].value)
      case '3':
        if 3 not in exclude:
          if point in descriptions:
            print(descriptions[point])
          else:
            print('No encuentras pistas en este momento')
          self.decide(point, exclude.append(3))
        else:
          self.decide(point, exclude)
      case '4':
        if 4 not in exclude:
          print(interactions.generateDialog())
          self.decide(point, exclude.append(4))
        else:
          self.decide(point, exclude)
      case _:
        self.decide(point, exclude)