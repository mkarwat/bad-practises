## Nazwa klasy i nazewnictwo zmiennych:


**CODE 1**: PiContainer, my_pies<br>
**CODE 2**: pi_container, a<br>
**Opis**: Nazwa klasy i nazwy zmiennych zostały zmienione z CamelCase na snake_case w CODE 2. Jest to zgodne z konwencjami nazewnictwa Pythona, czyniąc kod bardziej Pythonowym i poprawiając czytelność.


## Domyślny argument w konstruktorze:


**CODE 1**: Optional[List[float]] = None<br>
**CODE 2**: a=list()<br>
**Opis**: Domyślny argument w konstruktorze został zmieniony z Optional[List[float]] na a=list(). Upraszcza to kod i usuwa niepotrzebną złożoność. Używanie pustej listy jako argumentu domyślnego jest powszechną i jasną praktyką w Pythonie.


## Zmienne globalne:


**CODE 1**: Brak zmiennych globalnych.<br>
**CODE 2**: b = 0, c = 0<br>
**Opis**:  W KOD 2 zmienne globalne b i c są wprowadzane poza klasą. Może to prowadzić do potencjalnych problemów, zwłaszcza jeśli kod się rozrasta. Zmienne globalne mogą sprawić, że kod będzie trudniejszy do utrzymania i zrozumienia. Ogólnie zaleca się unikanie zmiennych globalnych, gdy jest to możliwe.


## Funkcja generatora:


**CODE 1**: calc_pi<br>
**CODE 2**: foo<br>
**Opis**: Funkcja calc_pi w CODE 1 jest funkcją generatora, która daje wartości do obliczenia liczby pi. W CODE 2 funkcja foo służy podobnemu celowi, ale ze zmiennymi globalnymi b i c. Zmiana niekoniecznie jest ulepszeniem i może sprawić, że kod będzie mniej modularny. Często lepiej jest hermetyzować taką funkcjonalność w klasie lub funkcji, tak jak to zrobiono w CODE 1.


## Funkcja wyliczająca:


**CODE 1**: enumerate_pi<br>
**CODE 2**: enumerate<br>
**Opis**:  Nazwa funkcji enumerate w CODE 2 koliduje z wbudowaną funkcją enumerate w Pythonie, która służy do iteracji po indeksach i elementach sekwencji. Może to prowadzić do nieporozumień i nieoczekiwanego zachowania. Zaleca się wybranie innej nazwy, aby uniknąć konfliktów z wbudowanymi nazwami.


## Instrukcje drukowania:


**CODE 1**: print('Wszystkie funkcje są zdefiniowane')<br>
**CODE 2**: print('Wszystkie funkcje są zdefiniowane')<br>
**Opis**: Oba kody zawierają tę samą instrukcję print wskazującą, że wszystkie funkcje są zdefiniowane. Ta instrukcja jest zwykle używana do debugowania lub sygnalizowania końca wykonywania skryptu.