b = 0
c = 0  # zmienne globalne nie maja typu


class pi_container:  # nazwy klas powinno sie zaczynac od duzej litery
    def __init__(self, a=list()):  # uzywamy listy ktora jest "mutable", powinnismy uzyc tuple zamiast listy(?)
        self.a = a

    def mth(self, x):  # nazwaa metody nie wskazuje na to co bedzie robic
        if type(x) == list:  # zle porownanie typu, lepiej uzyc "isinstance()")
            self.a += x
        else:
            self.a.append(x)


def foo(x):  # nazwa metody nie wskazuje na to co bedzie robic, nie okreslamy typu argumentu(?)
    global b  # tworzymy zmienna globalna wewnatrz funkcji
    global c  # zmienne nie opisują same siebie
    b = 0  #
    c=1  # nie czytelny zapis
    '''
    '''
    for hello in range(x):  # komentarz ponizej jest za dlugi, powinien sie znajdowac na poczatku prgramu,
        if hello % 2 == 0:  # brakuje 2 spacji przed początkiem
            b += 4 / c#this is a very important operation in calculateing pi according to documentation that is provided in a seperate file in this repository, please analyse this file before using!
        else:
            b -= 4 / c
        c += 2
        yield b  # wyjatki nie sa obslugiwane
    yield 'finished'

def enumerate(pi: pi_container):  # przeciazenie wbudowanej funkcji
    for hello in pi.a:  # odwolujemy sie do obiektu klasy poza klasą
        print(hello)


print('All functions are defined')  # po co to ?