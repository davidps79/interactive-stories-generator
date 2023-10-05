from data import descriptions
from validations import validate
import time

class Core:
  def type_effect(self, string):
    for char in string:
      print(char, end='', flush=True)
      if char=='.':
        time.sleep(0.3)
      if char==',' or char==';':
        time.sleep(0.15)
      else:
        time.sleep(0.03)
    print('')

  def __init__(self, story, descriptions, automaton, interactions, customization):
    self.interactions = interactions
    self.customization = customization
    self.final_states = automaton.dfa._final_states
    self.func = automaton.dfa._transition_function
    self.story = story
    self.descriptions = descriptions

  def mainMenu(self):
    print('Bienvenido')
    print('Ingresa una de las siguientes opciones:' )
    print('Iniciar juego')
    print('Personalizar nombre')

    while True:
      choice = validate(input())
      match choice:
        case 4:
          print('Iniciando nueva partida...')
          self.storyPoint('q0')
        case 5:
          self.changeNames()
        case _:
          print('Ingresa una cadena valida')
      if (choice==4 or choice==5):
        break
  
  def start(self):
    self.mainMenu()
  
  def storyPoint(self, point):
    if point!='q0':
      print()

    self.type_effect(self.story[point][0])

    if (point in self.final_states):
      return
    else:
      self.decide(point, [])

  def decide(self, point, exclude):
    print('Es momento de decidir...')
    self.type_effect(f'1. {self.story[point][1][0]}')
    self.type_effect(f'2. {self.story[point][1][1]}')
    if (3 not in exclude):
      print('3. Descipción detallada')
    if (4 not in exclude):
      print('4. Hablar con un personaje')

    while True:
      choice = validate(input())
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
            exclude.append(3)

          self.decide(point, exclude)
        case 1:
          if 4 not in exclude:
            print(self.interactions.generateDialog());
            exclude.append(4)
          else:
            print('Nadie está de humor para hablar ahora mismo')
          self.decide(point, exclude)
        case _:
          print("Ingresa un cadena valida")
      
      if (choice==2 or choice == 3 or choice==8 or choice==1):
        break
  
  def changeNames(self):
    print('Menu de cambio de nombres')
    print('Nombres que puedes cambiar: ')
    counter=1
    for i in self.customization.names:
      print(str(counter)+'-'+i)
      counter+=1

    print('Ingresa el nombre que deseas cambiar:')
    exist=False
    input_name=""
    while True:
      input_name = input()
      for i in self.customization.names:
        if i == input_name:
          exist=True
          break
      if exist == True:
        break
      print('Ingresa una cadena valida')

    print('Ahora ingresa el nombre por el cual quieres reemplazar:')

    output_name=input()
    self.customization.changeAll(input_name,output_name, self.story)
    print('Cambios efectuados con exito')
    self.mainMenu()