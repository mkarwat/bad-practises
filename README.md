# The worst way to calculate π in Python

### This project shows what should be avoided when creating Python projects.

### There are many bad practises there, can you find (and correct) them all?

Your task is to clone this repository, create a new branch, fix all the issues and bad practises, add  file with list of all the changes and explanations why they are wrong. Then create a pull request with your branch, add your teacher as reviewer.

(As this project is full of bad practises please do not use it as an example. It's for educational purposes only.)


Poprawione fragmenty:
1. Nazwy file 87 i file 157 powinny zostać zmienione w taki sposób aby określały ich funkcję 
    - file 87 -> Pi_Operations
    - file 157 -> main

File 157 problemy:
1. zdefiniowana funkcja enumerate "przykrywa wbudowaną funkcję o takiej samej nazwie"
2. owa funkcja jest zdefiniowana przed importami, które powinny znajdywać się na samej górze pliku
3. Odpowiednie odstępy np. między funkcją lub importami a dalszym kodem nie są zachowane
4. Komenda from file87 import * jest zbyt ogólna i powinno być bardziej sprecyzowane co chcemy importować
5. try except nie powinno "łapać" wszystkich wyjątków. Except powinno być bardziej sprecyzowane oraz w bloku except powinno być wyjaśnienie jaki wyjątek wystąpił
6. zbyt wiele kodu w try, przez co nie wiadomo co wyrzuci wyjatek
7. Konwencja zmiennych powinna być stała 
8. brak Użycie if __name__ == '__main__' 
9. plik powiino sie otwierac z pomoca with

File 87 problemy:
1. klasa pi_container: "Class names should use CamelCase convention"
2. zamiast type(x) == list lepiej uzyc isinstance
3. zmienne typu b = 0 lub c = 0 powinny być nazwane w taki sposób aby osoba była świadoma co one oznaczają. W tym wypadku podanie wzoru matematycznego uzasadnia taki dobór.
4. wcześniej wymienione zmienne są wykorzystywane w funcji foo i tam powinny być zdefiniowane
5. Komentarze powinny być zwięzłe oraz dokładne
6. W klasie pi container nie powinno się wykorzystywać domyślnego mutowalnego argumentu
7. Powinny występować komentarze tłumaczące czytającemu zasadę działania kodu 
8. Yield powinno zawierać jeden typ zmiennych, a nie ich różne rodzaje
9. Brak występowania error handlingu
10. brak Użycie if __name__ == '__main__' w plikach