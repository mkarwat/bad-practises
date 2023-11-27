## Nazwy funkcji:

**Zmiana**: Zmieniono nazwę funkcji z enumerate na enumerate_pi.<br>
**Powód**: Unika konfliktów nazewnictwa z wbudowaną funkcją enumerate. Zapewnia bardziej opisową nazwę dla przejrzystości.

## Obsługa wyjątków:

**Zmiana**: Używa określonych typów wyjątków (ValueError, FileNotFoundError, EOFError) w oddzielnych blokach except.<br>
**Powód**: Poprawa obsługi błędów poprzez wychwytywanie określonych wyjątków, co ułatwia identyfikację i obsługę różnych scenariuszy błędów.

## Zapis pliku:

**Zmiana**: Używa menedżera kontekstu (z open) do zapisu plików.<br>
**Powód**: Zapewnia prawidłowe zamknięcie pliku po zapisie, nawet jeśli wystąpi wyjątek. Jest to czystszy i bardziej Pythoniczny sposób obsługi operacji na plikach.

## Nazwy funkcji i klas:

**Zmiana**: Używa bardziej opisowych nazw, takich jak my_pi, my_pi_2, my_pi_3 i pi_gen dla instancji i generatorów.<br>
**Powód**: Zwiększa czytelność i przejrzystość kodu. Opisowe nazwy ułatwiają zrozumienie przeznaczenia zmiennych i obiektów.

## Użycie zmiennej:

**Zmiana**: Używa bardziej opisowych nazw zmiennych, takich jak pi_gen w pętli.<br>
**Powód**: Poprawia czytelność kodu i utrzymuje spójność. Opisowe nazwy zmiennych sprawiają, że kod nie wymaga wyjaśnień.

## Zamykanie plików:

**Zmiana**: Używa menedżera kontekstu (z open) do zapisu pliku, który automatycznie zamyka plik.<br>
**Powód**: Zapewnia prawidłowe zamknięcie pliku, nawet w przypadku wystąpienia wyjątku. Upraszcza obsługę plików i zmniejsza ryzyko wycieku zasobów.

## Wcięcie:

**Zmiana**: Utrzymuje spójne wcięcia w całym kodzie.<br>
**Powód**: Spójne wcięcia zwiększają czytelność kodu i są zgodne z wytycznymi stylu PEP 8.


## Wywołanie metody:

**Zmiana**: Używa next(pi_gen) zamiast pi_gen.__next__(), aby pobrać następny element z generatora. <br>
**Powód**: Funkcja next() jest zalecanym sposobem uzyskania następnego elementu z iteratora. Jest bardziej czytelna i zgodna z konwencjami Pythona.

## Komentarze:

**Zmiana**: Komentarz # result = a + b /c jest obecny w CODE 1, ale brakuje go w CODE 2.<br>
**Powód**: Komentarze pomagają dokumentować kod. Jeśli komentarz zawiera cenne informacje, warto go dołączyć dla przyszłych czytelników kodu.