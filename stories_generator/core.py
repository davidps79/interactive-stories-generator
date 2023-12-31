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

  def nameMenu(self):
    print("Ingrese su nombre para comenzar el juego:")
    self.name = input()
    self.mainMenu()

  def mainMenu(self):
    print(' ')
    print('Bienvenido ' + self.name)
    print(' ')
    print('Ingresa una de las siguientes opciones:' )
    print(' ')
    print('Iniciar juego')
    print('Personalizar nombre')
    print(' ')

    while True:
      choice = validate(input())
      match choice:
        case 4:
          print(' ')
          print('Iniciando nueva partida...')
          print(' ')
          self.storyPoint('q0')
        case 5:
          self.changeNames()
        case _:
          print('Ingresa una cadena valida')
      if (choice==4 or choice==5):
        break
    self.finalMenu()
  
  def finalMenu(self):
    print(' ')
    print('Has finalizado el juego. ¿Deseas volver a jugar?')
    print(' ')
    print('Ingresa:')
    print(' ')
    print('Volver a jugar')
    print('Finalizar juego')

    while True:
      choice = validate(input())
      match choice:
        case 6:
          self.start()
        case 7:
          print(' ')
          print('Adios')
        case _:
          print(' ')
          print('Ingresa una cadena valida')
      if (choice==6 or choice==7):
        break
    
  
  def start(self):
    self.nameMenu()
  
  def storyPoint(self, point):
    if point!='q0':
      print()

    self.type_effect(self.story[point][0])

    if (point in self.final_states):
      return
    else:
      self.decide(point, [])

  def decide(self, point, exclude):
    print('\nEs momento de decidir...')
    self.type_effect(f'1. {self.story[point][1][0]}')
    self.type_effect(f'2. {self.story[point][1][1]}')
    if (3 not in exclude):
      print('3. Descipcion detallada')
    if (4 not in exclude):
      print('4. Hablar con alguien')
    print(' ')

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
              print(' ')
              print(descriptions[point])
            else:
              print(' ')
              print('No encuentras pistas en este momento')
            exclude.append(3)

          self.decide(point, exclude)
        case 1:
          if 4 not in exclude:
            print(' ')
            print(self.interactions.generateDialog());
            exclude.append(4)
          else:
            print(' ')
            print('Nadie está de humor para hablar ahora mismo')
          self.decide(point, exclude)
        case _:
          print(' ')
          print("Ingresa un cadena valida")
      
      if (choice==2 or choice == 3 or choice==8 or choice==1):
        break
  
  def changeNames(self):
    print(' ')
    print('Menu de cambio de nombres')
    print('Nombres que puedes cambiar: ')
    print(' ')
    counter=1
    for i in self.customization.names:
      print(str(counter)+'-'+i)
      counter+=1
    print(' ')
    print('Ingresa el nombre que deseas cambiar:')
    print(' ')
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
      print(' ')
      print('Ingresa una cadena valida')
    print(' ')
    print('Ahora ingresa el nombre por el cual quieres reemplazar:')

    output_name=input()
    self.customization.changeAll(input_name,output_name, self.story)
    print(' ')
    print('Cambios efectuados con exito')
    self.mainMenu()