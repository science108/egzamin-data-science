# Plan nauki i weryfikacji wiedzy — droga do 100%

Cel: opanować 18 działów tak, by test jednokrotnego wyboru (40–50 pytań) rozwiązywać bez wahania. Metoda opiera się na trzech filarach: **aktywne przypominanie** (fiszki, nie tylko czytanie), **powtórki rozłożone w czasie** (spaced repetition) i **próbne testy pod warunki egzaminu**.

## Materiały w pakiecie

`skrypt-egzamin.md/.docx` — wyjaśnienia wszystkich zagadnień z rozróżnieniami „na co uważać na teście". `fiszki-egzamin.csv` — 123 fiszki pytanie/odpowiedź do importu w Anki (kolumny: pytanie, odpowiedź, dział). `testy-egzamin.md/.docx` — 64 pytania ABCD z kluczem i uzasadnieniami.

## Zasada trzech przejść przez materiał

Przez każdy dział przechodzisz trzy razy, za każdym razem inaczej, bo to wymusza inne procesy pamięciowe.

Pierwsze przejście — **zrozumienie**: przeczytaj dział w skrypcie powoli, upewnij się, że każde zdanie ma sens. Jeśli coś nie jest jasne, dopytaj lub sprawdź — nie idź dalej z luką. To jedyny etap, gdzie „czytasz".

Drugie przejście — **kodowanie**: zamknij skrypt i przerób fiszki tego działu w Anki. Kluczowe: najpierw próbujesz odpowiedzieć z głowy, dopiero potem odsłaniasz. Fiszka, którą znasz od ręki, wraca za kilka dni; fiszka, z którą się męczysz, wraca jutro. To jest spaced repetition i to on daje trwałość.

Trzecie przejście — **sprawdzenie**: rozwiąż pytania testowe z danego działu z zasłoniętym kluczem. Każda pomyłka to sygnał — wróć do odpowiedniego fragmentu skryptu i tej fiszki.

## Harmonogram

Dopasuj tempo do tego, ile masz czasu do egzaminu. Poniżej wariant 3-tygodniowy (ok. 1–1,5 h dziennie); przy krótszym czasie łącz działy, przy dłuższym rozciągnij.

**Tydzień 1 — pierwszy kontakt (przejścia 1 i 2).** Codziennie 2–3 działy: czytasz skrypt + tego samego dnia robisz fiszki. Sugerowane grupy tematyczne, żeby uczyć się powiązanego materiału razem:

- Dzień 1: UNIX (1) + Systemy operacyjne (13) — pokrewne.
- Dzień 2: Wstęp do informatyki (2) + Programowanie imperatywne/C (4).
- Dzień 3: Algorytmy (3) + Teoria obliczeń i złożoności (17).
- Dzień 4: Funkcyjne i obiektowe (5) + Automaty i języki formalne (16).
- Dzień 5: Bazy danych (6) + Inżynieria oprogramowania (10).
- Dzień 6: Technika cyfrowa (7) + Technika mikroprocesorowa (8) + Architektura (9).
- Dzień 7: Metody obliczeniowe (11) + Sztuczna inteligencja (12) + Sieci (14) + Rozproszone (15) + Współbieżność (18).

**Tydzień 2 — utrwalanie i pierwsze testy (przejścia 2 i 3).** Codziennie: 15–20 min powtórki Anki (całość, algorytm sam podsuwa zaległe) + rozwiązywanie testów z 3–4 działów dziennie. Zapisuj, które pytania mylisz.

**Tydzień 3 — symulacje egzaminu.** Rób cały zestaw 64 pytań na czas (limit ~45 min, jak na egzaminie), sprawdzaj wynik, analizuj błędy. Powtórz 2–3 razy w tygodniu. Między symulacjami dobijaj słabe działy fiszkami.

## Import fiszek do Anki (krok po kroku)

1. Zainstaluj darmowy Anki (apps.ankiweb.net) — desktop lub telefon.
2. Utwórz talię „Egzamin AGH".
3. File → Import → wskaż `fiszki-egzamin.csv`. Ustaw separator: przecinek. Pole 1 → Front (pytanie), Pole 2 → Back (odpowiedź), Pole 3 → Tag (dział, do filtrowania).
4. Ucz się codziennie — Anki sam ustala, co i kiedy powtórzyć.

Jeśli wolisz bez Anki: plik CSV otworzysz w Excelu/Arkuszach i możesz odpytywać się, zasłaniając kolumnę odpowiedzi.

## Kryterium opanowania (kiedy jesteś gotów na 100%)

Traktuj dział jako opanowany dopiero, gdy spełnia wszystkie trzy warunki: (1) każdą fiszkę działu odpowiadasz z pamięci bez podpowiedzi, (2) pytania testowe z działu robisz bezbłędnie dwa razy z rzędu, (3) potrafisz wytłumaczyć zagadnienie własnymi słowami komuś innemu (test Feynmana — jeśli się zacinasz, to luka).

Gotowość do egzaminu = **dwie pełne symulacje 64 pytań z wynikiem ≥ 95%**, przy czym błędy nie powtarzają się (każdy błąd raz zrobiony i domknięty). Dopiero wtedy 100% na egzaminie jest realne, bo materiał pokrywa się z zakresem, a Ty przećwiczyłeś dokładnie formę pytań.

## Najczęstsze pułapki testów jednokrotnego wyboru (uwaga!)

Egzaminy z tego zakresu lubią mylić pojęcia bliskie: weryfikacja vs walidacja, współbieżność vs równoległość, stronicowanie vs segmentacja, IP vs MAC, Amdahl vs Gustafson, Moore vs Mealy, soft vs hard limit, funkcjonalne vs niefunkcjonalne, distance-vector vs link-state. Te pary są w skrypcie wyróżnione — naucz się różnicy, nie tylko definicji. Druga pułapka to słowa absolutne („zawsze", „nigdy", „jedyny") — zwykle wskazują odpowiedź fałszywą, chyba że to twierdzenie ścisłe (np. „hard limit nigdy nieprzekraczalny").

## Sposób weryfikacji na bieżąco

Prowadź prostą tabelę (kartka lub arkusz): wiersze = 18 działów, kolumny = data ostatniej powtórki + status (czerwony/żółty/zielony) + liczba błędów w ostatnim teście działu. Każdy dział startuje czerwony, przechodzi w żółty po pierwszym teście, w zielony po spełnieniu kryterium opanowania. Uczysz się zawsze od najczerwieńszych. Gdy cała tabela jest zielona i masz dwie symulacje ≥95% — jesteś gotów.
