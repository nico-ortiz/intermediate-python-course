import random

def main():

  dice_rolls = int(input('¿Cuantos dados te gustaria tirar?\n'))
  dice_size  = int(input('¿Cuantos lados tienen los dados?\n'))
  suma = 0

  for i in range(0, dice_rolls):
    roll  = random.randint(1, dice_size)
    suma += roll

    if roll == 1:
      print(f'¡Has obtenido un {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'¡Has obtenido un {roll}! Exito critico')
    else:
      print(f'Has lanzado un {roll}')

  print(f'Has obtenido un total de {suma}')

if __name__== "__main__":
  main()