import random

name = input('Podaj swoję imię: ')
number = int(input('Podaj liczbę: '))

bla = random.randint(1, 5)

if __name__ == "__main__":
    if number == bla:
        print(f'Brawo {name} zgadłeś!')
    else:
        print(f'Niestety {name}, nie udało Ci się!')



