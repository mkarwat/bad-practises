1) nazwy plików są ciężkie do zrozumienia
2) używanie zmiennych globalnych jest złą praktyką
3) nazwa klasy powinna byc napisana camelCase a nie snake_case
4) importy powinny byc na samej gorze i powinno sie importowac poszczegolne rzeczy, a nie uzywac *
5) zmienne powinny miec nazwy zrozumiale dla czytajacego kod
6) zamiast type(x) == list lepiej uzyc isinstance
7) nazwa funkcji foo() jest niezrozumiala
8) komentarz w fukcji foo nie wnosi nic waznego, lepiej zastopic go dokladnym opisem funkcji w docstringu
9) niepotrzebne yield 'finished', ktore zwraca inny typ
10) brak uzycia if __name__ == '__main__' w plikach
11) stworzenie funkcjii enumerate, ktorej nazwa przyslania funkcje wbudowana
12) wielokrotne powtarzanie my_pi.mth(pi_gen.__next__()) - powinno to byc w petli
13) zbyt wiele kodu w bloku try, przez co nie wiadomo co wyrzuci wyjatek
14) po except powinno sie lapac wyjatki
15) plik powinno sie otwierac za pomoca with
