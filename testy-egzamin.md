# Baza pytań testowych — egzamin kwalifikacyjny (jednokrotny wybór)

Instrukcja: dla każdego pytania zaznacz jedną odpowiedź. Klucz z wyjaśnieniami na końcu. 60 pytań, po ~3–4 na dział. Zasłoń klucz i rozwiązuj na czas.

---

**1. Które stwierdzenie o i-węźle (inode) jest prawdziwe?**
A) Przechowuje nazwę pliku
B) Przechowuje metadane i wskaźniki na bloki, ale nie nazwę
C) Jest przechowywany w katalogu jako tekst
D) Nie istnieje w systemach UNIX

**2. Który limit quota można chwilowo przekroczyć?**
A) Twardy (hard)
B) Miękki (soft), w okresie karencji
C) Żaden
D) Oba bez ograniczeń

**3. Który mechanizm IPC jest najszybszy, ale wymaga własnej synchronizacji?**
A) Potok (pipe)
B) Sygnał
C) Pamięć dzielona
D) Kolejka komunikatów

**4. Kerberos do uwierzytelniania używa:**
A) Kluczy publicznych i certyfikatów
B) Kluczy symetrycznych, biletów i KDC
C) Wyłącznie haseł przesyłanych jawnie
D) Adresów MAC

**5. Wartość nice = -20 oznacza:**
A) Najniższy priorytet
B) Najwyższy priorytet
C) Proces zatrzymany
D) Proces w tle

---

**6. W EBNF zapis `{ X }` oznacza:**
A) Dokładnie jedno wystąpienie X
B) Opcjonalne X (0 lub 1)
C) Powtórzenie X (0 lub więcej)
D) Alternatywę

**7. Kodowanie UTF-8 znaku ASCII 'A' zajmuje:**
A) 1 bajt
B) 2 bajty
C) 4 bajty
D) Zależy od systemu

**8. W kodzie U2 na n bitach zakres liczb to:**
A) od 0 do 2ⁿ−1
B) od −2ⁿ do 2ⁿ
C) od −2^(n−1) do 2^(n−1)−1
D) od −2^(n−1)+1 do 2^(n−1)

**9. Przekazanie parametru przez wartość powoduje, że:**
A) Zmiany w funkcji modyfikują oryginał
B) Przekazywana jest kopia, oryginał bez zmian
C) Nie da się przekazać liczby
D) Argument musi być wskaźnikiem

**10. Który zapis jest w odwrotnej notacji polskiej (RPN)?**
A) (3 + 4)
B) + 3 4
C) 3 4 +
D) 3 + 4

**11. Problem nierozstrzygalny to problem, dla którego:**
A) Nie istnieje szybki algorytm
B) Nie istnieje żaden algorytm dający zawsze poprawną odpowiedź
C) Istnieje tylko algorytm wykładniczy
D) Brakuje pamięci

---

**12. Dolna granica złożoności sortowań porównaniowych to:**
A) O(n)
B) O(n log n)
C) O(n²)
D) O(log n)

**13. Który algorytm najkrótszych ścieżek radzi sobie z ujemnymi wagami?**
A) Dijkstra
B) Bellman-Ford
C) BFS
D) Sortowanie topologiczne

**14. Twierdzenie max-flow min-cut mówi, że:**
A) Maksymalny przepływ = minimalny przekrój
B) Przepływ jest zawsze zerowy
C) Nie da się policzyć przepływu
D) Przepływ = liczba wierzchołków

**15. Programowanie dynamiczne stosuje się, gdy problem ma:**
A) Niezależne podproblemy
B) Nakładające się podproblemy i optymalną podstrukturę
C) Tylko jedno rozwiązanie
D) Wyłącznie dane losowe

---

**16. Komunikat linkera „undefined reference" pojawia się na etapie:**
A) Preprocesora
B) Kompilacji
C) Konsolidacji (linkowania)
D) Wykonania

**17. Rozmiar struktury w C (`sizeof`):**
A) Zawsze równa się sumie rozmiarów pól
B) Może być większy niż suma pól z powodu wyrównania
C) Jest zawsze wielokrotnością 8
D) Nie zależy od kolejności pól

**18. Tablica VLA w C jest alokowana:**
A) Na stercie
B) Statycznie
C) Na stosie, rozmiar znany w czasie działania
D) W rejestrach

---

**19. Funkcja wyższego rzędu to funkcja, która:**
A) Ma dużo argumentów
B) Przyjmuje lub zwraca inną funkcję
C) Jest rekurencyjna
D) Zwraca liczbę

**20. Typ sumy (wariantowy) w typach algebraicznych oznacza:**
A) A i B jednocześnie
B) Albo A, albo B
C) Tablicę wartości
D) Liczbę zmiennoprzecinkową

**21. Rekursja ogonowa (tail) może być zoptymalizowana, ponieważ:**
A) Zawsze jest szybsza
B) Wywołanie rekurencyjne to ostatnia operacja — zamienia się w pętlę
C) Nie używa argumentów
D) Nie ma warunku bazowego

**22. Leniwe obliczanie (lazy) pozwala na:**
A) Szybsze wielowątkowe wykonanie
B) Nieskończone struktury danych, obliczane na żądanie
C) Automatyczne równoległe wykonanie
D) Kompilację bez błędów

---

**23. Litera „I" w ACID oznacza:**
A) Integrity
B) Isolation
C) Indexing
D) Integration

**24. Selekcja (σ) w algebrze relacji wybiera:**
A) Kolumny
B) Wiersze spełniające warunek
C) Całą tabelę
D) Klucze obce

**25. Trzecia postać normalna (3NF) eliminuje:**
A) Grupy powtarzalne
B) Zależności częściowe od klucza
C) Zależności przechodnie
D) Klucze obce

**26. Dodanie indeksu do tabeli zazwyczaj:**
A) Przyspiesza SELECT, spowalnia INSERT/UPDATE
B) Przyspiesza wszystkie operacje
C) Spowalnia SELECT
D) Nie ma żadnego wpływu

---

**27. Stan wysokiej impedancji (Z) w bramce trójstanowej oznacza:**
A) Logiczne 0
B) Logiczne 1
C) Wyjście odłączone od obwodu
D) Błąd

**28. W tablicy Karnaugha grupujemy jedynki w grupy o rozmiarze:**
A) Dowolnym
B) Potęgi liczby 2
C) Zawsze 3
D) Tylko pojedynczo

**29. Multiplekser z n liniami adresowymi obsługuje:**
A) n wejść
B) 2n wejść
C) 2ⁿ wejść
D) n² wejść

**30. Automat Mealy'ego różni się od Moore'a tym, że jego wyjście zależy od:**
A) Tylko stanu
B) Tylko wejścia
C) Stanu i wejścia
D) Zegara

**31. Który przerzutnik nie ma stanu zabronionego i przełącza się dla J=K=1?**
A) SR
B) D
C) JK
D) Brak takiego

---

**32. DMA służy do:**
A) Szyfrowania danych
B) Przenoszenia danych pamięć–I/O bez udziału CPU
C) Zwiększenia częstotliwości zegara
D) Kompresji

**33. Która pamięć wymaga cyklicznego odświeżania?**
A) SRAM
B) DRAM
C) Flash
D) ROM

**34. Cechą architektury RISC jest:**
A) Złożone rozkazy zmiennej długości
B) Proste rozkazy stałej długości, architektura load/store
C) Mało rejestrów
D) Operacje pamięć–pamięć

**35. Modyfikator `volatile` w C:**
A) Zapewnia atomowość operacji
B) Blokuje optymalizacje dostępów do zmiennej
C) Przyspiesza program
D) Alokuje pamięć na stercie

---

**36. Prawo Amdahla zakłada:**
A) Rosnący rozmiar problemu
B) Stały rozmiar problemu; ograniczenie przez część sekwencyjną
C) Nieskończoną liczbę procesorów bez ograniczeń
D) Brak części sekwencyjnej

**37. Benchmark HPCG w porównaniu do HPL (LINPACK):**
A) Mierzy tylko szczytowe FLOPS
B) Obciąża głównie pamięć i daje realistyczniejszy, niższy wynik
C) Nie jest używany
D) Działa tylko na GPU

**38. GPU wykonujące jedną instrukcję na wielu danych to według Flynna:**
A) SISD
B) SIMD
C) MISD
D) MIMD

---

**39. Walidacja oprogramowania odpowiada na pytanie:**
A) Czy budujemy produkt zgodnie ze specyfikacją?
B) Czy budujemy właściwy produkt (zgodny z potrzebami)?
C) Czy kod się kompiluje?
D) Czy testy jednostkowe przechodzą?

**40. „Czas odpowiedzi poniżej 1 s" to wymaganie:**
A) Funkcjonalne
B) Niefunkcjonalne
C) Biznesowe niemierzalne
D) Nieistotne

**41. Kanban w odróżnieniu od Scruma:**
A) Ma sprinty o stałej długości
B) Wprowadza ciągły przepływ i limity WIP, bez wyznaczonych ról
C) Nie używa tablicy
D) Wymaga Product Ownera

**42. Diagram sekwencji UML jest diagramem:**
A) Strukturalnym
B) Behawioralnym
C) Wdrożenia
D) Klas

---

**43. Kwadratura Gaussa o n węzłach jest dokładna dla wielomianów stopnia:**
A) ≤ n
B) ≤ n−1
C) ≤ 2n−1
D) ≤ n²

**44. Która cecha dotyczy arytmetyki zmiennoprzecinkowej?**
A) Dodawanie jest łączne
B) Każda liczba dziesiętna jest reprezentowana dokładnie
C) Odejmowanie bliskich liczb powoduje utratę cyfr znaczących
D) Nie występują błędy zaokrągleń

**45. Metoda Newtona-Raphsona:**
A) Jest zawsze zbieżna
B) Ma zbieżność kwadratową, ale wymaga pochodnej i dobrego startu
C) Nie wymaga funkcji
D) Jest wolniejsza od bisekcji

**46. Generator pseudolosowy przy tym samym ziarnie:**
A) Daje inną sekwencję za każdym razem
B) Daje tę samą sekwencję (jest deterministyczny)
C) Nie ma okresu
D) Wymaga sprzętu kwantowego

---

**47. Uczenie nienadzorowane charakteryzuje się:**
A) Danymi z etykietami
B) Brakiem etykiet — np. klasteryzacja, PCA
C) Predykcją wartości ciągłej
D) Regułą łańcuchową

**48. Bez nieliniowej funkcji aktywacji wielowarstwowa sieć neuronowa:**
A) Działa lepiej
B) Jest równoważna modelowi liniowemu
C) Nie da się jej uczyć w ogóle
D) Staje się rekurencyjna

**49. Algorytm A* jest optymalny, gdy heurystyka jest:**
A) Dowolna
B) Dopuszczalna (nie przeszacowuje kosztu)
C) Zawsze zerowa
D) Losowa

**50. Backpropagation oblicza gradienty za pomocą:**
A) Całkowania
B) Reguły łańcuchowej
C) Sortowania
D) Transformaty Fouriera

---

**51. Wątki tego samego procesu:**
A) Mają osobne przestrzenie adresowe
B) Współdzielą pamięć procesu
C) Nie mogą się komunikować
D) Są cięższe niż procesy

**52. Stronicowanie pamięci powoduje fragmentację:**
A) Zewnętrzną
B) Wewnętrzną
C) Żadną
D) Wyłącznie na dysku

**53. Które NIE jest jednym z czterech warunków Coffmana zakleszczenia?**
A) Wzajemne wykluczanie
B) Cykliczne oczekiwanie
C) Wywłaszczanie zasobów
D) Trzymaj i czekaj

**54. `fork()` w UNIX zwraca procesowi potomnemu wartość:**
A) PID rodzica
B) 0
C) −1 zawsze
D) Swój własny PID

---

**55. Adres MAC:**
A) Jest hierarchiczny i routowalny
B) Ma 48 bitów, jest płaski i nieroutowalny
C) Ma 32 bity
D) Zmienia się przy każdym pakiecie

**56. Protokół warstwy transportowej zapewniający niezawodność to:**
A) UDP
B) IP
C) TCP
D) ARP

**57. Router wybiera trasę na podstawie:**
A) Najkrótszego prefiksu
B) Najdłuższego pasującego prefiksu
C) Adresu MAC docelowego
D) Losowo

**58. Protokół STP (802.1d) służy do:**
A) Szyfrowania ruchu
B) Zapobiegania pętlom w sieci L2
C) Przydzielania adresów IP
D) Routingu między AS

---

**59. Zegar Lamporta gwarantuje, że jeśli a→b (happened-before), to:**
A) L(a) > L(b)
B) L(a) = L(b)
C) L(a) < L(b)
D) Nie ma zależności

**60. Problem ustalenia zwycięzcy w uogólnionych grach 2-osobowych z pełną informacją jest:**
A) W klasie P
B) PSPACE-zupełny
C) Nierozstrzygalny
D) W klasie L

**61. W hierarchii Chomsky'ego język regularny rozpoznaje:**
A) Maszyna Turinga
B) Automat ze stosem
C) Automat skończony
D) Automat liniowo ograniczony

**62. Współbieżność (concurrency) różni się od równoległości (parallelism) tym, że:**
A) Wymaga zawsze wielu rdzeni
B) Dotyczy struktury zarządzania zadaniami, możliwej też na jednym rdzeniu
C) Jest zawsze szybsza
D) Nie wymaga synchronizacji

**63. Teoria CAP mówi, że przy podziale sieci (partition) trzeba wybrać między:**
A) Spójnością (C) a dostępnością (A)
B) Szybkością a pamięcią
C) TCP a UDP
D) RISC a CISC

**64. Postać normalna Chomsky'ego dopuszcza produkcje:**
A) Dowolne
B) A→BC lub A→a
C) Tylko A→a
D) Z pustym słowem po prawej

---

# KLUCZ ODPOWIEDZI (z krótkim uzasadnieniem)

1. **B** — inode = metadane + wskaźniki na bloki, nazwa jest w katalogu.
2. **B** — soft można przekroczyć w grace period; hard nigdy.
3. **C** — pamięć dzielona najszybsza (bez kopiowania), wymaga semaforów.
4. **B** — Kerberos: klucze symetryczne, bilety, KDC; hasło nie idzie przez sieć.
5. **B** — niższa wartość nice = wyższy priorytet; -20 = najwyższy.
6. **C** — `{}` = powtórzenie 0+; `[]` = opcjonalność.
7. **A** — ASCII w UTF-8 = 1 bajt (kompatybilność).
8. **C** — U2 na n bitach: od −2^(n−1) do 2^(n−1)−1.
9. **B** — by value = kopia; oryginał niezmieniony.
10. **C** — RPN = operator po operandach: `3 4 +`.
11. **B** — nierozstrzygalny = brak jakiegokolwiek algorytmu (nie „wolny").
12. **B** — Ω(n log n) dla sortowań porównaniowych.
13. **B** — Bellman-Ford obsługuje ujemne wagi; Dijkstra nie.
14. **A** — max przepływ = przepustowość min. przekroju.
15. **B** — DP: nakładające się podproblemy + optymalna podstruktura.
16. **C** — „undefined reference" = brak symbolu przy linkowaniu.
17. **B** — padding/wyrównanie może zwiększyć sizeof; zależy od kolejności pól.
18. **C** — VLA na stosie, rozmiar znany w runtime.
19. **B** — HOF przyjmuje/zwraca funkcję (map, filter).
20. **B** — typ sumy = „albo A, albo B".
21. **B** — wywołanie rekurencyjne jest ostatnie → zamiana na pętlę (TCO).
22. **B** — lazy pozwala na nieskończone struktury liczone na żądanie.
23. **B** — Isolation (izolacja transakcji).
24. **B** — selekcja σ = wiersze; projekcja π = kolumny.
25. **C** — 3NF usuwa zależności przechodnie; 2NF częściowe.
26. **A** — indeks: szybszy SELECT, wolniejsze modyfikacje.
27. **C** — stan Z = wyjście odłączone (magistrala).
28. **B** — grupy w tablicy Karnaugha = potęgi 2.
29. **C** — n linii adresowych → 2ⁿ wejść MUX.
30. **C** — Mealy: wyjście od stanu i wejścia; Moore: tylko od stanu.
31. **C** — JK: brak stanu zabronionego, J=K=1 → toggle.
32. **B** — DMA przenosi dane bez CPU.
33. **B** — DRAM wymaga odświeżania (kondensatory).
34. **B** — RISC: proste rozkazy stałej długości, load/store.
35. **B** — volatile wyłącza optymalizacje; NIE daje atomowości.
36. **B** — Amdahl: stały rozmiar, limit przez część sekwencyjną.
37. **B** — HPCG memory-bound, realistyczniejszy, niższy wynik niż HPL.
38. **B** — SIMD = jedna instrukcja, wiele danych (GPU/wektory).
39. **B** — walidacja = właściwy produkt (potrzeby); weryfikacja = wobec specyfikacji.
40. **B** — wymaganie niefunkcjonalne (jakość/wydajność).
41. **B** — Kanban: ciągły przepływ, limity WIP, bez ról; Scrum ma sprinty i role.
42. **B** — diagram sekwencji = behawioralny.
43. **C** — Gauss n-węzłowy dokładny do stopnia 2n−1.
44. **C** — odejmowanie bliskich liczb → utrata cyfr (cancellation).
45. **B** — Newton: kwadratowa zbieżność, wymaga pochodnej i dobrego startu.
46. **B** — PRNG deterministyczny: to samo ziarno = ta sama sekwencja.
47. **B** — nienadzorowane = bez etykiet (klasteryzacja, PCA).
48. **B** — bez nieliniowości sieć = model liniowy.
49. **B** — A* optymalny dla heurystyki dopuszczalnej.
50. **B** — backprop = reguła łańcuchowa.
51. **B** — wątki dzielą pamięć procesu.
52. **B** — stronicowanie → fragmentacja wewnętrzna; segmentacja → zewnętrzna.
53. **C** — warunkiem jest BRAK wywłaszczania; „wywłaszczanie" nie jest warunkiem Coffmana.
54. **B** — fork zwraca 0 dziecku, PID dziecka rodzicowi.
55. **B** — MAC = 48 bitów, płaski, nieroutowalny.
56. **C** — TCP niezawodny; UDP zawodny.
57. **B** — longest prefix match.
58. **B** — STP zapobiega pętlom L2.
59. **C** — a→b ⇒ L(a) < L(b) (implikacja jednostronna).
60. **B** — PSPACE-zupełny (QBF, naprzemienne kwantyfikatory).
61. **C** — język regularny ↔ automat skończony (typ 3).
62. **B** — współbieżność = struktura, możliwa na jednym rdzeniu; równoległość = wiele jednostek.
63. **A** — przy partycji wybór między C a A.
64. **B** — CNF: A→BC lub A→a.
