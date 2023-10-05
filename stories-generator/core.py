import re
from data import story, dialogs, descriptions
from story_automaton import dfa

func = dfa._transition_function

def decide(point, exclude):
  print('Es momento de decidir...')
  print('1.', story[point][1][0])
  print('2.', story[point][1][1])
  if (3 not in exclude):
    print('3. Descipción detallada')
  if (4 not in exclude):
    print('4. Hablar con un personaje')

  choice = input()

  match choice:
    case '1':
      storyPoint(func(point, '1')[0].value)
    case '2':
      storyPoint(func(point, '2')[0].value)
    case '3':
      if 3 not in exclude:
        if point in descriptions:
          print(descriptions[point])
        else:
          print('No encuentras pistas en este momento')
        decide(point, exclude.append(3))
      else:
        decide(point, exclude)
    case '4':
      if 4 not in exclude:
        if point in dialogs:
          print(dialogs[point])
        else:
          print('Nadie está de humor para hablar ahora mismo')
        decide(point, exclude.append(4))
      else:
        decide(point, exclude)
    case _:
      decide(point, exclude)

def storyPoint(point):
  if point!='q0':
    print()

  print(story[point][0])

  if (point in dfa._final_states):
    return
  else:
    decide(point, [])