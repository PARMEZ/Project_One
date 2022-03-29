import random

name = input('Podaj swoję imię: ')
number = int(input(f'Podaj liczbę od 1 do 25: '))

bla = random.randint(1, 25)

if __name__ == "__main__":
    while number != bla:
        if bla < number:
            print(f'Przykro mi {name} Twoja liczba jest mniejsza od {number}!')
            number = int(input("Podaj liczbę: "))
        else:
            print(f"Przykro mi {name} Twoja liczba jest większa od {number}!")
            number = int(input("Podaj liczbę: "))

print(f'Brawo {name} zgadłeś!')






