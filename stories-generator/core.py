from data import descriptions
from story_automaton import dfa
from validations import validate
from interactions import generateDialog
from customization import changeAll

class Core:

  def __init__(self, story, dialogs, descriptions):
    self.func = dfa._transition_function
    self.story = story
    self.dialogs = dialogs
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

    print(self.story[point][0])

    if (point in dfa._final_states):
      return
    else:
      self.decide(point, [])

  def decide(self, point, exclude):
    print('Es momento de decidir...')
    print('1.', self.story[point][1][0])
    print('2.', self.story[point][1][1])
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
  
  def changeNames(self):
    nombres = ["Alex Mercer", "Los renegados","El informante","Sarah Ramirez","Los Cerebros Libres"]
    print('Menu de cambio de nombres')
    print('Nombres que puedes cambiar: ')
    counter=1
    for i in nombres:
      print(str(counter)+'-'+i)
      counter+=1

    print('Ingresa el nombre que deseas cambiar:')
    exist=False
    input_name=""
    while True:
      input_name = input()
      for i in nombres:
        if i == input_name:
          exist=True
          break
      if exist == True:
        break
      print('Ingresa una cadena valida')

    print('Ahora ingresa el nombre por el cual quieres reemplazar:')

    output_name=input()

    changeAll(input_name,output_name)

    print('Cambios efectuados con exito')

    




