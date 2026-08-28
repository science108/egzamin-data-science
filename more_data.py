# -*- coding: utf-8 -*-
# Deep-dive ("rozwinięcie") explanations, keyed by exact term string.
MORE = {}
def add(term, md):
    MORE[term] = md.strip()

add("PAM (moduły uwierzytelniania)", r"""
**Najprościej:** PAM to ochroniarz przy drzwiach, którego sposób sprawdzania możesz wymieniać jak klocki — bez przebudowywania całego budynku (aplikacji).

**Po co to jest?** Kiedyś każdy program (login, ssh) sam sprawdzał hasło. PAM wyciąga to na zewnątrz: program pyta PAM „wpuścić?", a PAM sam decyduje wg konfiguracji z `/etc/pam.d/`.

**4 typy modułów (co sprawdzają):**
- **auth** — kim jesteś (hasło, odcisk palca)
- **account** — czy konto jest ważne, godziny dostępu
- **password** — zmiana hasła
- **session** — sprzątanie na wejściu/wyjściu (np. montowanie katalogu)

**Flagi kontrolne** decydują, jak ważny jest wynik modułu: `required`, `requisite`, `sufficient`, `optional`.

**⚠️ Na egzaminie:** PAM = elastyczność bez rekompilacji aplikacji. Znaj 4 typy i flagi.
""")

add("System plików / i-węzeł (inode)", r"""
**Najprościej:** wielkie drzewo z jednym pniem `/`. Każdy plik ma metryczkę (inode), a jego imię wisi osobno.

**Inode (i-węzeł)** to dowód osobisty pliku: właściciel, prawa, rozmiar, wskaźniki na bloki danych — **ale NIE nazwa**.

**Nazwa** żyje w katalogu, który jest zwykłą tablicą par `nazwa → numer inode`. Dlatego jeden plik (inode) może mieć wiele nazw.

**Typy plików:** zwykły, katalog, dowiązanie, urządzenie znakowe/blokowe, potok (FIFO), gniazdo.

**⚠️ Na egzaminie:** inode NIE zawiera nazwy pliku — nazwa jest w katalogu.
""")

add("Dowiązania (hard link / symlink)", r"""
**Najprościej:** to dwa sposoby, żeby plik miał „drugie imię".

**Hard link (twarde)** — kolejna nazwa wskazująca **ten sam inode**. Jak dwa imiona tej samej osoby: usuniesz jedno, osoba dalej żyje pod drugim. Działa tylko w obrębie **jednego systemu plików**.

**Symlink (miękkie)** — malutki plik zawierający **ścieżkę** do celu: karteczka „idź tam →". Może wskazywać na inny dysk, ale jak usuniesz cel, karteczka wisi w próżnię (martwe dowiązanie).

**⚠️ Na egzaminie:** hard link nie przekracza granicy systemu plików, symlink tak; symlink pokazuje ścieżkę, hard link ten sam inode.
""")

add("ACL (listy kontroli dostępu)", r"""
**Najprościej:** zwykłe prawa `rwx` znają tylko trzy grupy: właściciel, jego grupa, cała reszta. ACL to lista gości VIP.

**Problem:** co jeśli chcesz dać dostęp Ani, ale NIE Tomkowi z tej samej grupy? Zwykłe prawa tego nie umieją.

**ACL** pozwala dopisać uprawnienia dla **konkretnych** użytkowników i grup, niezależnie od klasycznej trójki. Polecenia: `getfacl`, `setfacl`.

**Maska** ogranicza maksymalne prawa dla wpisów rozszerzonych (sufit uprawnień).

**⚠️ Na egzaminie:** ACL = drobnoziarnista kontrola przekraczająca model owner/group/other.
""")

add("Quota (kontyngenty)", r"""
**Najprościej:** limit miejsca w szafie, żeby jeden użytkownik nie zajął całego dysku.

**Co się liczy (dwa rodzaje):**
- **bloki** — ile miejsca (przestrzeń)
- **i-węzły** — ile plików

**Dwa progi:**
- **miękki (soft)** — możesz przekroczyć na chwilę, w okresie karencji (grace period)
- **twardy (hard)** — ściana, ani bajta więcej

**⚠️ Na egzaminie:** soft można chwilowo przekroczyć, hard nigdy; quota liczy i bloki, i inody.
""")

add("Tryb użytkownika i jądra (syscall)", r"""
**Najprościej:** ty (program) nie wchodzisz do kuchni — prosisz kelnera (jądro), a on obsługuje.

**Dwa tryby:**
- **user mode** — twój program, ograniczone prawa
- **kernel mode** — jądro, pełen dostęp do sprzętu

**Wywołanie systemowe (syscall)** to prośba do jądra (czytaj plik, otwórz sieć). Powoduje **przełączenie kontekstu** user → kernel i z powrotem.

**Kontekst procesu** = stan rejestrów, licznik rozkazów, stos, mapa pamięci. Przełączanie kontekstu zapisuje/odtwarza ten stan — i **kosztuje** czas.

**⚠️ Na egzaminie:** syscall = przejście user→kernel; przełączenie kontekstu nie jest darmowe.
""")

add("Priorytet procesu (nice)", r"""
**Najprościej:** miejsce w kolejce do procesora. Wartość `nice` działa **na odwrót** niż intuicja.

**Skala nice:** od **-20** (najwyższy priorytet, „wpycham się") do **+19** (najniższy, „przepuszczam wszystkich").

**Zasada:** im **niższa** wartość nice, tym **wyższy** priorytet.

**Kto może co:** zwykły użytkownik może tylko być grzeczniejszy (zwiększać nice = obniżać priorytet). Podniesienie priorytetu wymaga uprawnień. Polecenia: `nice`, `renice`.

**⚠️ Na egzaminie:** niższy nice = wyższy priorytet; użytkownik bez roota nie podniesie priorytetu.
""")

add("IPC (komunikacja między procesami)", r"""
**Najprościej:** sposoby, jak dwa programy do siebie gadają.

**Główne mechanizmy:**
- **potok (pipe)** — jednokierunkowa rura, między spokrewnionymi procesami
- **FIFO (potok nazwany)** — rura między dowolnymi procesami
- **kolejka komunikatów** — skrzynka na listy
- **pamięć dzielona** — wspólna tablica korkowa, **najszybsza** (brak kopiowania), ale wymaga własnej synchronizacji
- **semafory** — do synchronizacji (kto ma dostęp)
- **gniazda (sockets)** — także przez sieć
- **sygnały** — krótkie „puknięcie", przenoszą bardzo mało informacji

**⚠️ Na egzaminie:** pamięć dzielona najszybsza, ale sam pilnujesz porządku; sygnał niesie minimum informacji.
""")

add("LDAP", r"""
**Najprościej:** wielka książka telefoniczna firmy, ułożona jak drzewo.

**Co przechowuje:** informacje o użytkownikach, grupach, zasobach — w strukturze drzewa (**DIT**).

**Jak identyfikujemy wpis:** przez **DN (Distinguished Name)** — pełną ścieżkę w drzewie. Wpis opisany atrybutami wg schematu.

**Zoptymalizowany pod ODCZYT** — dużo czytania, mało zapisów (jak książka adresowa, którą rzadko się zmienia).

**Zastosowanie:** scentralizowane logowanie, książki adresowe.

**⚠️ Na egzaminie:** LDAP = katalog, hierarchia, DN, szybki odczyt.
""")

add("Kerberos", r"""
**Najprościej:** system biletów jak w wesołym miasteczku — pokazujesz hasło raz, dostajesz bilet i nim wchodzisz na wszystkie karuzele.

**Jak to działa (krok po kroku):**
1. Logujesz się do **KDC** (centrum, = AS + TGS)
2. Dostajesz **TGT** — bilet „na bilety"
3. TGT-em prosisz o bilety do konkretnych usług
4. Usługa ufa biletowi — **hasło nigdy nie wędruje przez sieć**

Opiera się na **kluczach symetrycznych** i **znacznikach czasu** (dlatego zegary muszą być zsynchronizowane).

**Zastosowanie:** Single Sign-On, Active Directory.

**⚠️ Na egzaminie:** bilety, KDC, klucze symetryczne, wymóg zsynchronizowanych zegarów.
""")

add("EBNF (notacja gramatyki)", r"""
**Najprościej:** przepis, jak budować poprawne zdania w języku programowania.

**Znaczenie nawiasów (to najczęściej pytają):**
- `[ ... ]` — opcjonalne (możesz pominąć)
- `{ ... }` — powtórzenie 0 lub więcej razy
- `( ... )` — grupowanie
- `|` — alternatywa (wybierz jedno)

**Reguły produkcji** definiują symbole **nieterminalne** (do rozwinięcia) przez **terminalne** (gotowe znaki).

**⚠️ Na egzaminie:** `{}` = powtórzenie, `[]` = opcjonalne — nie pomyl ich.
""")

add("Składnia, semantyka, pragmatyka", r"""
**Najprościej:** trzy pytania o zdanie: czy dobrze zapisane, czy ma sens, po co je mówisz.

**1. Składnia (syntax) —** forma zapisu (poprawna „pisownia" i gramatyka kodu).
**2. Semantyka —** znaczenie konstrukcji (co program właściwie robi).
**3. Pragmatyka —** sposób i cel użycia (po co, w jakim kontekście).

**Przykład:** `x = "tekst" + 5` może być poprawne składniowo, ale bez sensu semantycznie.

**⚠️ Na egzaminie:** składnia ≠ semantyka — program poprawny składniowo może być bez sensu.
""")

add("Zabezpieczenia przed błędami", r"""
**Najprościej:** barierki, które łapią wpadki w kodzie, najlepiej jak najwcześniej.

**Główne mechanizmy:**
- **kontrola typów** (silne/statyczne typowanie) — nie zmieszasz liczby z tekstem
- **kontrola zakresów tablic** — nie wyjdziesz poza koniec
- **obsługa wyjątków** — łapiesz błąd, zamiast się wywalić
- **inicjalizacja zmiennych**, **hermetyzacja**, `const`/niemodyfikowalność
- sprawdzanie zgodności argumentów funkcji

**⚠️ Na egzaminie:** silne typowanie wychwytuje błędy wcześniej; brak kontroli granic tablic = klasyczne źródło błędów w C.
""")

add("Procedury i funkcje", r"""
**Najprościej:** siekanie wielkiego zadania na małe, nazwane kawałki, których używasz wiele razy.

**Po co to (główne cele):**
- **modularność** — dziel i panuj
- **reużywalność** — nie powtarzaj się (zasada **DRY**)
- **abstrakcja** — ukryj szczegóły za nazwą
- **czytelność** i łatwiejsze testowanie/utrzymanie

**Różnica:** **funkcja** zwraca wartość, **procedura** wykonuje działanie.

**⚠️ Na egzaminie:** główny cel to dekompozycja i reużywalność — NIE „przyspieszenie programu".
""")

add("Typy numeryczne (int, float)", r"""
**Najprościej:** liczby całkowite są jak klocki (dokładne), zmiennoprzecinkowe jak gumowa miarka (przybliżone).

**Całkowite (int):** ze znakiem lub bez, różne rozmiary. W swoim zakresie **dokładne**.

**Zmiennoprzecinkowe (float/double, IEEE 754):** mają **skończoną precyzję** → błędy zaokrągleń. Nie zapiszą idealnie wielu ułamków dziesiętnych.

**Przykład:** `0.1 + 0.2` w komputerze to nie dokładnie `0.3`.

**⚠️ Na egzaminie:** float ≠ dokładna reprezentacja ułamków dziesiętnych.
""")

add("Typy strukturalne", r"""
**Najprościej:** pudełka na dane — jedne mieszają różne rzeczy, inne trzymają same jednakowe.

**Rekord / struktura —** pola **różnych** typów (imię, wiek, wzrost). **Heterogeniczna.**
**Tablica —** elementy **tego samego** typu, jak pudełko na jajka. **Homogeniczna.**
Inne: unia, zbiór, lista.

**Po co:** grupować powiązane dane w jedną całość.

**⚠️ Na egzaminie:** struktura = heterogeniczna, tablica = homogeniczna.
""")

add("UTF-8 (kodowanie znaków)", r"""
**Najprościej:** sposób zapisu liter w komputerze o **zmiennej długości** (1–4 bajty na znak).

**Jak to działa:**
- ASCII (0–127) — **1 bajt** (zgodność wsteczna, zwykłe angielskie litery)
- znaki spoza ASCII (np. `ą`, emoji) — 2, 3 lub 4 bajty

**Rozpoznawanie bajtów:** bajt wiodący zaczyna się od `110…`/`1110…`/`11110…` (mówi ile bajtów), bajty kontynuacji od `10…`.

**⚠️ Na egzaminie:** UTF-8 jest zmiennobajtowe, zgodne z ASCII na 1 bajcie; bajt kontynuacji zaczyna się od `10`.
""")

add("Przekazywanie parametrów", r"""
**Najprościej:** dajesz koledze kserokopię albo oryginał.

**Przez wartość (by value) —** kopia argumentu. Kolega bazgrze po kserze, twój oryginał czysty. Zmiany **nie** wychodzą na zewnątrz.

**Przez referencję/wskaźnik (by reference) —** dostęp do oryginału. Zmiany **widoczne** na zewnątrz.

Inne: przez wynik, przez wartość-wynik, przez nazwę (leniwe).

**⚠️ Na egzaminie:** by value nie zmienia oryginału; w C tablice przekazywane efektywnie „przez wskaźnik".
""")

add("Lambda w Pythonie", r"""
**Najprościej:** malutka funkcja bez imienia, jednorazówka pisana w locie.

**Zapis:** `lambda x: x + 1` — weź `x`, oddaj `x+1`.

**Gdzie się używa:** jako krótki argument do `map`, `filter`, `sorted(key=...)`.

**Ograniczenia:** tylko **jedno wyrażenie**, brak instrukcji (pętli, przypisań), brak `return` (wynik wyrażenia jest zwracany automatycznie).

**⚠️ Na egzaminie:** lambda zwraca wartość wyrażenia bez `return`; nie zawiera pętli ani przypisań.
""")

add("Rekurencja", r"""
**Najprościej:** funkcja, która woła samą siebie — jak lustro w lustrze.

**Dwie części każdej rekurencji:**
1. **Warunek bazowy (STOP)** — najprostszy przypadek, bez wołania siebie
2. **Krok rekurencyjny** — wołanie siebie na **mniejszym** problemie

**Przykład (schody):** żeby zejść z 10 stopni → zejdź o 1, potem rozwiąż „jak zejść z 9". Aż dojdziesz do 0 (STOP).

**Uwaga:** brak warunku STOP = nieskończone wołanie i przepełnienie stosu.

**⚠️ Na egzaminie:** każda rekurencja musi mieć przypadek bazowy.
""")

add("Złożoność sortowań", r"""
**Najprościej:** ile pracy trzeba, żeby ułożyć klocki po kolei — jedne metody są mądre, inne mozolne.

**Wolne — `O(n²)`:** bąbelkowe, przez wstawianie, przez wybór. Dużo porównań, dobre tylko dla małych danych.

**Szybkie — `O(n log n)`:**
- **merge sort** — zawsze `n log n`, **stabilne**, ale potrzebuje dodatkowej pamięci
- **quicksort** — średnio `n log n`, w miejscu, ale **pesymistycznie `n²`**
- **heapsort** — `n log n` w miejscu, niestabilne

**Ściana:** żadne sortowanie **porównaniowe** nie zejdzie poniżej `Ω(n log n)`.
**Wyjątek:** sortowania pozycyjne (counting/radix) robią `O(n)`, ale tylko przy założeniach o kluczach (nie porównują).

**⚠️ Na egzaminie:** dolna granica porównaniowych = `n log n`; quicksort pesymistycznie `n²`.
""")

add("Algorytmy zachłanne (greedy)", r"""
**Najprościej:** łakomczuch — w każdym kroku bierze to, co teraz wygląda najlepiej, i nigdy się nie cofa.

**Jak działa:** `WYBIERZ lokalnie najlepsze → nie cofaj → powtarzaj`.

**Kiedy daje optimum:** gdy problem ma **własność wyboru zachłannego** i **optymalną podstrukturę**.

**Działa (optimum):** kod Huffmana, drzewo rozpinające (Kruskal), wydawanie reszty w „ładnych" systemach monet.
**Nie działa:** plecak 0/1 (tu trzeba pomyśleć naprzód — programowanie dynamiczne).

**⚠️ Na egzaminie:** zachłanny NIE zawsze daje optimum globalne; Huffman i MST — tak.
""")

add("Najkrótsze ścieżki (Dijkstra, Bellman-Ford)", r"""
**Najprościej:** szukanie najtańszej drogi na mapie — trzy różne narzędzia do trzech sytuacji.

**1. Dijkstra —** jedno źródło, **wagi nieujemne**, zachłanny. Szybki: `O((V+E) log V)` z kopcem.
**2. Bellman-Ford —** dopuszcza **wagi ujemne**, wykrywa ujemne cykle. Wolniejszy: `O(V·E)`.
**3. Floyd-Warshall —** **wszystkie pary** naraz, programowanie dynamiczne: `O(V³)`.

**⚠️ Na egzaminie:** Dijkstra NIE działa dla ujemnych wag; Floyd-Warshall = wszystkie pary.
""")

add("Techniki projektowania algorytmów", r"""
**Najprościej:** to różne sposoby myślenia o rozwiązaniu problemu. Zależnie od problemu — labirynt, klocki czy pudełko cukierków — wybierasz inną strategię.

**1. Brute force — „sprawdzę wszystko"**
Masz 10 kluczy i nie wiesz który pasuje — próbujesz każdego. **Idea:** sprawdź wszystkie możliwości. **+** proste i pewne, **−** bywa bardzo wolne.

**2. Dziel i zwyciężaj — „podziel duży problem"**
Wielka sterta klocków: dzielisz na dwie, porządkujesz każdą, łączysz. **Idea:** `PODZIEL → ROZWIĄŻ → POŁĄCZ`. Przykład: merge sort, wyszukiwanie binarne.

**3. Zachłanny — „biorę najlepsze teraz"**
Wydajesz 8 zł: bierzesz największą pasującą monetę, potem kolejną. **Idea:** w każdym kroku wybierz to, co teraz najlepsze. **⚠️** lokalnie najlepsze ≠ zawsze globalnie najlepsze.

**4. Programowanie dynamiczne — „zapamiętuję, co policzyłem"**
Ta sama zagadka drugi raz? Zaglądasz do notatek zamiast liczyć od nowa. **Idea:** `rozbij → rozwiąż mniejsze → zapamiętaj → używaj ponownie`. Przykład: Fibonacci, plecak.

**5. Backtracking — „spróbuję, a jak źle to się cofnę"**
Labirynt: wybierasz drogę, ślepa uliczka → wracasz do skrzyżowania. **Idea:** `WYBIERZ → SPRAWDŹ → jeśli źle: COFNIJ`. Przykład: Sudoku, hetmany.

**6. Zamiatanie / redukcja —** przesuwasz „miotłę" przez dane (geometria) albo sprowadzasz problem do już rozwiązanego.

**⚠️ Na egzaminie:** DP dla **nakładających się** podproblemów; dziel-i-zwyciężaj dla **niezależnych**.
""")

add("Reprezentacja grafów", r"""
**Najprościej:** graf to mapa z kropkami (wierzchołki) i liniami (krawędzie). Są dwa sposoby jej zapisu.

**1. Macierz sąsiedztwa —** wielka tabela „kto z kim". Sprawdzenie krawędzi **`O(1)`**, ale zajmuje **`O(V²)`** pamięci. Dobra dla grafów **gęstych**.

**2. Lista sąsiedztwa —** dla każdego wierzchołka lista jego sąsiadów. Pamięć **`O(V+E)`**, szybka iteracja po sąsiadach. Dobra dla grafów **rzadkich**.

(Jest też macierz incydencji: wierzchołki × krawędzie.)

**⚠️ Na egzaminie:** macierz = szybkie sprawdzenie krawędzi + dużo pamięci; lista = oszczędna dla rzadkich.
""")

add("Maksymalny przepływ (max-flow/min-cut)", r"""
**Najprościej:** rury z wodą od źródła `s` do kranu `t` — ile wody przepłynie maksymalnie?

**Sieć przepływowa:** krawędzie mają **przepustowości** (ile się zmieści).

**Kluczowe twierdzenie (max-flow = min-cut):** maksymalny przepływ równa się przepustowości **najwęższego przekroju** (najcieńszego „gardła" rozcinającego graf na część z `s` i część z `t`).

**Algorytmy:** Ford-Fulkerson (ścieżki powiększające), Edmonds-Karp (BFS, `O(V·E²)`).

**⚠️ Na egzaminie:** wartość max przepływu = przepustowość minimalnego przekroju.
""")

add("Programowanie dynamiczne", r"""
**Najprościej:** rozwiązujesz zagadkę krok po kroku i zapisujesz wyniki na karteczkach, żeby nie liczyć tego samego dwa razy.

**Kiedy się nadaje (dwa warunki):**
1. **nakładające się podproblemy** — te same mniejsze zadania wracają wielokrotnie
2. **optymalna podstruktura** — optimum całości składa się z optimów części

**Dwa style:**
- **top-down (memoizacja)** — liczysz normalnie, ale zapamiętujesz wyniki
- **bottom-up (tablica)** — wypełniasz tabelę od najmniejszych przypadków

**Przykłady:** Fibonacci, plecak, najdłuższy wspólny podciąg, Floyd-Warshall.

**⚠️ Na egzaminie:** DP zamienia koszt wykładniczy na wielomianowy dzięki zapamiętywaniu.
""")

add("Budowa programu z kodu C", r"""
**Najprościej:** kod C jedzie taśmą przez 4 stacje, zanim stanie się programem.

**Cztery etapy (kolejność!):**
1. **Preprocesor** — rozwija `#include`, `#define`, dyrektywy
2. **Kompilator** — C → asembler/kod obiektowy, sprawdza składnię
3. **Asembler** — tworzy plik obiektowy `.o`
4. **Linker (konsolidacja)** — skleja pliki `.o` i biblioteki w plik wykonywalny, rozwiązuje symbole

**Diagnoza błędów:** błąd „undefined reference" pojawia się na etapie **linkowania** (brakuje definicji funkcji).

**⚠️ Na egzaminie:** preprocesor → kompilator → asembler → linker.
""")

add("Tablica 2D do funkcji", r"""
**Najprościej:** dając funkcji tabelę (wiersze i kolumny), musisz jej zdradzić liczbę kolumn.

**Dlaczego:** w C tablica „rozpada się" (decay) do wskaźnika. Żeby policzyć adres kratki `a[i][j]`, kompilator musi znać **liczbę kolumn** `N`.

**Zapis:** `void f(int a[][N])` albo `int (*a)[N]`. Alternatywnie: wskaźnik + wymiary podane jawnie.

**⚠️ Na egzaminie:** rozmiar **pierwszego** wymiaru można pominąć, **drugiego (i dalszych) — nie**.
""")

add("Tablice VLA", r"""
**Najprościej:** tablica, której rozmiar poznajesz dopiero w trakcie działania programu.

**Zapis:** `int a[n];` gdzie `n` to zmienna (C99).

**Gdzie leży:** na **stosie** (podręczna półka). Stąd zaleta i wada:
- **+** wygoda (nie musisz z góry znać rozmiaru)
- **−** ryzyko **przepełnienia stosu** dla dużych `n`, brak sprawdzania

W C11 VLA są opcjonalne.

**⚠️ Na egzaminie:** VLA żyją na stosie, rozmiar znany dopiero w runtime.
""")

add("Padding / wyrównanie struktur", r"""
**Najprościej:** komputer lubi układać dane w równych rządkach, więc czasem wstawia puste przerwy między polami.

**Dlaczego:** procesor szybciej czyta pola leżące pod „ładnymi" adresami (wyrównanie/alignment). Kompilator dokłada **padding** (luki), by tak było.

**Skutek:** `sizeof(struct)` ≥ suma rozmiarów pól, i **zależy od kolejności pól**. Poukładanie pól od największych do najmniejszych zwykle zmniejsza padding.

**⚠️ Na egzaminie:** rozmiar struktury zależy od wyrównania i kolejności pól — nie zawsze = suma `sizeof` pól.
""")

add("qsort()", r"""
**Najprościej:** gotowa maszynka ze `stdlib`, która posortuje cokolwiek jej dasz.

**Wywołanie:** `qsort(baza, liczba, rozmiar_elementu, komparator)`.

**Sekret uniwersalności:** działa na `void*`, więc nie wie, co sortuje — dlatego **ty** dajesz jej **komparator**: funkcję zwracającą `<0`, `0`, `>0` (który element pierwszy).

**Wydajność:** średnio `O(n log n)`.

**⚠️ Na egzaminie:** qsort wymaga funkcji porównującej i **nie jest stabilne** wg standardu.
""")

add("Funkcja wyższego rzędu", r"""
**Najprościej:** funkcja, która przyjmuje inną funkcję jako prezent albo oddaje funkcję.

**Dwa przypadki (wystarczy jeden):**
- przyjmuje funkcję jako argument (np. `map(f, lista)`)
- zwraca funkcję jako wynik

**Klasyczne przykłady:** `map` (zrób coś z każdym elementem), `filter` (zostaw pasujące), `reduce/fold` (zwiń do jednej wartości), kompozycja funkcji.

**⚠️ Na egzaminie:** HOF operuje na funkcjach; `map` i `filter` to sztandarowe przykłady.
""")

add("Typ algebraiczny (ADT)", r"""
**Najprościej:** budujesz nowy typ z innych na dwa sposoby: „albo-albo" oraz „i-i".

**1. Typ sumy (wariant/union) — „albo A, albo B".**
Np. `Maybe` (jest wartość ALBO jej brak), `Either` (wynik ALBO błąd). W danej chwili to **jeden** z wariantów.

**2. Typ iloczynu (rekord/krotka) — „A i B naraz".**
Np. punkt = `(x, y)` — oba pola jednocześnie.

**Pattern matching** rozróżnia, który wariant sumy właśnie mamy, i rozpakowuje pola.

**⚠️ Na egzaminie:** suma = wybór jednego wariantu; iloczyn = kombinacja pól.
""")

add("Funktor i monada", r"""
**Najprościej:** to „pudełka", w których obliczasz, nie wyjmując zawartości na stół.

**Funktor —** pudełko, które umie `map`: zmieniasz zawartość, **struktura pudełka zostaje**. Np. `map (+1) [1,2,3] = [2,3,4]` — lista dalej jest listą.

**Monada —** funktor, który dodatkowo umie **ustawiać obliczenia w kolejkę** z jakimś bagażem/kontekstem:
- `Maybe` — obliczenia, które mogą się nie udać
- `IO` — obliczenia z efektem (wejście/wyjście)
- `List` — obliczenia z wieloma wynikami

**Po co monada:** porządkuje sekwencję kroków „jedno po drugim", automatycznie przenosząc kontekst (np. jak coś zwróci `Nothing`, reszta się nie wykonuje).

**⚠️ Na egzaminie:** funktor = `map` pod strukturą; monada = sekwencjonowanie obliczeń z kontekstem.
""")

add("Polimorfizm (parametryczny / ad-hoc)", r"""
**Najprościej:** „polimorfizm" = jeden zapis działa dla wielu typów, ale na dwa różne sposoby.

**1. Parametryczny (generyki) —** DOKŁADNIE ta sama funkcja dla wszystkich typów. Np. `length :: [a] -> Int` liczy długość dowolnej listy, nie zaglądając w elementy.

**2. Ad-hoc (przeciążanie, klasy typów) —** ta sama nazwa, ale **różne implementacje** dla różnych typów. Np. `+` dla liczb dodaje, dla napisów skleja.

**⚠️ Na egzaminie:** generyki = parametryczny; klasy typów / przeciążanie = ad-hoc.
""")

add("Rekursja ogonowa", r"""
**Najprościej:** rekursja, w której wywołanie samej siebie jest **ostatnią** czynnością.

**Dlaczego to ważne:** skoro po powrocie nie ma już nic do zrobienia, komputer nie musi pamiętać starej ramki — może ją **nadpisać**. Zamienia rekursję w zwykłą pętlę (**TCO** — optymalizacja wywołań ogonowych). Efekt: **stała pamięć stosu**.

**Kontrast:** rekursja **nieogonowa** (np. drzewiasta jak Fibonacci — dwa wywołania) rośnie na stosie.

**Sztafeta:** oddajesz pałeczkę i od razu schodzisz z bieżni — nie czekasz.

**⚠️ Na egzaminie:** rekursja ogonowa może być zoptymalizowana (TCO) i nie zapycha stosu.
""")

add("Leniwe obliczanie (lazy)", r"""
**Najprościej:** „policzę to dopiero, jak naprawdę będzie potrzebne" — i zapamiętam wynik.

**Nazwa techniczna:** call-by-need. Wartość liczona przy pierwszym użyciu, potem trzymana gotowa.

**Co to daje:**
- **nieskończone struktury** — możesz mieć „nieskończoną listę", bo bierzesz z niej tylko tyle, ile chcesz
- unikanie zbędnych obliczeń

**Przeciwieństwo:** gorliwe (eager/strict) — liczy od razu. Lazy króluje w Haskellu.

**⚠️ Na egzaminie:** lazy = obliczenie odroczone; pozwala na nieskończone listy/strumienie.
""")

add("Cechy obiektowości (4 filary)", r"""
**Najprościej:** cztery zasady, na których stoi programowanie obiektowe.

**1. Abstrakcja —** pokazuj tylko to, co istotne; resztę pomiń.
**2. Hermetyzacja (enkapsulacja) —** schowaj stan (bebechy) za interfejsem (guzikami).
**3. Dziedziczenie —** dziecko przejmuje cechy rodzica; hierarchia i ponowne użycie.
**4. Polimorfizm —** jeden interfejs, wiele implementacji (przycisk „graj" działa różnie na różnych urządzeniach).

**⚠️ Na egzaminie:** to klasyczna czwórka; hermetyzacja ≠ dziedziczenie.
""")

add("ACID (własności transakcji)", r"""
**Najprościej:** cztery gwarancje bezpiecznej operacji w bazie — jak przelew, który albo cały przejdzie, albo cały się cofnie.

**1. Atomicity (atomowość) —** wszystko albo nic. Jak coś padnie w połowie, cała transakcja jest cofana.
**2. Consistency (spójność) —** baza przechodzi z jednego poprawnego stanu do drugiego (reguły zawsze zachowane).
**3. Isolation (izolacja) —** równoległe transakcje nie zakłócają się wzajemnie.
**4. Durability (trwałość) —** zatwierdzone zmiany przetrwają nawet awarię prądu (zapis na dysk).

**⚠️ Na egzaminie:** izolacja dotyczy współbieżności, trwałość — awarii.
""")

add("Model związków encji (ERD)", r"""
**Najprościej:** rysunek „kto z czym się łączy", robiony ZANIM zbudujesz bazę.

**Trzy elementy:**
- **encje** — rzeczy/obiekty (Uczeń, Klasa)
- **atrybuty** — cechy encji (imię, wiek)
- **związki** — relacje między encjami, z **licznością**: `1:1`, `1:N`, `M:N`

**Ważny przypadek:** związek **`M:N`** (wielu do wielu) w modelu relacyjnym wymaga dodatkowej **tabeli łączącej**.

**⚠️ Na egzaminie:** M:N → tabela pośrednicząca; ERD to model konceptualny, podstawa schematu.
""")

add("Klucze (główny, obcy)", r"""
**Najprościej:** różne rodzaje „identyfikatorów" wiersza w tabeli.

**1. Superklucz —** dowolny zbiór atrybutów jednoznacznie wskazujący krotkę (może mieć nadmiar).
**2. Klucz kandydujący —** **minimalny** superklucz (bez zbędnych atrybutów).
**3. Klucz główny (primary) —** wybrany kandydujący. **Unikalny i NOT NULL** (jak PESEL).
**4. Klucz obcy (foreign) —** odwołanie do klucza w innej tabeli. Zapewnia **integralność referencyjną** (nie wskażesz nieistniejącego wiersza).

**⚠️ Na egzaminie:** klucz główny ≠ NULL i unikalny; obcy spina tabele i pilnuje integralności.
""")

add("Algebra relacji", r"""
**Najprościej:** podstawowe klocki, z których zbudowany jest SQL.

**Najważniejsze operacje:**
- **selekcja `σ`** — wybiera **WIERSZE** spełniające warunek
- **projekcja `π`** — wybiera **KOLUMNY**
- **złączenie `⋈` (join)** — skleja relacje po warunku
- **iloczyn kartezjański `×`** — każdy z każdym
- suma `∪`, różnica `−`, przecięcie `∩`, przemianowanie `ρ`

**Pamiętaj:** `σ` = wiersze (poziomo), `π` = kolumny (pionowo).

**⚠️ Na egzaminie:** to teoretyczna podstawa SQL; join łączy relacje po warunku.
""")

add("Normalizacja (postacie normalne)", r"""
**Najprościej:** sprzątanie bazy, żeby nie trzymać tej samej informacji w wielu miejscach (redundancja i anomalie).

**Kolejne poziomy porządku:**
1. **1NF —** wartości atomowe, brak grup powtarzalnych (jedna komórka = jedna wartość)
2. **2NF —** 1NF + brak **zależności częściowej** od klucza (nieklucz zależy od CAŁEGO klucza)
3. **3NF —** 2NF + brak **zależności przechodnich** (nieklucz nie zależy od innego niekluczu)
4. **BCNF —** mocniejsza wersja 3NF

**Cena:** mniej redundancji, ale więcej złączeń przy zapytaniach.

**⚠️ Na egzaminie:** 2NF usuwa zależności częściowe, 3NF — przechodnie.
""")

add("Widoki (views)", r"""
**Najprościej:** okno pokazujące wybrany fragment danych — samo danych **nie przechowuje**.

**Czym jest:** wirtualna tabela zdefiniowana zapytaniem. Za każdym użyciem liczy się na bieżąco z tabel źródłowych.

**Po co:**
- **uproszczenie** skomplikowanych zapytań
- **bezpieczeństwo** — pokaż tylko wybrane kolumny/wiersze, ukryj poufne
- **niezależność logiczna**

**Wyjątek:** widok **materializowany** faktycznie zapisuje wynik (zajmuje miejsce, trzeba odświeżać).

**⚠️ Na egzaminie:** zwykły widok nie zajmuje miejsca na dane; materializowany — tak.
""")

add("Indeksy", r"""
**Najprościej:** skorowidz na końcu książki — błyskawicznie znajdujesz stronę, ale trzeba go pielęgnować.

**Jak działa:** dodatkowa struktura (najczęściej **B-drzewo**, czasem hasz) wskazująca, gdzie leżą wiersze.

**Kompromis:**
- **+** przyspiesza `SELECT` (wyszukiwanie)
- **−** spowalnia `INSERT/UPDATE/DELETE` (każda zmiana musi zaktualizować indeks) i zajmuje miejsce

**Typ ma znaczenie:** B-drzewo dobre dla **zakresów** (`>`, `<`, `BETWEEN`), hasz dla **równości** (`=`).

**⚠️ Na egzaminie:** indeks przyspiesza odczyt, spowalnia zapisy.
""")

add("Bramki trójstanowe (stan Z)", r"""
**Najprościej:** zwykła bramka daje 0 albo 1. Trójstanowa ma trzecią opcję: „odłączam się".

**Trzeci stan — wysoka impedancja (Z):** wyjście jest jak **wyciągnięta wtyczka** — ani 0, ani 1, po prostu odcięte. Sterowane sygnałem **enable**.

**Po co:** wiele urządzeń może dzielić jeden wspólny kabel — **magistralę**. W danej chwili tylko **jedno** wyjście jest aktywne, reszta w stanie Z.

**⚠️ Na egzaminie:** stan Z = odcięcie od magistrali; klucz do współdzielenia szyny.
""")

add("Tablice Karnaugha", r"""
**Najprościej:** rysunek-siatka, który pomaga uprościć skomplikowaną logikę bez algebry.

**Jak działa:**
1. Wpisujesz wartości funkcji do siatki, gdzie **sąsiednie komórki różnią się jednym bitem** (kod Graya)
2. **Zakreślasz grupy jedynek** — grupy muszą być potęgą 2 (`1, 2, 4, 8…`)
3. Większa grupa = eliminuje więcej zmiennych = prostsze wyrażenie

**Sztuczka:** grupy „owijają się" na brzegach tablicy (lewy brzeg sąsiaduje z prawym).

**⚠️ Na egzaminie:** grupy = potęgi 2 i owijają się; większa grupa = prostszy wynik.
""")

add("Układy synchroniczne i asynchroniczne", r"""
**Najprościej:** jedne robią wszystko na wspólny rytm, drugie reagują natychmiast.

**Synchroniczne —** zmiany stanu taktowane wspólnym **zegarem**. Jak taniec do rytmu: przewidywalne, łatwiejsze w projektowaniu.

**Asynchroniczne —** reagują od razu na zmianę wejść, **bez zegara**. Szybsze, ale podatne na **hazardy** (wyścigi sygnałów) i trudniejsze.

**⚠️ Na egzaminie:** synchroniczny = wspólny zegar; asynchroniczny = brak zegara, ryzyko wyścigów.
""")

add("Multiplekser / demultiplekser", r"""
**Najprościej:** MUX to przełącznik kanałów, DEMUX robi odwrotnie.

**MUX (multiplekser) —** z **wielu wejść** wybiera **jedno wyjście**, wg linii adresowych. `n` linii wyboru obsłuży **`2ⁿ`** wejść. To jak przełącznik kanałów TV — może zrealizować dowolną funkcję logiczną.

**DEMUX (demultiplekser) —** jedno wejście kieruje na **jedno z wielu wyjść**.

**⚠️ Na egzaminie:** `n` linii adresowych → `2ⁿ` wejść MUX.
""")

add("Hazardy", r"""
**Najprościej:** krótkie, niechciane „mignięcia" na wyjściu, bo sygnały docierają różnymi drogami w różnym czasie.

**Skąd się biorą:** różne **opóźnienia propagacji** ścieżek — jeden sygnał przychodzi ciut później i przez moment wyjście jest błędne.

**Rodzaje:**
- **statyczny** — wyjście powinno być stałe, a pojawia się krótki impuls
- **dynamiczny** — przy zmianie pojawiają się dodatkowe przełączenia

**Leczenie:** dodatkowe (redundantne) składniki logiczne, synchronizacja zegarem.

**⚠️ Na egzaminie:** hazard = skutek różnic opóźnień; groźny w układach asynchronicznych.
""")

add("Rejestry", r"""
**Najprościej:** malutka pamięć na jedno „słowo" bitów, zbudowana z przerzutników.

**Rodzaje:**
- **równoległy (parallel)** — wszystkie bity wchodzą/wychodzą naraz
- **przesuwający (shift)** — bity wędrują po kolei, bit po bicie

**Zastosowanie rejestru przesuwnego:** konwersja **szeregowo↔równolegle** (SIPO/PISO), a także mnożenie/dzielenie przez 2 (przesunięcie bitów).

**⚠️ Na egzaminie:** rejestr przesuwny konwertuje szereg↔równolegle i przesuwa bity.
""")

add("Liczniki", r"""
**Najprościej:** układy, które liczą impulsy — jak licznik kliknięć.

**Dwa rodzaje:**
- **asynchroniczny (ripple)** — przerzutniki taktowane **kaskadowo** (jeden wyzwala następny). Wolniejszy, bo opóźnienie się **narasta**.
- **synchroniczny** — wszystkie przerzutniki taktowane **wspólnym zegarem** naraz. Szybszy, bez narastającego opóźnienia.

Liczą modulo N, w górę lub w dół.

**⚠️ Na egzaminie:** licznik synchroniczny szybszy i bez narastającego opóźnienia.
""")

add("Sumatory i półsumatory", r"""
**Najprościej:** układy dodające bity — jak dodawanie w słupku z przenoszeniem.

**Półsumator (half adder) —** dodaje **2 bity**, daje sumę i przeniesienie (carry-out). **Nie ma** wejścia przeniesienia.

**Sumator pełny (full adder) —** dodaje **3 bity** (dwa dane + carry-in z poprzedniej kolumny), daje sumę i carry-out.

**Łączenie:** kaskada pełnych sumatorów = sumator równoległy (ripple carry) dla wielobitowych liczb.

**⚠️ Na egzaminie:** half adder NIE ma wejścia carry, full adder MA.
""")

add("Przerzutniki (flip-flopy)", r"""
**Najprościej:** najmniejsze pudełeczka pamiętające **1 bit** (0 albo 1).

**Rodzaje:**
- **SR (set/reset)** — ustaw/zeruj, ma **stan zabroniony** (S=R=1)
- **D (data)** — zapamiętuje to, co dostanie na wejściu (zatrzask danych)
- **JK** — uniwersalny, **brak stanu zabronionego**, dla J=K=1 się przełącza (toggle)
- **T (toggle)** — przy każdym takcie zmienia stan (do liczników)

**Wyzwalanie:** poziomem (latch) lub zboczem zegara (edge).

**⚠️ Na egzaminie:** JK usuwa stan zabroniony SR; T służy do liczników.
""")

add("Automaty (Moore / Mealy)", r"""
**Najprościej:** maszyny stanów (FSM) — chodzą po „pokojach" (stanach). Różnią się tym, od czego zależy wyjście.

**Moore —** wyjście zależy **tylko od stanu** (od tego, w którym pokoju jesteś).

**Mealy —** wyjście zależy **od stanu i od wejścia** (od pokoju ORAZ którymi drzwiami wchodzisz). Zwykle mniej stanów i szybsza reakcja.

Opis: graf stanów, tablica przejść.

**⚠️ Na egzaminie:** Moore = wyjście od stanu; Mealy = od stanu i wejścia.
""")

add("Układy kombinacyjne i sekwencyjne", r"""
**Najprościej:** jedne mają pamięć, drugie nie.

**Kombinacyjne —** wyjście zależy **tylko od bieżących wejść**, brak pamięci. Jak kalkulator: te same wejścia → te same wyjścia. Przykłady: bramki, MUX, sumatory, dekodery.

**Sekwencyjne —** wyjście zależy od wejść **i stanu** (mają pamięć tego, co było). Przykłady: przerzutniki, rejestry, liczniki, automaty.

**⚠️ Na egzaminie:** kombinacyjny = bez pamięci; sekwencyjny = z pamięcią stanu.
""")

add("DMA (bezpośredni dostęp do pamięci)", r"""
**Najprościej:** pomocnik, który przenosi dane między pamięcią a urządzeniem I/O **bez angażowania procesora**.

**Jak działa (krok po kroku):**
1. CPU zleca kontrolerowi DMA transfer i wraca do swoich zadań
2. DMA sam przenosi dane (dysk ↔ pamięć)
3. Po zakończeniu DMA zgłasza **przerwanie**

**Koszt:** DMA „podkrada" cykle magistrali (**cycle stealing**), ale i tak mocno odciąża CPU przy dużych transferach.

**⚠️ Na egzaminie:** DMA odciąża CPU; kradnie cykle magistrali.
""")

add("SRAM vs DRAM", r"""
**Najprościej:** dwie pamięci — jedna szybka i droga, druga tania i „dziurawa".

**SRAM (statyczna) —** bit trzymany w **przerzutniku**. Szybka, droga, **nie wymaga odświeżania**. Używana w **cache**.

**DRAM (dynamiczna) —** bit w **kondensatorze**, który się rozładowuje, więc trzeba go ciągle **odświeżać**. Tania, gęsta, wolniejsza. To **pamięć główna** (RAM).

**⚠️ Na egzaminie:** DRAM wymaga odświeżania i jest wolniejsza; SRAM siedzi w cache.
""")

add("Pamięć Flash", r"""
**Najprościej:** pamięć, która pamięta nawet po odcięciu prądu (pendrive, SSD).

**Cechy:**
- **nieulotna** — trzyma dane bez zasilania
- elektrycznie kasowalna (odmiana EEPROM), ale **kasowana blokami** (nie pojedynczy bajt)
- **ograniczona liczba cykli** zapisu/kasowania — komórki się **zużywają**

**Typy:** NOR (szybki odczyt losowy, do kodu) i NAND (gęsta, do danych, dyski SSD).

**⚠️ Na egzaminie:** Flash nieulotna, kasowana blokowo, ograniczona żywotność komórek.
""")

add("RISC vs CISC", r"""
**Najprościej:** proste klocki LEGO kontra gotowe, złożone zabawki.

**RISC —** mało **prostych** rozkazów **równej długości**, zwykle 1 cykl, dużo rejestrów, architektura **load/store** (pamięć tylko przez load/store). Łatwe **potokowanie**. Np. ARM, RISC-V.

**CISC —** dużo **złożonych** rozkazów **zmiennej długości**, operacje pamięć-pamięć, mniej rejestrów. Np. x86.

**⚠️ Na egzaminie:** RISC = proste, stałej długości, łatwy pipeline; CISC = złożone, zmiennej długości.
""")

add("Pipelining (potokowe wykonanie)", r"""
**Najprościej:** taśma produkcyjna dla rozkazów — gdy jeden jest myty, drugi już suszony.

**Fazy rozkazu** (np. 5): pobranie → dekodowanie → wykonanie → dostęp do pamięci → zapis. W potoku **kilka rozkazów naraz**, każdy na innym etapie.

**Zysk:** większa **przepustowość** (więcej rozkazów na sekundę). Ale **nie skraca** czasu pojedynczego rozkazu.

**Zagrożenia (hazardy):** strukturalne (brak zasobu), danych (rozkaz czeka na wynik), sterowania (skoki psują taśmę).

**⚠️ Na egzaminie:** potok zwiększa przepustowość; skoki powodują hazardy sterowania.
""")

add("volatile w C/C++", r"""
**Najprościej:** karteczka na zmiennej: „UWAGA, mogę zmienić się sama z zewnątrz".

**Co robi:** mówi kompilatorowi **nie optymalizuj** dostępów — każdy odczyt naprawdę sięga do pamięci (nie używaj zapamiętanej wartości z rejestru).

**Kiedy potrzebne:** rejestry sprzętowe, zmienne zmieniane przez **przerwanie (ISR)**, inny wątek czy sprzęt.

**Czego NIE robi:** nie zapewnia **atomowości** ani synchronizacji między wątkami.

**⚠️ Na egzaminie:** volatile wyłącza optymalizację odczytów/zapisów; to nie jest mechanizm synchronizacji.
""")

add("Pamięć podręczna (cache)", r"""
**Najprościej:** mała, superszybka półka tuż przy procesorze na rzeczy używane najczęściej — żeby nie biegać do wielkiej, wolnej szafy (RAM).

**Dlaczego działa (lokalność):**
- **czasowa** — jak użyłeś czegoś, pewnie zaraz użyjesz znowu
- **przestrzenna** — pewnie sięgniesz po dane obok

**Poziomy:** L1 (najmniejszy, najszybszy) → L2 → L3.

**Trafienie/chybienie:** **hit** = jest w cache (szybko), **miss** = trzeba sięgnąć do wolniejszej pamięci.

**Wada:** koszt, złożoność (spójność cache w wieloprocesorach).

**⚠️ Na egzaminie:** cache działa dzięki lokalności; miss = sięgnięcie do wolniejszej pamięci.
""")

add("Prawo Amdahla i Gustafsona", r"""
**Najprościej:** dwa spojrzenia na to, ile zyskasz, dokładając procesorów.

**Amdahl (pesymistyczny) —** dla **stałego** problemu część **sekwencyjna** (`s`) hamuje. Maksymalne przyspieszenie = `1 / (s + (1−s)/p)`. Nawet 1000 procesorów nie przeskoczy tej sekwencyjnej części.

**Gustafson (optymistyczny) —** dla **rosnącego** problemu przyspieszenie skaluje się liniowo — mając więcej procesorów, bierzesz po prostu **większe** zadanie.

**⚠️ Na egzaminie:** Amdahl = stały rozmiar (pesymistyczny); Gustafson = skalowany rozmiar (optymistyczny).
""")

add("Benchmarki HPL i HPCG", r"""
**Najprościej:** dwa testy prędkości superkomputerów, które mierzą co innego.

**HPL (LINPACK) —** rozwiązuje **gęsty** układ równań. Mierzy szczytową moc obliczeniową (**FLOPS**), jest podstawą listy **TOP500**. Faworyzuje surową moc (compute-bound) — pokazuje ładne, wysokie wyniki.

**HPCG —** **rzadkie** macierze, wzorzec bliski realnym aplikacjom. Obciąża **pamięć i komunikację** (memory-bound). Daje niższe, „uczciwsze" wyniki.

**⚠️ Na egzaminie:** HPL = moc obliczeniowa; HPCG = przepustowość pamięci, realistyczniejszy.
""")

add("Taksonomia Flynna", r"""
**Najprościej:** podział komputerów wg „ile strumieni instrukcji i ile strumieni danych naraz".

**Cztery klasy:**
- **SISD —** jeden robotnik, jedno zadanie (klasyczny jednoprocesor)
- **SIMD —** jedna instrukcja, wielu robotników na różnych danych (**GPU**, wektory)
- **MISD —** rzadki, egzotyczny przypadek
- **MIMD —** wielu robotników, każdy swoje (wieloprocesory, **klastry**)

**⚠️ Na egzaminie:** GPU/wektory = SIMD; klaster wielordzeniowy = MIMD.
""")

add("Wydajność komputera", r"""
**Najprościej:** szybkość to NIE tylko zegar (GHz).

**Co się składa na wydajność:**
- częstotliwość zegara
- **IPC** — ile instrukcji na cykl
- liczba rdzeni
- hierarchia i **przepustowość pamięci** (cache, RAM), I/O

**Miary:** FLOPS, IPS, czas wykonania. Uwaga na **ścianę pamięci** i granice skalowania (Amdahl).

**⚠️ Na egzaminie:** sama częstotliwość nie decyduje — liczy się IPC, rdzenie, pamięć.
""")

add("Model kaskadowy (waterfall)", r"""
**Najprościej:** budowa krok po kroku jak schody — każda faza kończy się, zanim zacznie się następna.

**Kolejność faz:** wymagania → projekt → implementacja → testy → wdrożenie → utrzymanie.

**Zalety:** prostota, dobra dokumentacja, jasne kamienie milowe.
**Wady:** sztywność, **późne wykrycie błędów**, kosztowne zmiany, klient widzi efekt dopiero na końcu.

**⚠️ Na egzaminie:** waterfall = sekwencyjny, słaby przy zmiennych wymaganiach.
""")

add("Zwinne vs klasyczne", r"""
**Najprościej:** „zaplanuj wszystko z góry" kontra „rób małymi kroczkami i dostosowuj się".

**Klasyczne (waterfall, V-model) —** planowanie z góry, sztywne, dużo dokumentacji, **predykcyjne**.

**Zwinne (agile) —** iteracyjno-przyrostowe, **adaptacja do zmian**, częste dostarczanie, ścisła współpraca z klientem, mniej dokumentacji.

**⚠️ Na egzaminie:** agile = iteracyjne i elastyczne; klasyczne = predykcyjne i sekwencyjne.
""")

add("Agile Manifesto", r"""
**Najprościej:** cztery wartości mówiące, co jest ważniejsze przy wytwarzaniu oprogramowania.

**Cztery wartości (lewe ważniejsze):**
1. **Ludzie i interakcje** ponad procesy i narzędzia
2. **Działające oprogramowanie** ponad obszerną dokumentację
3. **Współpraca z klientem** ponad negocjacje umów
4. **Reagowanie na zmiany** ponad realizację planu

Do tego 12 zasad.

**⚠️ Na egzaminie:** „ponad" ≠ „zamiast" — prawa strona też ma wartość, lewa większą.
""")

add("Poziomy testów", r"""
**Najprościej:** testujemy na piętrach — od jednego klocka po całą budowlę.

**Poziomy (od dołu):**
1. **jednostkowe** — pojedynczy moduł/funkcja osobno
2. **integracyjne** — czy moduły współpracują
3. **systemowe** — cały system jako całość
4. **akceptacyjne** — czy spełnia wymagania **klienta** (klient zatwierdza)

**Rodzaje:** czarnoskrzynkowe/białoskrzynkowe, regresji, wydajnościowe.

**⚠️ Na egzaminie:** jednostkowe = najniższy poziom; akceptacyjne robi/zatwierdza klient.
""")

add("Weryfikacja i walidacja", r"""
**Najprościej:** dwa różne pytania kontrolne o produkt.

**Weryfikacja — „czy budujemy produkt POPRAWNIE?"**
Zgodność ze **specyfikacją**. Czy zrobiliśmy dokładnie to, co zapisano.

**Walidacja — „czy budujemy WŁAŚCIWY produkt?"**
Zgodność z **potrzebami** użytkownika. Czy to w ogóle jest to, czego on chciał.

**⚠️ Na egzaminie:** weryfikacja = wobec specyfikacji; walidacja = wobec potrzeb.
""")

add("Wymagania funkcjonalne i niefunkcjonalne", r"""
**Najprościej:** CO system ma robić kontra JAK dobrze ma to robić.

**Funkcjonalne —** konkretne funkcje i zachowania. Np. „system ma logować użytkownika".

**Niefunkcjonalne (jakościowe) —** wydajność, bezpieczeństwo, niezawodność, użyteczność, skalowalność. Np. „odpowiedź w mniej niż 1 sekundę".

**⚠️ Na egzaminie:** „loguje użytkownika" = funkcjonalne; „odpowiedź < 1 s" = niefunkcjonalne.
""")

add("Kanban i Scrum", r"""
**Najprościej:** dwie zwinne metody — jedna w równych odcinkach czasu, druga ciągłym strumieniem.

**Scrum —**
- **role:** Product Owner, Scrum Master, Zespół
- **sprinty** o stałej długości
- **artefakty:** backlog produktu/sprintu, inkrement
- **zdarzenia:** planning, daily, review, retrospektywa

**Kanban —** tablica z wizualizacją przepływu, **limity WIP** (ile zadań naraz), **ciągły przepływ** bez sprintów i wyznaczonych ról.

**⚠️ Na egzaminie:** Scrum = iteracje/role; Kanban = ciągły przepływ i limity WIP.
""")

add("Studium wykonalności", r"""
**Najprościej:** sprawdzenie ZANIM zaczniesz — czy da się i czy warto?

**Aspekty, które badasz:**
- **techniczna** — czy technologia to udźwignie
- **ekonomiczna** — koszt vs korzyść
- **organizacyjna** — czy zespół/firma to ogarnie
- **prawna** i **harmonogramowa** — czy zdążymy

**Efekt:** decyzja **go / no-go**.

**⚠️ Na egzaminie:** to analiza opłacalności i realności przed startem projektu.
""")

add("Diagramy UML", r"""
**Najprościej:** standardowy zestaw rysunków do opisu systemu — jedne pokazują z czego jest zbudowany, inne jak działa.

**Strukturalne (statyka — „z czego"):** klas, obiektów, komponentów, wdrożenia, pakietów.

**Behawioralne (dynamika — „jak działa"):** przypadków użycia, sekwencji, aktywności, stanów, komunikacji.

**⚠️ Na egzaminie:** diagram klas = struktura statyczna; sekwencji/aktywności = zachowanie/dynamika.
""")

add("Numeryczna reprezentacja liczb", r"""
**Najprościej:** komputer ma tylko ograniczoną liczbę szufladek na liczby, więc nie zmieści wszystkich.

**Konsekwencje:**
- zbiór liczb jest **skończony i nierównomierny** — gęściej blisko zera, rzadziej daleko
- pojawiają się **błędy zaokrągleń** i **epsilon maszynowy** (najmniejsza rozróżnialna różnica)
- wiele zwykłych ułamków dziesiętnych **nie ma** dokładnej reprezentacji

**⚠️ Na egzaminie:** liczby zmiennoprzecinkowe są dyskretne i nierównomierne; nie każda liczba dziesiętna jest reprezentowalna.
""")

add("IEEE 754 (arytmetyka float)", r"""
**Najprościej:** standard zapisu liczb „z przecinkiem": `znak × mantysa × 2^wykładnik`.

**Skutki skończonej precyzji:**
- **błędy zaokrągleń** przy prawie każdej operacji
- **brak łączności** dodawania — `(a+b)+c` ≠ `a+(b+c)` co do bitu
- **utrata cyfr znaczących (cancellation)** przy odejmowaniu bliskich liczb
- wartości specjalne: `±∞`, `NaN`, zero ze znakiem

**⚠️ Na egzaminie:** dodawanie float nie jest łączne; odejmowanie bliskich liczb traci precyzję.
""")

add("Divide and conquer w numeryce", r"""
**Najprościej:** podziel wielki rachunek na mniejsze, policz je i sklej wyniki.

**Schemat:** `PODZIEL → ROZWIĄŻ mniejsze → POŁĄCZ`.

**Sztandarowy przykład — FFT** (szybka transformata Fouriera): liczy w `O(n log n)` zamiast `O(n²)`.

**Inne:** szybkie mnożenie macierzy, rekurencyjne całkowanie adaptacyjne.

**⚠️ Na egzaminie:** FFT to klasyczny przykład dziel-i-zwyciężaj w numeryce.
""")

add("Wielomiany ortogonalne", r"""
**Najprościej:** specjalne rodziny wielomianów „ustawionych prostopadle", które świetnie przybliżają funkcje.

**Rodziny:** Legendre'a, **Czebyszewa**, Hermite'a, Laguerre'a — ortogonalne względem iloczynu skalarnego z wagą.

**Zastosowania:**
- **aproksymacja** (minimalizacja błędu)
- **kwadratury Gaussa** — węzły całkowania = **pierwiastki** wielomianu ortogonalnego
- stabilne obliczenia

**Czebyszew** minimalizuje błąd maksymalny → ogranicza brzydkie falowania na brzegach (**efekt Rungego**).

**⚠️ Na egzaminie:** węzły Gaussa = pierwiastki wielomianów ortogonalnych; Czebyszew tłumi Rungego.
""")

add("Kwadratury (Newton-Cotes, Gauss)", r"""
**Najprościej:** liczenie pola pod krzywą przez sumowanie pasków — dwa podejścia do wyboru punktów.

**Newton-Cotes —** węzły **równoodległe**. Proste (trapezów, Simpsona), ale przy wysokim stopniu **niestabilne**.

**Gauss —** węzły i wagi dobrane **optymalnie**. Kwadratura `n`-węzłowa jest dokładna dla wielomianów stopnia **≤ 2n−1** — czyli dużo dokładniejsza przy tej samej liczbie punktów.

**⚠️ Na egzaminie:** Gauss dokładniejszy przy tej samej liczbie węzłów; Simpson należy do Newton-Cotes.
""")

add("Układy równań liniowych (numerycznie)", r"""
**Najprościej:** dwa sposoby rozwiązywania `Ax = b` — „za skończoną liczbę kroków" albo „krążąc coraz bliżej".

**Metody bezpośrednie —** eliminacja Gaussa, rozkład **LU**, Cholesky (dla macierzy symetrycznych dodatnio określonych). Dają wynik w **skończonej** liczbie kroków.

**Metody iteracyjne —** Jacobi, Gauss-Seidel, gradienty sprzężone. Zbliżają się do rozwiązania — dobre dla **dużych rzadkich** układów.

**Uwaga:** źle **uwarunkowana** macierz → małe błędy wejścia dają duże błędy wyniku.

**⚠️ Na egzaminie:** bezpośrednie = skończona liczba kroków; iteracyjne dla dużych rzadkich; złe uwarunkowanie = duże błędy.
""")

add("Równania nieliniowe (bisekcja, Newton)", r"""
**Najprościej:** szukanie miejsca, gdzie funkcja przecina zero.

**Bisekcja —** gra „ciepło-zimno" na przedziale ze zmianą znaku. **Zawsze zbiega**, ale **wolno** (liniowo).

**Newton-Raphson —** skacze wzdłuż stycznej. **Szybki (kwadratowo)**, ale wymaga **pochodnej** i dobrego punktu startowego — czasem **rozbiega**.

**Sieczne —** jak Newton, ale bez pochodnej (przybliża ją); zbieżność nadliniowa.

**⚠️ Na egzaminie:** Newton kwadratowo zbieżny ale nie zawsze; bisekcja zawsze zbieżna w przedziale ze zmianą znaku.
""")

add("Generatory liczb losowych (PRNG)", r"""
**Najprościej:** maszynki udające losowość — tak naprawdę w pełni przewidywalne.

**PRNG (pseudolosowe) —** deterministyczne. **To samo ziarno (seed) → dokładnie ta sama sekwencja.** Mają skończony **okres**. Przykłady: LCG (liniowy kongruencyjny), Mersenne Twister.

**Prawdziwie losowe —** ze źródeł fizycznych (szum, rozpad).

**Transformacje rozkładów:** metoda odwrotnej dystrybuanty, Boxa-Mullera (rozkład normalny).

**⚠️ Na egzaminie:** PRNG jest deterministyczny i okresowy; to samo ziarno = ta sama sekwencja.
""")

add("Uczenie nadzorowane", r"""
**Najprościej:** uczysz model na przykładach z podpisami (etykietami).

**Jak działa:** pokazujesz pary `wejście → oczekiwane wyjście` (np. zdjęcie → „pies"). Model uczy się mapowania.

**Dwa zadania:**
- **klasyfikacja** — etykiety **dyskretne** (pies/kot/ptak)
- **regresja** — wartości **ciągłe** (cena, temperatura)

**Przykłady:** drzewa decyzyjne, SVM, sieci neuronowe, regresja liniowa/logistyczna.

**Ryzyko:** **przeuczenie (overfitting)** — model wkuwa dane treningowe zamiast uogólniać.

**⚠️ Na egzaminie:** nadzorowane = etykiety; klasyfikacja (dyskretne) vs regresja (ciągłe).
""")

add("Uczenie nienadzorowane", r"""
**Najprościej:** dajesz kupę danych **bez podpisów** i mówisz „poukładaj to sam".

**Główne zadania:**
- **klasteryzacja** — grupowanie podobnych (k-średnich, hierarchiczna)
- **redukcja wymiarowości** — upraszczanie danych (**PCA**)
- **reguły asocjacyjne** — „kto kupił X, kupił też Y"

**Uwaga:** grupowanie (klasteryzacja) **≠** klasyfikacja — tu nie ma z góry danych kategorii.

**⚠️ Na egzaminie:** brak etykiet; k-means i PCA to klasyka.
""")

add("Budowa sieci neuronowej", r"""
**Najprościej:** warstwy „neuronów", które przepuszczają i przetwarzają sygnał.

**Warstwy:** wejściowa → ukryte → wyjściowa.

**Pojedynczy neuron:**
1. liczy **sumę ważoną** wejść + `bias`
2. przepuszcza przez **funkcję aktywacji** (sigmoid, tanh, **ReLU**), która dodaje **nieliniowość**

**Kluczowa myśl:** bez nieliniowej aktywacji cała wielowarstwowa sieć = zwykły model **liniowy**. Uczenie = dostrajanie **wag**.

**⚠️ Na egzaminie:** bez nieliniowej aktywacji sieć = model liniowy; ReLU popularna w głębokich sieciach.
""")

add("Wsteczna propagacja (backpropagation)", r"""
**Najprościej:** uczenie sieci na własnych błędach, poprawiając wagi tam, gdzie najbardziej zawiniły.

**Krok po kroku:**
1. **Propagacja w przód** — policz wyjście i **błąd** (funkcję straty)
2. **Propagacja wstecz** — policz **gradient** straty względem wag **regułą łańcuchową** (od końca do początku)
3. **Aktualizacja wag** — spadek gradientu (przesuń wagi w stronę mniejszego błędu)

**Warunek:** funkcje aktywacji muszą być **różniczkowalne**.

**⚠️ Na egzaminie:** backprop liczy gradienty regułą łańcuchową; wymaga różniczkowalnych aktywacji.
""")

add("Sieci rekurencyjne (RNN, LSTM)", r"""
**Najprościej:** sieci z **pamięcią** — przetwarzają rzeczy po kolei, pamiętając, co było wcześniej.

**RNN —** mają sprzężenie zwrotne (**stan**), więc nadają się do **sekwencji**: tekst, mowa, szeregi czasowe.

**Problem:** przy długich sekwencjach gradient **zanika** lub **eksploduje** — sieć zapomina albo się rozjeżdża.

**Rozwiązanie — LSTM / GRU:** warianty z **bramkami**, które decydują, co pamiętać, a co zapomnieć.

**⚠️ Na egzaminie:** RNN dla danych sekwencyjnych; LSTM/GRU rozwiązują problem zanikającego gradientu.
""")

add("Algorytm A*", r"""
**Najprościej:** sprytne szukanie drogi = Dijkstra + intuicja (heurystyka), która podpowiada, gdzie jest cel.

**Wzór oceny węzła:** `f(n) = g(n) + h(n)`, gdzie:
- `g(n)` — koszt **dotychczasowy** (ile już przeszedłeś)
- `h(n)` — **szacowany** koszt do celu (heurystyka)

**Gwarancja optymalności:** gdy heurystyka jest **dopuszczalna** (nigdy nie **przeszacowuje**) i spójna.

**Skrajne przypadki:** `h = 0` → A* staje się zwykłym Dijkstrą.

**⚠️ Na egzaminie:** A* = Dijkstra + heurystyka; dopuszczalna heurystyka gwarantuje optymalność.
""")

add("Algorytmy szeregowania", r"""
**Najprościej:** zasady, który proces dostaje procesor i na jak długo.

**Główne algorytmy:**
- **FCFS** — kto pierwszy, ten pierwszy (ryzyko **efektu konwoju** — wielkie zadanie blokuje kolejkę)
- **SJF** — najkrótsze zadanie pierwsze; **minimalny średni czas oczekiwania**, ale **głodzi** długie
- **Round Robin** — każdy dostaje **kwant** czasu po kolei; sprawiedliwy, interaktywny
- **priorytetowy** i **wielopoziomowe kolejki**

**Podział:** wywłaszczające (można przerwać) vs niewywłaszczające.

**⚠️ Na egzaminie:** RR z małym kwantem = dużo przełączeń; SJF minimalizuje śr. czas oczekiwania, ale głodzi długie.
""")

add("Mechanizmy synchronizacji", r"""
**Najprościej:** narzędzia, żeby procesy/wątki nie wchodziły sobie w drogę przy wspólnym zasobie.

**Scentralizowane (wspólna pamięć):**
- **semafor** — licznik wolnych miejsc/pozwoleń
- **mutex** — jeden klucz do sekcji krytycznej (łazienki)
- **monitor** + zmienne warunkowe

**Rozproszone (brak wspólnej pamięci):** wzajemne wykluczanie przez **wiadomości** i znaczniki czasu — token ring, Ricart-Agrawala, Lamport.

**⚠️ Na egzaminie:** semafor/mutex/monitor to prymitywy; w rozproszeniu synchronizacja przez komunikaty.
""")

add("Problemy synchronizacyjne", r"""
**Najprościej:** klasyczne zagadki, które ilustrują pułapki współbieżności.

**Cztery klasyki:**
1. **Producent-konsument** — jeden wkłada, drugi wyjmuje z **bufora ograniczonego** (rozwiązanie: semafory)
2. **Czytelnicy-pisarze** — wielu czyta, ale pisarz musi mieć zasób na wyłączność
3. **Ucztujący filozofowie** — każdy chce dwóch widelców naraz → grozi **zakleszczeniem** i głodzeniem
4. **Śpiący fryzjer** — synchronizacja klient–usługodawca

**⚠️ Na egzaminie:** filozofowie = klasyczny przykład zakleszczenia; producent-konsument rozwiązywany semaforami.
""")

add("Proces a wątek", r"""
**Najprościej:** proces to osobny dom, wątek to domownik w tym samym domu.

**Proces —** własna **przestrzeń adresowa**, izolowany. Bezpieczny, ale **kosztowny** w tworzeniu i przełączaniu.

**Wątek —** jednostka wykonania **wewnątrz** procesu. **Współdzieli pamięć** i zasoby procesu. Lekki, szybkie przełączanie — ale wymaga **synchronizacji** (bo wątki wchodzą na wspólną pamięć).

**⚠️ Na egzaminie:** wątki jednego procesu dzielą pamięć; procesy są izolowane.
""")

add("Pamięć wirtualna (stronicowanie/segmentacja)", r"""
**Najprościej:** dwa sposoby cięcia pamięci — na równe kartki albo na logiczne kawałki.

**Stronicowanie —** dzieli pamięć na **strony/ramki stałej wielkości**, mapowane **tablicą stron**. Brak fragmentacji **zewnętrznej**, jest **wewnętrzna** (marnowanie na końcu strony).

**Segmentacja —** dzieli logicznie na **segmenty zmiennej długości** (kod, dane, stos). Jest fragmentacja **zewnętrzna**.

**Page fault —** gdy potrzebnej strony nie ma w pamięci, ładuje się ją z dysku.

**⚠️ Na egzaminie:** stronicowanie = stały rozmiar + fragmentacja wewnętrzna; segmentacja = zmienny + zewnętrzna.
""")

add("Systemy czasu rzeczywistego", r"""
**Najprościej:** liczy się **zdążyć na czas** (deadline), a nie być najszybszym.

**Dwa rodzaje:**
- **twardy (hard RT)** — przekroczenie terminu = **katastrofa** (poduszka powietrzna, sterownik hamulców)
- **miękki (soft RT)** — spóźnienie tylko **pogarsza jakość** (zacinający się film)

**Wymagają:** determinizmu i przewidywalnego szeregowania.

**⚠️ Na egzaminie:** RT = przewidywalność i terminy, niekoniecznie „najszybszy".
""")

add("Tworzenie procesów (fork/exec)", r"""
**Najprościej:** trzy uniksowe czasowniki: skopiuj się, zamień program, poczekaj.

**Trzy wywołania:**
- **fork()** — tworzy **kopię** procesu (dziecko). Dziedziczy przestrzeń (**copy-on-write**). Zwraca `0` dziecku, `PID` rodzicowi
- **exec()** — **podmienia** obraz procesu na nowy program (kod się zmienia, proces zostaje)
- **wait()** — rodzic **czeka** na zakończenie dziecka

**Stany potomka:** **zombie** (skończył, ale rodzic nie odebrał statusu), **osierocony** (rodzic zniknął).

**⚠️ Na egzaminie:** fork kopiuje, exec zastępuje kod; zombie/osierocony to stany procesu potomnego.
""")

add("Zakleszczenie (deadlock)", r"""
**Najprościej:** każdy czeka na każdego i nikt się nie rusza — jak auta blokujące się na skrzyżowaniu.

**Cztery warunki Coffmana (muszą zajść WSZYSTKIE):**
1. **wzajemne wykluczanie** — zasób niepodzielny
2. **trzymaj i czekaj** — trzymasz jedno, czekasz na drugie
3. **brak wywłaszczania** — nie można siłą odebrać zasobu
4. **cykliczne oczekiwanie** — koło czekających

**Strategie:** zapobieganie (zerwij 1 warunek), **unikanie** (algorytm bankiera), wykrywanie i usuwanie, ignorowanie.

**⚠️ Na egzaminie:** zerwanie choć jednego z 4 warunków usuwa deadlock; bankier = unikanie.
""")

add("Łączenie statyczne i dynamiczne", r"""
**Najprościej:** wkładasz bibliotekę na stałe do programu albo pożyczasz wspólną przy starcie.

**Statyczne —** biblioteka **wkompilowana** w plik wykonywalny. Plik **większy**, ale **samodzielny**. Aktualizacja biblioteki = rekompilacja.

**Dynamiczne —** biblioteka (`.so`/`.dll`) ładowana przy uruchomieniu/działaniu, **współdzielona** między programami. Plik **mniejszy**, łatwa aktualizacja — ale zależność od wersji (słynne „DLL hell").

**⚠️ Na egzaminie:** dynamiczne = współdzielenie i mniejszy plik; statyczne = samodzielność.
""")

add("Adresacja IP", r"""
**Najprościej:** adres IP to jak adres pocztowy — hierarchiczny, więc router (listonosz) wie, dokąd kierować.

**Cechy:** adres **logiczny** warstwy sieciowej (L3), **hierarchiczny** (część sieci + część hosta), **routowalny**.

**IPv4 —** 32 bity (4 oktety), maska/prefiks (**CIDR**), adresy prywatne/publiczne, **NAT**.
**IPv6 —** 128 bitów (bo adresów IPv4 zabrakło).

**⚠️ Na egzaminie:** IP logiczny i hierarchiczny (routing po prefiksie); MAC płaski i fizyczny.
""")

add("Adresacja MAC", r"""
**Najprościej:** MAC to numer seryjny karty sieciowej, przyklejony na stałe w fabryce.

**Cechy:** adres **fizyczny** warstwy łącza (L2), **płaski** (bez hierarchii), przypisany karcie sieciowej, **lokalny** dla segmentu — **nie routowalny**.

**Zasięg:** działa w obrębie sieci lokalnej / domeny rozgłoszeniowej. Router go nie przenosi dalej.

**⚠️ Na egzaminie:** MAC nie jest routowalny; działa w obrębie sieci lokalnej.
""")

add("Struktura adresu MAC", r"""
**Najprościej:** 48 bitów (6 bajtów, zapis szesnastkowy) podzielonych na „producenta" i „numer sztuki".

**Budowa:**
- pierwsze **3 bajty = OUI** — identyfikator producenta (nadaje IEEE)
- ostatnie **3 bajty** — numer nadany przez producenta

**Specjalne bity** w pierwszym bajcie: I/G (indywidualny/grupowy), U/L (uniwersalny/lokalny).
**Broadcast:** same jedynki — `FF:FF:FF:FF:FF:FF`.

**⚠️ Na egzaminie:** MAC = 48 bitów; OUI (pierwsze 3 bajty) identyfikuje producenta.
""")

add("DHCP i SLAAC", r"""
**Najprościej:** dwa sposoby, żeby urządzenie samo dostało adres, gdy je podłączysz.

**DHCP —** serwer (recepcjonista) przydziela **IP, maskę, bramę, DNS** na wynajem (**dzierżawa**). To **stanowe** przydzielanie.

**SLAAC (IPv6) —** urządzenie samo **układa sobie adres** z prefiksu ogłaszanego przez router. To **bezstanowe** (router nie prowadzi listy przydziałów).

Dodatkowo: APIPA / link-local (adres awaryjny bez serwera).

**⚠️ Na egzaminie:** DHCP = stanowe przydzielanie; SLAAC = bezstanowe w IPv6.
""")

add("TCP i UDP", r"""
**Najprościej:** list polecony z potwierdzeniem kontra zwykła pocztówka.

**TCP —** **połączeniowy**, **niezawodny**: potwierdzenia, retransmisje, numeracja, kontrola przepływu i przeciążenia. Strumień danych. **Wolniejszy**, ale pewny.

**UDP —** **bezpołączeniowy**, **zawodny**: bez potwierdzeń, mały narzut, **szybki**. Dobry do VoIP, streamingu, gier, DNS.

**⚠️ Na egzaminie:** TCP niezawodny i połączeniowy; UDP szybki, bez gwarancji dostarczenia.
""")

add("Routing IP (longest prefix match)", r"""
**Najprościej:** router patrzy w swoją tablicę tras i wybiera **najbardziej pasujący, najdokładniejszy** wpis.

**Jak decyduje:**
1. porównuje adres docelowy z wpisami w **tablicy routingu**
2. wybiera regułą **najdłuższego pasującego prefiksu** (im dłuższy pasujący prefiks, tym dokładniejsza trasa)
3. przekazuje do **next-hop**; jeśli nic nie pasuje → **brama domyślna**

**⚠️ Na egzaminie:** wybór trasy = najdłuższy pasujący prefiks; brak trasy → brama domyślna.
""")

add("VLAN", r"""
**Najprościej:** dzielenie jednej fizycznej sieci na osobne, niewidzące się grupy — jak przegródki w pudełku.

**Co to daje:** logiczny podział L2 na odrębne **domeny rozgłoszeniowe** niezależnie od okablowania (znakowanie ramek **802.1Q**).

**Zalety:** segmentacja, bezpieczeństwo, mniej broadcastu, elastyczność.

**Ważne:** ruch **między** VLAN-ami wymaga **routera / urządzenia L3**.

**⚠️ Na egzaminie:** VLAN dzieli domeny rozgłoszeniowe; komunikacja między VLAN wymaga routingu.
""")

add("Protokoły routingu (IGP/EGP)", r"""
**Najprościej:** jedne protokoły działają wewnątrz jednej sieci-firmy, inne spinają różne sieci-państwa.

**Wg zasięgu:**
- **IGP** — wewnątrz systemu autonomicznego (RIP, OSPF, EIGRP)
- **EGP** — między systemami autonomicznymi (**BGP** — spina cały internet)

**Wg algorytmu:**
- **wektor odległości** (RIP) — wymiana tablic z sąsiadami („ile masz do X?")
- **stan łącza** (OSPF) — pełna mapa topologii, trasy liczone **Dijkstrą**

**⚠️ Na egzaminie:** OSPF = link-state; RIP = distance-vector; BGP = między systemami autonomicznymi.
""")

add("ARP (IP → MAC)", r"""
**Najprościej:** znasz czyjś adres IP, ale nie MAC — ARP to krzyk po sieci lokalnej „kto ma ten IP?".

**Jak działa:**
1. rozgłoszenie (**broadcast**): „kto ma IP `x.x.x.x`?"
2. właściciel odpowiada swoim **MAC**
3. odpowiedź trafia do **tablicy ARP** (buforowanie na później)

**Zasięg:** tylko sieć **lokalna**. W IPv6 zastępuje to **NDP**.

**⚠️ Na egzaminie:** ARP mapuje IP→MAC przez broadcast; działa w sieci lokalnej.
""")

add("STP (drzewo rozpinające)", r"""
**Najprościej:** gdy w sieci są zapasowe kable, dane mogłyby krążyć w kółko bez końca — STP temu zapobiega.

**Problem:** redundantne łącza L2 tworzą **pętle** (ramki krążą w nieskończoność, broadcast storm).

**Co robi STP (802.1d):**
1. wybiera **root bridge** (most o najniższym Bridge ID)
2. liczy najkrótsze ścieżki do roota
3. **blokuje** nadmiarowe łącza → zostaje drzewo bez pętli

**Awaria łącza →** rekonfiguracja (odblokowuje zapas).

**⚠️ Na egzaminie:** STP eliminuje pętle L2, blokując porty; most główny wybierany wg Bridge ID.
""")

add("Teoria CAP", r"""
**Najprościej:** gdy dane są w wielu kopiach na wielu serwerach, nie da się mieć naraz wszystkich trzech dobrych rzeczy.

**Trzy litery:**
- **C (Consistency)** — każdy odczyt widzi najnowszy zapis
- **A (Availability)** — każde żądanie dostaje odpowiedź
- **P (Partition tolerance)** — system działa mimo zerwanej sieci między węzłami

**Twierdzenie:** przy **podziale sieci (P)** musisz wybrać: **C albo A**. W praktyce P jest nieunikniona, więc realny wybór to CP lub AP.

**⚠️ Na egzaminie:** w razie partycji poświęcasz C lub A; P jest praktycznie nieunikniona.
""")

add("Middleware (warstwa pośrednicząca)", r"""
**Najprościej:** tłumacz-pośrednik między aplikacją a siecią/systemem, który ukrywa cały bałagan rozproszenia.

**Co załatwia:**
- ukrywa **heterogeniczność** (różne maszyny, systemy) i szczegóły komunikacji
- zapewnia **przezroczystość**
- zdalne wywołania (**RPC/RMI**), nazewnictwo, synchronizację, bezpieczeństwo, transakcje

**⚠️ Na egzaminie:** middleware = warstwa ukrywająca rozproszenie i ułatwiająca komunikację.
""")

add("Systemy reaktywne (Reactive Manifesto)", r"""
**Najprościej:** cztery cechy dobrze zaprojektowanego, odpornego systemu — a fundamentem są wiadomości.

**Cztery cechy:**
1. **Responsive** — szybko odpowiada
2. **Resilient** — odporny na awarie (izolacja, replikacja)
3. **Elastic** — skaluje się z obciążeniem (rośnie i maleje)
4. **Message-driven** — oparty na **asynchronicznych komunikatach** (luźne powiązanie)

**Zależność:** z przesyłania komunikatów wynika elastyczność i odporność, a ich efektem jest responsywność.

**⚠️ Na egzaminie:** fundament = message-driven; efektem końcowym jest responsywność.
""")

add("Zegar Lamporta", r"""
**Najprościej:** licznik porządkujący zdarzenia, gdy komputery nie mają wspólnego zegara.

**Reguły (krok po kroku):**
1. przy każdym zdarzeniu **zwiększ** swój licznik
2. przy **wysłaniu** wiadomości dołącz do niej swój licznik
3. przy **odbiorze**: `zegar = max(lokalny, otrzymany) + 1`

**Gwarancja:** jeśli `a → b` (a jest przyczyną b), to `L(a) < L(b)`. **Uwaga:** odwrotność nie zachodzi — mniejszy numer nie dowodzi przyczynowości.

**Ograniczenie:** nie wykrywa **współbieżności** (od tego są zegary wektorowe).

**⚠️ Na egzaminie:** daje porządek częściowy zgodny z przyczynowością; nie wykrywa zdarzeń współbieżnych.
""")

add("Wzorzec REST", r"""
**Najprościej:** styl usług sieciowych po HTTP, gdzie serwer nie pamięta twoich poprzednich żądań.

**Kluczowe cechy:**
- **bezstanowość** — każde żądanie jest kompletne (serwer nie trzyma stanu sesji)
- **zasoby** identyfikowane przez **URI**
- operacje **metodami HTTP**: `GET`, `POST`, `PUT`, `DELETE`
- reprezentacje w JSON/XML, jednolity interfejs, klient-serwer, cache

**⚠️ Na egzaminie:** REST jest bezstanowy i zasobowy; stan sesji nie jest trzymany po stronie serwera.
""")

add("Przezroczystość", r"""
**Najprościej:** ukrywanie przed użytkownikiem, że system jest rozproszony — ma po prostu „działać".

**Typy przezroczystości:**
- **dostępu** — jednolity dostęp lokalny i zdalny
- **położenia** — nie wiesz, gdzie fizycznie jest zasób
- **migracji** — zasób może się przenieść niezauważenie
- **replikacji**, **współbieżności**, **awarii**, **skalowania**

**⚠️ Na egzaminie:** przezroczystość położenia = użytkownik nie zna fizycznej lokalizacji zasobu.
""")

add("Gniazda (sockets)", r"""
**Najprościej:** końcówka do rozmowy przez sieć = **adres IP + port** (numer domu + numer mieszkania).

**Dwa typy:**
- **strumieniowe (TCP)** — niezawodne, połączeniowe
- **datagramowe (UDP)** — szybkie, bezpołączeniowe

**Zalety:** uniwersalność, kontrola.
**Wady:** niski poziom — sam ogarniasz błędy i serializację.

**⚠️ Na egzaminie:** gniazdo = IP + port; TCP-socket niezawodny, UDP-socket szybki.
""")

add("Klasyfikacja Chomsky'ego", r"""
**Najprościej:** drabinka języków wg trudności — im niższy typ, tym potężniejsza maszyna potrzebna.

**Cztery typy (od najprostszych):**
- **Typ 3 — regularne:** automat **skończony**
- **Typ 2 — bezkontekstowe:** automat ze **stosem**
- **Typ 1 — kontekstowe:** automat liniowo ograniczony
- **Typ 0 — rekurencyjnie przeliczalne:** **maszyna Turinga**

**Zawieranie:** regularne ⊂ bezkontekstowe ⊂ kontekstowe ⊂ rekurencyjnie przeliczalne.

**⚠️ Na egzaminie:** typ 3 = automat skończony, typ 2 = stosowy; każdy wyższy typ zawiera niższe.
""")

add("Postać normalna Chomsky'ego (CNF)", r"""
**Najprościej:** uporządkowanie reguł gramatyki bezkontekstowej do dwóch prostych wzorów.

**Dozwolone produkcje:**
- `A → BC` — dokładnie **dwa nieterminale**
- `A → a` — dokładnie **jeden terminal**

**Po co:** umożliwia algorytm **CYK** rozpoznawania słów w czasie `O(n³)`.

**⚠️ Na egzaminie:** CNF = produkcje do dwóch nieterminali albo jednego terminala; podstawa CYK.
""")

add("Postać normalna Greibach (GNF)", r"""
**Najprościej:** reguły, w których prawa strona **zawsze zaczyna się od terminala**.

**Postać:** `A → aα`, gdzie `a` to terminal, a `α` to (możliwie pusty) ciąg nieterminali.

**Zaleta:** terminal na początku → **brak rekurencji lewostronnej** → wygodna analiza **zstępująca** (top-down).

**⚠️ Na egzaminie:** GNF zaczyna prawą stronę terminalem; eliminuje rekurencję lewostronną.
""")

add("Wieloznaczność gramatyki", r"""
**Najprościej:** gramatyka jest wieloznaczna, gdy jedno zdanie da się rozłożyć na **więcej niż jedno** drzewo.

**Definicja:** istnieje słowo z ≥2 drzewami wyprowadzenia (lub ≥2 skrajnie lewymi wyprowadzeniami).

**Problem praktyczny:** utrudnia parsowanie — klasyczny przykład **„dangling else"** (do którego `if` należy `else`?).

**Trudność:** niektóre języki są **istotnie wieloznaczne** (nie mają żadnej jednoznacznej gramatyki); ogólne sprawdzenie wieloznaczności jest **nierozstrzygalne**.

**⚠️ Na egzaminie:** wieloznaczność = ≥2 drzewa wywodu dla jednego słowa.
""")

add("Problem stopu", r"""
**Najprościej:** czy da się zbudować program, który dla KAŻDEGO innego programu powie z góry „zatrzyma się czy będzie kręcił się wiecznie"? Nie da się.

**Wynik:** problem stopu jest **nierozstrzygalny** — nie istnieje ogólny algorytm rozstrzygający zatrzymanie.

**Dowód (idea):** Turing, przez **przekątniową sprzeczność** — zakładasz, że taki program istnieje, i budujesz przypadek, który mu przeczy.

**Znaczenie:** fundamentalna **granica obliczalności**.

**⚠️ Na egzaminie:** brak ogólnego algorytmu na zatrzymanie; klasyczny problem nierozstrzygalny.
""")

add("P vs NP", r"""
**Najprościej:** czy „łatwe do sprawdzenia" znaczy „łatwe do rozwiązania"? Nikt tego nie wie.

**Klasy:**
- **P —** problemy **rozwiązywalne** w czasie wielomianowym
- **NP —** problemy, których rozwiązanie da się **zweryfikować** w czasie wielomianowym (jak sprawdzenie gotowego sudoku)

**Pytanie tysiąclecia:** czy `P = NP`? (nierozstrzygnięte)

**NP-zupełne —** najtrudniejsze w NP; jeśli KTÓRYKOLWIEK jest w P, to `P = NP`. Pierwszy taki: **SAT** (twierdzenie Cooka-Levina).

**⚠️ Na egzaminie:** NP = łatwa weryfikacja, niekoniecznie łatwe znajdowanie; SAT pierwszy NP-zupełny.
""")

add("Rozstrzygalność", r"""
**Najprościej:** czy istnieje algorytm, który zawsze da odpowiedź TAK/NIE i się zatrzyma.

**Rozstrzygalny —** istnieje algorytm **zawsze kończący się** poprawną odpowiedzią TAK/NIE.

**Częściowo rozstrzygalny (rekurencyjnie przeliczalny) —** algorytm zatrzymuje się i mówi „TAK", gdy odpowiedź to TAK, ale przy „NIE" może **kręcić się w nieskończoność**.

**Przykład:** problem stopu jest r.p. (półrozstrzygalny), ale **nierozstrzygalny**.

**⚠️ Na egzaminie:** rozstrzygalny = zawsze się zatrzymuje z odpowiedzią.
""")

add("Złożoność problemu vs algorytmu", r"""
**Najprościej:** koszt jednej konkretnej metody kontra najlepszy możliwy koszt dla całego problemu.

**Złożoność algorytmu —** zasoby (czas, pamięć) zużywane przez **konkretną metodę**.

**Złożoność problemu —** **najlepsza możliwa** złożoność jakiegokolwiek algorytmu rozwiązującego ten problem (dolna granica, poniżej której się nie da).

Bada się: dolne granice, przypadek najgorszy/średni.

**⚠️ Na egzaminie:** złożoność problemu = najlepsza możliwa; złożoność algorytmu = konkretnej metody.
""")

add("Klasy złożoności", r"""
**Najprościej:** szufladki grupujące problemy wg zużycia czasu i pamięci.

**Najważniejsze:**
- **P** — czas wielomianowy
- **NP** — weryfikacja wielomianowa
- **PSPACE** — pamięć wielomianowa
- **EXPTIME** — czas wykładniczy
- **L / NL** — pamięć logarytmiczna

**Zawierania:** `P ⊆ NP ⊆ PSPACE ⊆ EXPTIME`. Wiadomo, że `P ⊊ EXPTIME`.

**⚠️ Na egzaminie:** znaj inkluzje; NP ⊆ PSPACE.
""")

add("Maszyna Turinga", r"""
**Najprościej:** najprostszy wyobrażalny komputer, definiujący, co w ogóle da się policzyć.

**Budowa:**
- nieskończona **taśma** (pamięć)
- **głowica** — czyta, pisze, przesuwa się
- zbiór **stanów** i **funkcja przejścia**

**Znaczenie:** podstawa **tezy Churcha-Turinga** (definicja obliczalności).

**Warianty (równoważne co do mocy):** deterministyczna, niedeterministyczna, wielotaśmowa.

**⚠️ Na egzaminie:** MT = model obliczalności; niedeterministyczna nie jest silniejsza, tylko potencjalnie szybsza.
""")

add("Dowodzenie przynależności do klasy (redukcja)", r"""
**Najprościej:** żeby pokazać, że problem jest trudny, „przerabiasz" na niego znany trudny problem.

**Dwie części dowodu:**
1. **Przynależność (membership)** — wskaż algorytm o danym zasobie (np. „to jest w NP, bo weryfikuję w czasie wielomianowym")
2. **Trudność (hardness)** — **redukcja wielomianowa** znanego trudnego problemu **do** badanego

**Zupełność = przynależność + trudność.** Np. NP-zupełność: pokaż, że problem jest w NP, i zredukuj do niego SAT (lub inny NP-zupełny).

**⚠️ Na egzaminie:** NP-zupełność = w NP + redukcja z problemu już NP-zupełnego.
""")

add("PSPACE a gry (QBF)", r"""
**Najprościej:** ustalenie zwycięzcy w wielu grach dwuosobowych z pełną informacją to problem klasy PSPACE.

**Dlaczego:** uogólnione szachy, go, geografia — ich rozstrzyganie jest **PSPACE-zupełne**.

**Związek z logiką (QBF):** odpowiada **kwantyfikowanym formułom logicznym** z naprzemiennymi kwantyfikatorami: „**istnieje** mój ruch, taki że **dla każdego** ruchu przeciwnika **istnieje** mój...". QBF jest **PSPACE-zupełny**.

**⚠️ Na egzaminie:** naprzemienne kwantyfikatory `∃∀∃…` = istota PSPACE; QBF jest PSPACE-zupełny.
""")

add("Algebra CSP", r"""
**Najprościej:** opis procesów współbieżnych, które rozmawiają przez kanały „twarzą w twarz".

**Kluczowa idea:** komunikacja przez **synchroniczne kanały** (**rendez-vous**) — nadawca i odbiorca **czekają na siebie** i wymieniają dane w jednym momencie. **Brak dzielonej pamięci.**

**Operatory:** prefiks, wybór, komunikacja, kompozycja równoległa.

**Dziedzictwo:** kanały w językach Go i occam.

**⚠️ Na egzaminie:** CSP = komunikacja przez synchroniczne kanały (spotkanie), bez wspólnej pamięci.
""")

add("Sieci Petriego", r"""
**Najprościej:** rysunek z kółkami (miejsca z żetonami) i prostokątami (tranzycje = zdarzenia), modelujący współbieżność.

**Jak działa:**
- **miejsca** przechowują **żetony** (rozmieszczenie żetonów = **znakowanie / marking**)
- **tranzycja** jest **aktywna (odpala)**, gdy miejsca wejściowe mają dość żetonów
- odpalenie **przesuwa** żetony (zabiera z wejść, dokłada do wyjść)

**Opis macierzowy:** macierze wejść, wyjść i **incydencji** `C = wyjścia − wejścia`; równanie stanu.

**Do czego:** modeluje współbieżność, synchronizację, konflikty, zakleszczenia.

**⚠️ Na egzaminie:** macierz incydencji = wyjścia − wejścia; marking = rozmieszczenie żetonów.
""")

add("Relacja happened-before", r"""
**Najprościej:** porządek „co na pewno było przed czym" w systemie rozproszonym.

**Reguły relacji `→`:**
1. zdarzenia w **jednym procesie** są uporządkowane (po kolei)
2. **wysłanie** komunikatu `→` jego **odebranie**
3. **przechodniość** (jeśli `a→b` i `b→c`, to `a→c`)

**Współbieżność:** zdarzenia **nieporównywalne** tą relacją są **współbieżne** (dzieją się „obok siebie").

**To porządek CZĘŚCIOWY** — nie każde dwa zdarzenia da się porównać. Podstawa zegarów logicznych.

**⚠️ Na egzaminie:** happened-before = porządek częściowy; brak relacji = współbieżność.
""")

add("Współbieżność a równoległość", r"""
**Najprościej:** żonglowanie wieloma zadaniami kontra faktyczne robienie wielu rzeczy naraz.

**Współbieżność (concurrency) —** **zarządzanie** wieloma zadaniami w tym samym okresie. Mogą przeplatać się na **jednym rdzeniu** (kwestia **struktury** programu). Jeden kucharz gotujący kilka dań, przełączając się.

**Równoległość (parallelism) —** **faktyczne** jednoczesne wykonanie na **wielu** jednostkach (kwestia **wykonania**). Kilku kucharzy naraz.

**⚠️ Na egzaminie:** współbieżność ≠ równoległość; współbieżny możesz być na 1 rdzeniu, równoległość wymaga wielu.
""")
