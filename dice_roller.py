import random

def main():

  suma = 0
  dice_rolls = 2  
  for i in range(0, dice_rolls):
    roll  = random.randint(1, 6)
    print(f'Has lanzado un {roll}')
    suma += roll

  print(f'Has obtenido un total de {suma}')

if __name__== "__main__":
  main()