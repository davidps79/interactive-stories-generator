import random
from pyformlang.cfg import CFG
from data import comments, answers, silence, attacks

class Interactions:
  def __init__(self):
    self.comments = comments
    self.answers = answers
    self.attack = attacks
    self.silence = silence

    self.cfg = CFG.from_text("""
    S -> A | B | E I | E | I
    E -> a f
    A -> a b
    B -> A f
    I -> i i
    """)

  def generateDialog(self):
    l = []
    for i in list(self.cfg.get_words(max_length = 4)):
      l.append(''.join([x.to_text() for x in i]))

    preDialog = random.choice(l)
    result=""
    for i in preDialog:
      match i:
        case 'a':
          result+= random.choice(self.comments) +"\n"
        case 'b':
          result+= random.choice(self.answers) +"\n"
        case 'f':
          result+= random.choice(self.silence) +"\n"
        case 'i':
          result+= random.choice(self.insults) +"\n"
    return result
