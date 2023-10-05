import random
from pyformlang.cfg import CFG

# Lista de comentarios
comments = [
    "¿Crees que el nuevo alcalde cumplirá sus promesas electorales?",
    "Estoy emocionado por el concierto de la semana próxima, ¿te gustaría ir?",
    "La tecnología avanza tan rápido, a veces me cuesta mantenerme al día.",
    "La comida en ese restaurante nuevo es increíble, deberías probarla.",
    "El tráfico de hoy estuvo insoportable, ¿no crees?",
    "La lectura es una excelente forma de escapar de la rutina diaria.",
    "No puedo creer lo caros que son los precios de la vivienda en esta ciudad.",
    "¿Qué opinas sobre la educación en línea? ¿Crees que es efectiva?",
    "El clima últimamente es tan impredecible, nunca sabes qué esperar.",
    "¿Alguna vez has considerado hacer un viaje espontáneo? A veces es justo lo que necesitas."
]

# Lista de respuestas
answers = [
    "Sí, pero la clave está en mantenernos informados y responsables como ciudadanos.",
    "¡Claro! Será genial disfrutar de buena música juntos.",
    "Estoy de acuerdo, cada día aparece algo nuevo en el mercado.",
    "Definitivamente, he escuchado muchas críticas positivas sobre ese lugar.",
    "Totalmente, parece que el tráfico empeora cada año.",
    "Completamente de acuerdo, los libros tienen ese poder especial.",
    "Es una locura, ¿verdad? Espero que haya cambios pronto.",
    "Creo que puede ser muy efectiva si tienes la disciplina para ello.",
    "Sí, el cambio climático está teniendo un impacto real en nuestro clima.",
    "¡Sí! A veces, lo inesperado trae las mejores aventuras."
]

insults = [
  'A a veces tu obsesión por demostrar que eres más listo te lleva a pasar por alto detalles cruciales',
  'No todo es código y algoritmos, a veces se necesita sentido común y experiencia',
  'A veces te aferras tanto a tus métodos tradicionales que pierdes las oportunidades que la tecnología podría ofrecer',
  'Si no te actualizas, te quedará atrás en este mundo en constante evolución',
  'Sólo espero que la justicia prevalezca y que no logres comprarla también',
  'La tecnología no lo es todo; parece que perdiste lo humano en esta búsqueda de perfección mecánica',
  'Tus motivos son egoístas. No todos merecen ser glorificados',
  'Sólo quieres ver arder el mundo',
  'Hasta los androides más viejos de NeoTech tienen más sentido común que tú',
  'No vale la pena hablar contigo',
  'Te falla, no?'
]

silence = [
  'No vale la pena opinar..',
  '(Guarda silencio)',
  'Preferiría no hablar contigo',
  'No estoy de acuerdo...'
]

cfg1 = CFG.from_text("""
S -> A | B | E I | E | I
E -> a f
A -> a b
B -> A f
I -> i i
""")

def generateDialog():
  l = []
  for i in list(cfg1.get_words(max_length = 4)):
    l.append(''.join([x.to_text() for x in i]))

  preDialog = random.choice(l)
  result=""
  for i in preDialog:
    match i:
      case 'a':
        result+= random.choice(comments) +"\n"
      case 'b':
        result+= random.choice(answers) +"\n"
      case 'f':
        result+= random.choice(silence) +"\n"
      case 'i':
        result+= random.choice(insults) +"\n"
  return result
