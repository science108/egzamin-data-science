# Skrypt do egzaminu kwalifikacyjnego — Informatyka / Data Science (AGH)

Egzamin: test jednokrotnego wyboru, 40–50 pytań. Materiał obejmuje 18 działów. Każde zagadnienie: krótka definicja + jak działa + na co uważać na teście.

---

## 1. Wprowadzenie do systemu UNIX

**System PAM (Pluggable Authentication Modules).** Modularny mechanizm uwierzytelniania w UNIX/Linux, oddzielający aplikacje od metody uwierzytelniania. Aplikacja (np. `login`, `sshd`) wywołuje bibliotekę PAM, a ta ładuje moduły wg konfiguracji (`/etc/pam.d/`). Cztery grupy modułów (typy): **auth** (weryfikacja tożsamości, np. hasło), **account** (czy konto ważne, godziny dostępu), **password** (zmiana haseł), **session** (czynności przy otwarciu/zamknięciu sesji, np. montowanie katalogu). Flagi kontrolne: `required`, `requisite`, `sufficient`, `optional`. *Na teście:* PAM = elastyczność bez rekompilacji aplikacji; znaj 4 typy i flagi.

**Budowa systemu plików w UNIX.** Struktura drzewiasta z jednym korzeniem `/`. Kluczowe pojęcia: **i-węzeł (inode)** — przechowuje metadane pliku (właściciel, prawa, rozmiar, wskaźniki na bloki), ale NIE nazwę. Nazwa jest w katalogu (katalog = tablica par nazwa→numer inode). **Dowiązanie twarde (hard link)** = kolejna nazwa wskazująca ten sam inode; **dowiązanie symboliczne (soft link)** = plik zawierający ścieżkę. Typy plików: zwykły, katalog, dowiązanie, urządzenie znakowe/blokowe, potok (FIFO), gniazdo. *Na teście:* inode nie zawiera nazwy; hard link nie działa między systemami plików, symlink tak.

**Listy kontroli dostępu (ACL).** Rozszerzenie klasycznych praw `rwx` (właściciel/grupa/inni). ACL pozwala nadać uprawnienia konkretnym użytkownikom i grupom niezależnie od standardowej trójki. Polecenia: `getfacl`, `setfacl`. Występuje **maska** ograniczająca maksymalne prawa dla wpisów rozszerzonych. *Zastosowanie:* precyzyjne współdzielenie plików. *Na teście:* ACL = drobnoziarnista kontrola przekraczająca model owner/group/other.

**System kontyngentów (quota).** Limit zasobów dyskowych na użytkownika lub grupę. Dwa rodzaje limitów: liczba **bloków** (przestrzeń) i liczba **i-węzłów** (liczba plików). Dwa progi: **miękki (soft)** — można przekroczyć na czas okresu karencji (grace period); **twardy (hard)** — nieprzekraczalny. *Na teście:* soft można chwilowo przekroczyć, hard nigdy; quota liczy bloki i inody.

**Kontekst pracy uniksowego systemu operacyjnego.** Rozróżnienie **trybu użytkownika (user mode)** i **trybu jądra (kernel mode)**. Program użytkownika prosi jądro o usługi przez **wywołania systemowe (syscall)**, co powoduje przełączenie kontekstu. Kontekst procesu = stan rejestrów, licznik rozkazów, stos, mapa pamięci. Przełączanie kontekstu (context switch) zapisuje/odtwarza ten stan przy zmianie procesu. *Na teście:* syscall = przejście user→kernel; przełączenie kontekstu ma koszt.

**Priorytet procesu.** Określa kolejność dostępu do CPU. W UNIX wartość **nice** (od -20 najwyższy priorytet, do +19 najniższy); zwykły użytkownik może tylko obniżać priorytet (zwiększać nice). Jądro liczy priorytet dynamiczny. Polecenia: `nice`, `renice`. *Na teście:* niższa wartość nice = wyższy priorytet; użytkownik nie podniesie priorytetu swojego procesu bez uprawnień.

**Mechanizmy komunikacji między procesami (IPC).** Potoki (pipe) — jednokierunkowe, między spokrewnionymi procesami; potoki nazwane (FIFO) — między dowolnymi; kolejki komunikatów; pamięć dzielona (shared memory, najszybsza — brak kopiowania); semafory (synchronizacja); gniazda (sockets, także sieciowo); sygnały (asynchroniczne powiadomienia). *Na teście:* pamięć dzielona = najszybsza ale wymaga własnej synchronizacji; sygnał przenosi bardzo mało informacji.

**Protokół LDAP.** Lightweight Directory Access Protocol — dostęp do usług katalogowych (hierarchiczna baza informacji o użytkownikach, grupach, zasobach). Dane w strukturze drzewa (DIT), wpisy identyfikowane przez **DN (Distinguished Name)**, opisane atrybutami wg schematu. Zoptymalizowany pod **odczyt** (dużo czytań, mało zapisów). Zastosowanie: scentralizowane uwierzytelnianie i książki adresowe. *Na teście:* LDAP = katalog, hierarchia, DN, szybki odczyt.

**Protokół Kerberos.** System uwierzytelniania w sieci oparty na **kluczach symetrycznych** i zaufanej trzeciej stronie (**KDC** = AS + TGS). Użytkownik dostaje **bilet (ticket)** — TGT, a potem bilety do usług; hasło nie wędruje przez sieć. Wykorzystuje znaczniki czasu (wrażliwość na synchronizację zegarów). Zastosowanie: **Single Sign-On**, uwierzytelnianie w Active Directory. *Na teście:* Kerberos = bilety, KDC, klucze symetryczne, wymaga zsynchronizowanych zegarów.

---

## 2. Wstęp do informatyki

**EBNF (Rozszerzona notacja Backusa-Naura).** Formalny zapis gramatyki (składni) języka. Rozszerza BNF o wygodne operatory: `[...]` opcjonalność, `{...}` powtórzenie (0 lub więcej), `(...)` grupowanie, `|` alternatywa. Reguły produkcji definiują symbole nieterminalne przez terminalne. *Na teście:* rozpoznaj znaczenie nawiasów; `{}` = powtórzenie, `[]` = opcjonalne.

**Aspekty języka programowania.** Trzy główne wymiary: **składnia (syntax)** — forma zapisu; **semantyka** — znaczenie konstrukcji; **pragmatyka** — sposób i cel użycia. Czasem dodaje się leksykę. *Na teście:* składnia ≠ semantyka; poprawny składniowo program może być bezsensowny semantycznie.

**Mechanizmy zabezpieczające przed błędami.** Kontrola typów (typowanie silne/statyczne), kontrola zakresów tablic, obsługa wyjątków, inicjalizacja zmiennych, hermetyzacja, `const`/niemodyfikowalność, sprawdzanie zgodności argumentów. *Na teście:* silne typowanie wychwytuje błędy wcześniej; brak kontroli granic tablic = źródło błędów (C).

**Cele procedur i funkcji.** Modularność, ponowne użycie kodu (unikanie powtórzeń — DRY), abstrakcja/ukrycie szczegółów, czytelność, łatwiejsze testowanie i utrzymanie. Funkcja zwraca wartość, procedura wykonuje działanie. *Na teście:* główny cel = dekompozycja i reużywalność, nie „przyspieszenie".

**Typy numeryczne.** Całkowite (int, ze znakiem/bez znaku, różne rozmiary) i zmiennoprzecinkowe (float/double wg IEEE 754). Różnią się zakresem i precyzją. Liczby całkowite są dokładne w swoim zakresie; zmiennoprzecinkowe mają skończoną precyzję (błędy zaokrągleń). *Na teście:* float ≠ dokładna reprezentacja ułamków dziesiętnych (np. 0.1).

**Typy strukturalne.** Typy złożone z innych typów: rekord/struktura (pola różnych typów), tablica (elementy tego samego typu), unia, zbiór, lista. Pozwalają grupować powiązane dane. *Na teście:* struktura = heterogeniczna, tablica = homogeniczna.

**Kodowanie znaków UTF-8.** Kodowanie Unicode o **zmiennej długości** (1–4 bajty). ASCII (0–127) = 1 bajt (kompatybilność wsteczna). Bajty wielobajtowe mają charakterystyczne prefiksy bitowe: bajt wiodący `110xxxxx`/`1110xxxx`/`11110xxx`, bajty kontynuacji `10xxxxxx`. *Na teście:* UTF-8 jest zmiennobajtowe, zgodne z ASCII na 1 bajcie; bajt kontynuacji zaczyna się od `10`.

**Sposoby przekazywania parametrów.** **Przez wartość (by value)** — kopia argumentu, zmiany lokalne. **Przez referencję/wskaźnik (by reference)** — dostęp do oryginału, zmiany widoczne na zewnątrz. Inne: przez wynik, przez wartość-wynik, przez nazwę (leniwe). *Na teście:* by value nie zmienia oryginału; w C tablice przekazywane efektywnie „przez wskaźnik".

**Funkcja lambda w Pythonie.** Anonimowa funkcja jednowyrażeniowa: `lambda x: x+1`. Używana tam, gdzie potrzeba krótkiej funkcji (argument `map`, `filter`, `sorted(key=...)`). Ograniczenie: tylko jedno wyrażenie, brak instrukcji. *Na teście:* lambda zwraca wartość wyrażenia bez `return`; nie zawiera pętli/przypisań.

**Rekurencja.** Funkcja wywołująca samą siebie. Wymaga **warunku bazowego** (stop) i kroku zbliżającego do bazy. Rodzaje: bezpośrednia/pośrednia, ogonowa (tail). Koszt: pamięć stosu (ryzyko przepełnienia). *Na teście:* brak warunku bazowego = nieskończona rekurencja / stack overflow.

**Sposoby przydziału pamięci dla zmiennych.** **Statyczny** — przydzielony na czas życia programu (zmienne globalne/static). **Automatyczny (stos)** — zmienne lokalne, tworzone/niszczone z blokiem. **Dynamiczny (sterta/heap)** — `malloc`/`new`, ręczne lub przez GC zwalnianie. *Na teście:* stos = szybki, automatyczny, ograniczony; sterta = elastyczny, ręczne zarządzanie, ryzyko wycieków.

**Nadmiar (overflow) w obliczeniach stałopozycyjnych.** Wynik przekracza zakres reprezentacji danego typu. W arytmetyce ze znakiem (U2) dodanie dwóch liczb tego samego znaku dające wynik przeciwnego znaku = nadmiar. Wykrywany przez bity/flagi (carry/overflow). *Na teście:* overflow ≠ carry; nadmiar dotyczy przekroczenia zakresu liczb ze znakiem.

**Kodowanie U2 (uzupełnienie do dwóch).** Standard reprezentacji liczb całkowitych ze znakiem. Najstarszy bit ma wagę ujemną. Liczbę ujemną uzyskujemy: neguj bity i dodaj 1. Zalety: jedna reprezentacja zera, dodawanie/odejmowanie tym samym układem. Zakres n bitów: od −2^(n−1) do 2^(n−1)−1. *Na teście:* w U2 jest jedno zero i o jedną liczbę ujemną więcej niż dodatnich.

**Odwrotna notacja polska (RPN, postfix).** Operator po operandach: `3 4 +`. Nie wymaga nawiasów, łatwa do obliczenia stosem (napotkany operand → na stos; operator → zdejmij operandy, policz, wynik na stos). *Na teście:* RPN nie potrzebuje nawiasów; oblicza się stosem.

**Paradygmaty języków programowania.** Imperatywny (jak: sekwencja instrukcji), w tym proceduralny i obiektowy; deklaratywny (co: funkcyjny, logiczny). Funkcyjny — funkcje, brak efektów ubocznych; logiczny — fakty i reguły (Prolog). *Na teście:* SQL/Prolog = deklaratywne; C = imperatywne.

**Interpretacja a kompilacja.** **Kompilacja** — tłumaczenie całości kodu źródłowego na kod maszynowy przed wykonaniem (szybkie wykonanie, wolniejszy cykl budowy). **Interpretacja** — wykonywanie instrukcja po instrukcji w trakcie działania (elastyczność, wolniej). Hybryda: kod pośredni + maszyna wirtualna (Java bytecode, JIT). *Na teście:* interpreter nie tworzy pliku wykonywalnego; kompilator wykrywa błędy przed uruchomieniem.

**Rząd złożoności obliczeniowej.** Notacja asymptotyczna opisująca wzrost kosztu (czas/pamięć) w funkcji rozmiaru danych n: O (górne ograniczenie), Ω (dolne), Θ (dokładne). Typowe klasy: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!). *Na teście:* pomijamy stałe i składniki niższego rzędu; O to ograniczenie górne.

**Problemy nierozstrzygalne.** Problemy, dla których nie istnieje algorytm dający zawsze poprawną odpowiedź w skończonym czasie. Klasyczny przykład: **problem stopu** (czy program się zatrzyma). *Na teście:* nierozstrzygalny ≠ trudny obliczeniowo; to brak jakiegokolwiek algorytmu.

**Bloki funkcjonalne prostego komputera.** Model von Neumanna: **jednostka arytmetyczno-logiczna (ALU)**, **jednostka sterująca (CU)** (razie CPU), **pamięć** (wspólna dla danych i programu), **układy wejścia/wyjścia**, połączone **magistralą** (adresowa, danych, sterująca). *Na teście:* von Neumann = wspólna pamięć programu i danych; Harvard = rozdzielona.

---

## 3. Algorytmy i struktury danych

**Złożoność algorytmów sortowania.** Bąbelkowe/wstawianie/wybór: O(n²). Sortowanie przez scalanie (merge sort): O(n log n) zawsze, stabilne, dodatkowa pamięć. Szybkie (quicksort): średnio O(n log n), pesymistycznie O(n²), w miejscu. Kopcowe (heapsort): O(n log n) w miejscu, niestabilne. Dolna granica sortowań porównaniowych: **Ω(n log n)**. Sortowania pozycyjne (counting/radix): O(n) przy założeniach o kluczach. *Na teście:* żadne sortowanie porównaniowe nie zejdzie poniżej n log n; quicksort pesymistycznie n².

**Algorytmy zachłanne (greedy).** W każdym kroku wybór lokalnie najlepszy, bez cofania, w nadziei na optimum globalne. Działają poprawnie, gdy problem ma własność wyboru zachłannego i optymalną podstrukturę (np. Kruskal, Dijkstra, kod Huffmana, wydawanie reszty w „ładnych" systemach monet). *Na teście:* zachłanny nie zawsze daje optimum (np. plecak 0/1); Huffman i MST — tak.

**Najkrótsze ścieżki w grafie.** **Dijkstra** — jedno źródło, wagi nieujemne, zachłanny, O((V+E)log V) z kopcem. **Bellman-Ford** — dopuszcza wagi ujemne, wykrywa ujemne cykle, O(VE). **Floyd-Warshall** — wszystkie pary, programowanie dynamiczne, O(V³). *Na teście:* Dijkstra nie działa dla ujemnych wag; Floyd-Warshall = wszystkie pary.

**Techniki projektowania algorytmów.** Dziel i zwyciężaj (divide and conquer), programowanie dynamiczne (nakładające się podproblemy + memoizacja), zachłanne, z nawrotami (backtracking), zamiatanie, redukcja. *Na teście:* DP dla nakładających się podproblemów; D&C dla niezależnych.

**Reprezentacja grafów.** **Macierz sąsiedztwa** — O(V²) pamięci, sprawdzenie krawędzi O(1), dobra dla gęstych. **Lista sąsiedztwa** — O(V+E) pamięci, dobra dla rzadkich, iteracja po sąsiadach szybka. Macierz incydencji (wierzchołki×krawędzie). *Na teście:* macierz = szybkie sprawdzenie krawędzi, dużo pamięci; lista = oszczędna dla rzadkich.

**Maksymalny przepływ w grafie.** Sieć przepływowa: źródło s, ujście t, przepustowości krawędzi. **Twierdzenie max-flow = min-cut** (maksymalny przepływ = minimalny przekrój). Algorytmy: Ford-Fulkerson (ścieżki powiększające), Edmondsa-Karpa (BFS, O(VE²)). *Na teście:* wartość max przepływu = przepustowość min. przekroju.

**Programowanie dynamiczne.** Rozwiązywanie przez łączenie rozwiązań nakładających się podproblemów, zapamiętywanych (memoizacja top-down lub tablica bottom-up). Wymaga optymalnej podstruktury i nakładających się podproblemów. Przykłady: najdłuższy wspólny podciąg, plecak, ciąg Fibonacciego, Floyd-Warshall. *Na teście:* DP zamienia wykładniczy koszt na wielomianowy dzięki zapamiętywaniu.

---

## 4. Programowanie imperatywne

**Budowa programu wykonywalnego z kodu C.** Cztery etapy: **preprocesor** (rozwija `#include`, `#define`, dyrektywy), **kompilacja** (kod C → asembler/kod obiektowy, sprawdzenie składni), **asemblacja** (→ plik obiektowy `.o`), **konsolidacja/linkowanie** (łączy pliki obiektowe i biblioteki → plik wykonywalny, rozwiązuje symbole). *Na teście:* kolejność: preprocesor → kompilator → asembler → linker; błędy „undefined reference" = etap linkowania.

**Przekazywanie tablicy dwuwymiarowej do funkcji.** W C tablica „rozpada się" (decay) do wskaźnika. Przy tablicy 2D funkcja musi znać liczbę kolumn, by policzyć adres elementu: `void f(int a[][N])` lub `int (*a)[N]`. Alternatywnie wskaźnik + wymiary jawnie. *Na teście:* trzeba podać rozmiar drugiego (i dalszych) wymiaru; pierwszy można pominąć.

**Tablice VLA (Variable Length Array).** Tablice o rozmiarze ustalanym w czasie działania (C99), alokowane na stosie: `int a[n];` gdzie n to zmienna. Zaleta: wygoda; wada: ryzyko przepełnienia stosu dla dużych n, brak sprawdzania. W C11 opcjonalne. *Na teście:* VLA żyją na stosie, rozmiar znany dopiero w runtime.

**Przydział pamięci dla zmiennych strukturalnych w C.** Struktura zajmuje pamięć pól plus **wyrównanie (padding/alignment)** — kompilator wstawia luki, by pola leżały pod adresami zgodnymi z wymaganiami. Dlatego `sizeof(struct)` ≥ suma pól i zależy od kolejności pól. *Na teście:* rozmiar struktury zależy od wyrównania i kolejności pól; nie zawsze = suma sizeof pól.

**Funkcja biblioteczna qsort().** Uniwersalne sortowanie ze stdlib: `qsort(baza, liczba, rozmiar_elementu, komparator)`. Komparator zwraca <0, 0, >0. Działa na dowolnym typie dzięki `void*`. Średnio O(n log n). *Na teście:* qsort wymaga funkcji porównującej; nie jest stabilne wg standardu.

---

## 5. Programowanie funkcyjne i obiektowe

**Funkcja wyższego rzędu.** Funkcja przyjmująca inną funkcję jako argument i/lub zwracająca funkcję. Przykłady: `map`, `filter`, `reduce/fold`, kompozycja. *Na teście:* HOF operuje na funkcjach; `map` i `filter` to klasyczne przykłady.

**Typ algebraiczny (ADT).** Typ złożony z innych typów przez: **sumę** (wariant/union — „albo A, albo B", np. `Either`, `Maybe`) i **iloczyn** (rekord/krotka — „A i B naraz"). Dopasowanie wzorców (pattern matching) rozróżnia warianty. *Na teście:* typ sumy = wybór jednego z wariantów; iloczyn = kombinacja pól.

**Funkcyjne wzorce projektowe/obliczeniowe.** Funktor (map zachowujący strukturę), monada (sekwencjonowanie obliczeń z kontekstem, np. Maybe/IO/List), aplikatyw, currying, kompozycja funkcji, rekurencja ogonowa. *Na teście:* monada porządkuje obliczenia z efektami; funktor pozwala mapować pod strukturą.

**Rodzaje polimorfizmu w statycznie typowanych językach funkcyjnych.** **Parametryczny** (generyki — ta sama funkcja dla wszystkich typów, np. `length :: [a] -> Int`); **ad-hoc** (przeciążanie, klasy typów — różne implementacje dla różnych typów); (podtypowy — rzadziej w czysto funkcyjnych). *Na teście:* generyki = parametryczny; klasy typów/przeciążanie = ad-hoc.

**Rekursja i jej rodzaje.** Bezpośrednia/pośrednia; **ogonowa (tail)** — wywołanie rekurencyjne to ostatnia operacja, optymalizowana do pętli (stała pamięć stosu); nieogonowa (np. drzewiasta — dwa wywołania jak w Fibonaccim). *Na teście:* rekursja ogonowa może być zoptymalizowana (TCO) i nie rośnie stos.

**Leniwe (lazy) obliczanie wyrażeń.** Wartość liczona dopiero, gdy jest potrzebna (call-by-need), z zapamiętaniem wyniku. Umożliwia nieskończone struktury (strumienie), unika zbędnych obliczeń. Przeciwieństwo: gorliwe (eager/strict). *Na teście:* lazy = obliczenie odroczone; pozwala na nieskończone listy (Haskell).

**Cechy języków obiektowych.** **Abstrakcja**, **hermetyzacja (enkapsulacja)** — ukrycie stanu za interfejsem, **dziedziczenie** — ponowne użycie i hierarchia, **polimorfizm** — jeden interfejs, wiele implementacji. *Na teście:* to klasyczna czwórka; hermetyzacja ≠ dziedziczenie.

---

## 6. Podstawy baz danych

**Własności transakcji (ACID).** **Atomicity** (atomowość — wszystko albo nic), **Consistency** (spójność — z jednego poprawnego stanu do drugiego), **Isolation** (izolacja — transakcje nie zakłócają się wzajemnie), **Durability** (trwałość — zatwierdzone zmiany przetrwają awarię). *Na teście:* zapamiętaj ACID; izolacja dotyczy współbieżności, trwałość — awarii.

**Model związków encji (ERD).** Konceptualny model danych: **encje** (obiekty), **atrybuty** (cechy), **związki** (relacje) z **licznością** (1:1, 1:N, M:N) i opcjonalnością. Podstawa projektowania schematu relacyjnego. *Na teście:* związek M:N wymaga tabeli łączącej w modelu relacyjnym.

**Klucze w modelu relacyjnym.** **Superklucz** — zbiór atrybutów jednoznacznie identyfikujący krotkę. **Klucz kandydujący** — minimalny superklucz. **Klucz główny (primary)** — wybrany kandydujący; unikalny, NOT NULL. **Klucz obcy (foreign)** — odwołanie do klucza w innej tabeli (integralność referencyjna). *Na teście:* klucz główny ≠ NULL i unikalny; obcy zapewnia integralność referencyjną.

**Algebra relacji.** Formalny język operacji na relacjach: **selekcja σ** (wybór wierszy wg warunku), **projekcja π** (wybór kolumn), **złączenie ⋈ (join)**, **iloczyn kartezjański ×**, suma ∪, różnica −, przecięcie ∩, przemianowanie ρ. Podstawa teoretyczna SQL. *Na teście:* σ = wiersze, π = kolumny; join łączy relacje po warunku.

**Normalizacja. Postacie normalne.** Proces eliminacji redundancji i anomalii przez rozkład tabel. **1NF** — wartości atomowe, brak grup powtarzalnych. **2NF** — 1NF + brak zależności częściowej od klucza. **3NF** — 2NF + brak zależności przechodnich (nieklucz od nieklucza). **BCNF** — mocniejsza 3NF. *Na teście:* 2NF usuwa zależności częściowe, 3NF przechodnie; normalizacja redukuje redundancję kosztem złączeń.

**Widoki (views).** Wirtualna tabela zdefiniowana zapytaniem; nie przechowuje danych (poza materializowanym). Zastosowania: uproszczenie zapytań, warstwa bezpieczeństwa (ukrycie kolumn/wierszy), niezależność logiczna. *Na teście:* zwykły widok nie zajmuje miejsca na dane; materializowany — tak.

**Indeksy.** Struktura (najczęściej **B-drzewo**, też haszujące) przyspieszająca wyszukiwanie kosztem miejsca i wolniejszych zapisów (INSERT/UPDATE muszą aktualizować indeks). *Na teście:* indeks przyspiesza SELECT, spowalnia modyfikacje; B-drzewo dobre dla zakresów, hasz dla równości.

---

## 7. Technika cyfrowa

**Bramki trójstanowe (three-state).** Oprócz stanów 0 i 1 mają stan **wysokiej impedancji (Z)** — wyjście „odłączone". Sterowane sygnałem enable. Umożliwiają podłączenie wielu wyjść do wspólnej **magistrali** (tylko jedno aktywne naraz). *Na teście:* stan Z = odcięcie od magistrali; klucz do współdzielenia szyny.

**Tablice Karnaugha.** Graficzna metoda minimalizacji funkcji logicznych. Sąsiednie komórki różnią się jednym bitem (kod Graya); grupowanie jedynek w potęgi dwójki (1,2,4,8...) eliminuje zmienne. Redukuje liczbę bramek. *Na teście:* grupy muszą być potęgą 2 i „owijają się" na brzegach; większa grupa = prostsze wyrażenie.

**Układy synchroniczne i asynchroniczne.** **Synchroniczne** — zmiany stanu taktowane wspólnym **zegarem** (przewidywalne, łatwiejsze projektowanie). **Asynchroniczne** — reagują natychmiast na zmiany wejść, bez zegara (szybsze, ale podatne na hazardy, trudniejsze). *Na teście:* synchroniczny = wspólny zegar; asynchroniczny = brak zegara, ryzyko wyścigów.

**Multipleksery i demultipleksery.** **MUX** — wybiera jedno z wielu wejść na jedno wyjście wg linii adresowych (2ⁿ wejść → n linii wyboru). **DEMUX** — kieruje jedno wejście na jedno z wielu wyjść. MUX to „przełącznik", może realizować dowolną funkcję logiczną. *Na teście:* n linii adresowych obsługuje 2ⁿ wejść MUX.

**Hazardy.** Chwilowe, niepożądane stany na wyjściu wskutek różnych opóźnień propagacji ścieżek. **Statyczny** (wyjście powinno być stałe, a pojawia się impuls), **dynamiczny** (przy zmianie pojawiają się dodatkowe przełączenia). Usuwa się redundantnymi składnikami / synchronizacją. *Na teście:* hazard wynika z różnic opóźnień; groźny w układach asynchronicznych.

**Rejestry.** Zespoły przerzutników przechowujące słowo bitowe. Rodzaje: równoległe (parallel), **przesuwające (shift)** — dane wędrują bit po bicie; konwersja szeregowo-równoległa (SIPO/PISO). *Na teście:* rejestr przesuwny służy m.in. konwersji szeregowej↔równoległej i mnożeniu/dzieleniu przez 2.

**Liczniki.** Układy zliczające impulsy. **Asynchroniczne (rippl)** — przerzutniki taktowane kaskadowo (wolniejsze, propagacja); **synchroniczne** — wszystkie taktowane wspólnym zegarem (szybsze). Modulo N, w górę/w dół. *Na teście:* licznik synchroniczny szybszy i bez narastającego opóźnienia.

**Sumatory i półsumatory.** **Półsumator (half adder)** — dodaje 2 bity, daje sumę i przeniesienie, brak wejścia carry. **Sumator pełny (full adder)** — dodaje 3 bity (w tym carry-in), daje sumę i carry-out. Łączenie w kaskadę = sumator równoległy (ripple carry). *Na teście:* half adder nie ma wejścia przeniesienia, full adder ma.

**Przerzutniki (flip-flopy).** Podstawowe elementy pamięci 1 bitu. Rodzaje: **SR** (set/reset, stan zabroniony), **D** (data — zatrzask danych), **JK** (uniwersalny, brak stanu zabronionego, przełącza dla J=K=1), **T** (toggle — zmienia stan). Wyzwalane poziomem (latch) lub zboczem (edge). *Na teście:* JK usuwa stan zabroniony SR; T służy do liczników.

**Automaty w technice cyfrowej.** Maszyny stanów (FSM): **Moore** — wyjście zależy tylko od stanu; **Mealy** — wyjście zależy od stanu i wejścia (zwykle mniej stanów, szybsza reakcja). Opis: graf stanów, tablica przejść. *Na teście:* Moore = wyjście od stanu; Mealy = od stanu i wejścia.

**Układy kombinacyjne i sekwencyjne.** **Kombinacyjne** — wyjście zależy tylko od bieżących wejść (brak pamięci): bramki, MUX, sumatory, dekodery. **Sekwencyjne** — wyjście zależy od wejść i stanu (mają pamięć): przerzutniki, rejestry, liczniki, automaty. *Na teście:* kombinacyjny = bez pamięci; sekwencyjny = z pamięcią stanu.

---

## 8. Technika mikroprocesorowa

**DMA (Direct Memory Access).** Układ (kontroler DMA) przenoszący dane między pamięcią a urządzeniem I/O **bez udziału procesora**. CPU zleca transfer i jest wolny do innych zadań; DMA zgłasza przerwanie po zakończeniu. *Na teście:* DMA odciąża CPU przy dużych transferach; kradnie cykle magistrali (cycle stealing).

**Pamięć statyczna vs dynamiczna.** **SRAM** — przechowuje bit w przerzutniku, szybka, droga, nie wymaga odświeżania (cache). **DRAM** — bit w kondensatorze, tania, gęsta, **wymaga odświeżania** (rozładowuje się), wolniejsza (pamięć główna). *Na teście:* DRAM wymaga odświeżania i jest wolniejsza; SRAM w cache.

**Pamięć Flash.** Nieulotna, elektrycznie kasowalna (odmiana EEPROM), kasowanie **blokami**. Typy NOR (szybki odczyt losowy, kod) i NAND (gęsta, dane, dyski SSD). Ograniczona liczba cykli zapisu/kasowania (zużycie). *Na teście:* Flash nieulotna, kasowana blokowo, ograniczona żywotność komórek.

**RISC vs CISC.** **RISC** — mało prostych, jednakowej długości rozkazów, wykonywanych zwykle w 1 cyklu, dużo rejestrów, architektura load/store, sprzyja potokowaniu (ARM, RISC-V). **CISC** — dużo złożonych rozkazów o zmiennej długości, operacje pamięć-pamięć, mniej rejestrów (x86). *Na teście:* RISC = proste stałej długości rozkazy, łatwe potokowanie; CISC = złożone, zmiennej długości.

**Potokowe wykonywanie rozkazów (pipelining).** Nakładanie faz przetwarzania rozkazów (pobranie, dekodowanie, wykonanie, dostęp do pamięci, zapis) — kilka rozkazów jednocześnie na różnych etapach. Zwiększa przepustowość. Zagrożenia (hazardy): strukturalne, danych, sterowania (skoki). *Na teście:* potok zwiększa przepustowość, nie skraca czasu pojedynczego rozkazu; skoki powodują hazardy sterowania.

**Modyfikator volatile w C/C++.** Informuje kompilator, że zmienna może zmienić się „z zewnątrz" (przerwanie, sprzęt, inny wątek), więc **nie wolno optymalizować** dostępów (każdy odczyt z pamięci realny). Stosowany do rejestrów sprzętowych, zmiennych w ISR. *Na teście:* volatile wyłącza optymalizacje odczytów/zapisów; nie zapewnia atomowości ani synchronizacji.

---

## 9. Architektura komputerów

**Pamięć podręczna (cache).** Szybka, mała pamięć między CPU a RAM, wykorzystująca **lokalność** czasową i przestrzenną. Poziomy L1/L2/L3. Zaleta: skraca średni czas dostępu. Wada: koszt, złożoność (spójność cache w wieloprocesorach), problem trafień/chybień (hit/miss). *Na teście:* cache działa dzięki lokalności odwołań; miss powoduje sięgnięcie do wolniejszej pamięci.

**Prawo Amdahla i Gustafsona.** **Amdahl** — przyspieszenie ograniczone częścią sekwencyjną programu: dla stałego problemu maksymalne przyspieszenie = 1/(s + (1−s)/p); część nierównoległa limituje zysk. **Gustafson** — dla rosnącego problemu przyspieszenie skaluje się liniowo (zwiększamy rozmiar zadania z liczbą procesorów). *Na teście:* Amdahl = stały rozmiar, pesymistyczny; Gustafson = skalowany rozmiar, optymistyczny.

**Benchmarki HPCG i LINPACK (HPL).** **LINPACK/HPL** — rozwiązywanie gęstego układu równań; mierzy szczytową wydajność zmiennoprzecinkową (FLOPS), podstawa listy TOP500 (compute-bound). **HPCG** — rzadkie macierze, wzorzec zbliżony do realnych aplikacji, obciąża pamięć/komunikację (memory-bound), daje niższe, „realistyczniejsze" wyniki. *Na teście:* HPL faworyzuje moc obliczeniową, HPCG — przepustowość pamięci.

**Taksonomia Flynna.** Klasyfikacja wg strumieni instrukcji i danych: **SISD** (klasyczny jednoprocesor), **SIMD** (jedna instrukcja, wiele danych — wektory, GPU), **MISD** (rzadki), **MIMD** (wiele instrukcji i danych — wieloprocesory, klastry). *Na teście:* GPU/wektory = SIMD; klaster wielordzeniowy = MIMD.

**Wydajność współczesnego komputera.** Zależy od: częstotliwości zegara, IPC (instrukcje/cykl), liczby rdzeni, hierarchii pamięci (cache), przepustowości pamięci i I/O. Miary: FLOPS, IPS, czas wykonania. Uwaga na „ścianę pamięci" i granice skalowania (Amdahl). *Na teście:* sama częstotliwość nie decyduje; liczy się też IPC, rdzenie, pamięć.

---

## 10. Inżynieria oprogramowania

**Model kaskadowy (waterfall).** Sekwencyjne, nienakładające się fazy: wymagania → projekt → implementacja → testy → wdrożenie → utrzymanie. Zalety: prostota, dobra dokumentacja, jasne kamienie milowe. Wady: sztywność, późne wykrycie błędów, kosztowne zmiany, klient widzi efekt na końcu. *Na teście:* waterfall = sekwencyjny, słaby przy zmiennych wymaganiach.

**Metodyki zwinne vs klasyczne.** **Klasyczne** (waterfall, V-model) — planowanie z góry, sztywne, dokumentacja. **Zwinne (agile)** — iteracyjno-przyrostowe, adaptacja do zmian, częste dostarczanie, współpraca z klientem, mniej dokumentacji. *Na teście:* agile = iteracyjne i elastyczne; klasyczne = predykcyjne i sekwencyjne.

**Agile Manifesto.** Cztery wartości: **ludzie i interakcje** ponad procesy i narzędzia; **działające oprogramowanie** ponad dokumentację; **współpraca z klientem** ponad negocjacje umów; **reagowanie na zmiany** ponad realizację planu. 12 zasad. *Na teście:* „ponad" nie znaczy „zamiast" — prawa strona też ma wartość, lewa większą.

**Testy w inżynierii oprogramowania.** Poziomy: **jednostkowe** (moduł), **integracyjne** (współpraca modułów), **systemowe** (całość), **akceptacyjne** (spełnienie wymagań klienta). Rodzaje: czarnoskrzynkowe/białoskrzynkowe, regresji, wydajnościowe. *Na teście:* testy jednostkowe najniższy poziom; akceptacyjne robi/zatwierdza klient.

**Weryfikacja i walidacja.** **Weryfikacja** — „czy budujemy produkt poprawnie?" (zgodność ze specyfikacją). **Walidacja** — „czy budujemy właściwy produkt?" (zgodność z potrzebami użytkownika). *Na teście:* weryfikacja = wobec specyfikacji, walidacja = wobec potrzeb.

**Wymagania funkcjonalne i niefunkcjonalne.** **Funkcjonalne** — co system ma robić (funkcje, zachowania). **Niefunkcjonalne** — jak (jakość): wydajność, bezpieczeństwo, niezawodność, użyteczność, skalowalność. *Na teście:* „system ma logować użytkownika" = funkcjonalne; „odpowiedź < 1 s" = niefunkcjonalne.

**Kanban i Scrum.** **Scrum** — role (Product Owner, Scrum Master, Zespół), sprinty o stałej długości, artefakty (backlog produktu/sprintu, inkrement), zdarzenia (planning, daily, review, retrospektywa). **Kanban** — wizualizacja przepływu (tablica), limity WIP, ciągły przepływ bez sprintów i wyznaczonych ról. *Na teście:* Scrum = iteracje/role; Kanban = ciągły przepływ i limity WIP.

**Studium wykonalności.** Wczesna analiza, czy projekt warto i da się zrealizować: wykonalność techniczna, ekonomiczna (koszt/korzyść), organizacyjna, prawna, harmonogramowa. Decyzja go/no-go. *Na teście:* to analiza opłacalności i realności przed rozpoczęciem projektu.

**Diagramy UML.** Ujednolicony język modelowania. **Strukturalne**: klas, obiektów, komponentów, wdrożenia, pakietów. **Behawioralne**: przypadków użycia, sekwencji, aktywności, stanów, komunikacji. *Na teście:* diagram klas = struktura statyczna; sekwencji/aktywności = zachowanie/dynamika.

---

## 11. Metody obliczeniowe w nauce i technice

**Numeryczna reprezentacja liczb rzeczywistych.** Skończona liczba bitów → skończony, nierównomiernie rozłożony zbiór liczb (gęściej blisko zera). Stąd błędy zaokrągleń, epsilon maszynowy, brak dokładnej reprezentacji wielu ułamków. *Na teście:* liczby zmiennoprzecinkowe są dyskretne i nierównomierne; nie każda liczba dziesiętna jest reprezentowalna.

**Arytmetyka zmiennoprzecinkowa (IEEE 754).** Liczba = znak × mantysa × 2^wykładnik. Cechy: skończona precyzja, **błędy zaokrągleń**, brak łączności dodawania, **utrata cyfr znaczących** przy odejmowaniu bliskich liczb (cancellation), wartości specjalne (±∞, NaN, zero ze znakiem). *Na teście:* dodawanie float nie jest łączne; odejmowanie bliskich liczb traci precyzję.

**Divide and conquer w metodach numerycznych.** Podział problemu na mniejsze, rozwiązanie i scalenie (FFT, szybkie mnożenie macierzy, rekurencyjne całkowanie adaptacyjne). Redukuje złożoność (np. FFT O(n log n) zamiast O(n²)). *Na teście:* FFT to sztandarowy przykład D&C w numeryce.

**Wielomiany ortogonalne.** Rodziny wielomianów (Legendre'a, Czebyszewa, Hermite'a, Laguerre'a) ortogonalnych względem iloczynu skalarnego z wagą. Zastosowania: aproksymacja (minimalizacja błędu), kwadratury Gaussa (węzły = pierwiastki wielomianu), stabilne obliczenia. **Czebyszew** minimalizuje błąd maksymalny (oscylacje Rungego). *Na teście:* węzły kwadratur Gaussa to pierwiastki wielomianów ortogonalnych; Czebyszew ogranicza efekt Rungego.

**Kwadratury Newtona-Cotesa i Gaussa.** Numeryczne całkowanie. **Newton-Cotes** — węzły równoodległe (trapezów, Simpsona); prosta, ale niestabilna przy wysokim stopniu. **Gauss** — węzły i wagi dobrane optymalnie; kwadratura n-węzłowa jest dokładna dla wielomianów stopnia ≤ 2n−1. *Na teście:* Gauss dokładniejszy przy tej samej liczbie węzłów; Simpson to Newton-Cotes.

**Numeryczne rozwiązywanie układów równań liniowych.** **Metody bezpośrednie** — eliminacja Gaussa, rozkład LU, Cholesky'ego (macierze symetryczne dodatnio określone); dają wynik w skończonej liczbie kroków. **Iteracyjne** — Jacobiego, Gaussa-Seidla, gradientów sprzężonych; dobre dla dużych rzadkich układów. Uwaga na **uwarunkowanie** macierzy. *Na teście:* metody bezpośrednie = skończona liczba kroków; iteracyjne dla dużych rzadkich; źle uwarunkowana macierz = duże błędy.

**Numeryczne rozwiązywanie równań nieliniowych.** **Bisekcja** — pewna, wolna (liniowa zbieżność), wymaga zmiany znaku. **Newton-Raphson** — szybka (kwadratowa), wymaga pochodnej i dobrego punktu startowego, może rozbiegać. **Sieczne** — bez pochodnej, nadliniowa. *Na teście:* Newton kwadratowo zbieżny ale nie zawsze; bisekcja zawsze zbieżna w przedziale ze zmianą znaku.

**Metody generowania liczb losowych.** **Generatory pseudolosowe (PRNG)** — deterministyczne, powtarzalne przy tym samym ziarnie (np. liniowy kongruencyjny LCG, Mersenne Twister); mają okres. **Sprzętowe/prawdziwie losowe** — ze źródeł fizycznych. Transformacje rozkładów (odwrotnej dystrybuanty, Boxa-Mullera). *Na teście:* PRNG jest deterministyczny i okresowy; to samo ziarno = ta sama sekwencja.

---

## 12. Podstawy sztucznej inteligencji

**Uczenie nadzorowane.** Model uczy się z **danych etykietowanych** (wejście→oczekiwane wyjście). Zadania: klasyfikacja (etykiety dyskretne) i regresja (wartości ciągłe). Przykłady: drzewa, SVM, sieci, regresja liniowa/logistyczna. Ryzyko przeuczenia (overfitting). *Na teście:* nadzorowane = etykiety; klasyfikacja vs regresja.

**Uczenie nienadzorowane.** Dane **bez etykiet** — szukanie struktury: **klasteryzacja** (k-średnich, hierarchiczna), redukcja wymiarowości (PCA), reguły asocjacyjne. *Na teście:* brak etykiet; k-means i PCA to klasyka; grupowanie ≠ klasyfikacja.

**Budowa sztucznych sieci neuronowych.** Warstwy neuronów (wejściowa, ukryte, wyjściowa). Neuron: suma ważona wejść + bias → **funkcja aktywacji** (sigmoid, tanh, ReLU) wprowadzająca nieliniowość. Uczenie = dostrajanie wag. *Na teście:* bez nieliniowej aktywacji sieć wielowarstwowa = model liniowy; ReLU popularna w głębokich sieciach.

**Wsteczna propagacja błędu (backpropagation).** Algorytm uczenia sieci: propagacja w przód (oblicz wyjście i błąd), potem wstecz — obliczenie gradientu funkcji straty względem wag **regułą łańcuchową** i aktualizacja wag (spadek gradientu). *Na teście:* backprop liczy gradienty regułą łańcuchową i wymaga różniczkowalnych aktywacji.

**Rekurencyjne sieci neuronowe (RNN).** Sieci ze sprzężeniem zwrotnym, mają **stan/pamięć** — przetwarzają sekwencje (tekst, mowa, szeregi czasowe). Problem zanikającego/eksplodującego gradientu → warianty **LSTM/GRU** z bramkami. *Na teście:* RNN dla danych sekwencyjnych; LSTM/GRU rozwiązują zanikający gradient.

**Algorytm A\*.** Wyszukiwanie najkrótszej ścieżki z **heurystyką**: minimalizuje f(n) = g(n) (koszt dotychczasowy) + h(n) (szacowany koszt do celu). Jest **optymalny i zupełny**, gdy heurystyka jest **dopuszczalna** (nie przeszacowuje) i spójna. *Na teście:* A\* = Dijkstra + heurystyka; dopuszczalna heurystyka gwarantuje optymalność; h=0 → A\* = Dijkstra.

---

## 13. Systemy operacyjne

**Algorytmy szeregowania (scheduling).** Decydują, który proces dostaje CPU. **FCFS** (kolejność zgłoszeń — efekt konwoju), **SJF** (najkrótsze zadanie — optymalne dla śr. czasu oczekiwania, ryzyko głodzenia), **Round Robin** (kwant czasu — sprawiedliwy, interaktywny), **priorytetowy**, **wielopoziomowe kolejki**. Wywłaszczające vs niewywłaszczające. *Na teście:* RR z małym kwantem = dużo przełączeń; SJF minimalizuje średni czas oczekiwania ale głodzi długie zadania.

**Mechanizmy synchronizacji (scentralizowane i rozproszone).** Scentralizowane: **semafory**, **muteksy**, **monitory**, zmienne warunkowe. Rozproszone: algorytmy wzajemnego wykluczania (token ring, Ricart-Agrawala, Lamport), brak wspólnej pamięci → komunikacja komunikatami. *Na teście:* semafor/mutex/monitor to prymitywy; w rozproszeniu synchronizacja przez wiadomości i znaczniki czasu.

**Podstawowe problemy synchronizacyjne.** **Producent-konsument** (bufor ograniczony), **czytelnicy-pisarze** (współdzielony zasób), **ucztujący filozofowie** (zakleszczenie i głodzenie), **fryzjer**. Ilustrują wzajemne wykluczanie, zakleszczenia, głodzenie. *Na teście:* filozofowie = klasyczny przykład zakleszczenia; producent-konsument rozwiązywany semaforami.

**Proces a wątek.** **Proces** — własna przestrzeń adresowa, izolowany, kosztowne przełączanie i tworzenie. **Wątek** — jednostka wykonania w obrębie procesu, **współdzieli pamięć** i zasoby procesu, lekki, szybkie przełączanie, ale wymaga synchronizacji. *Na teście:* wątki jednego procesu dzielą pamięć; procesy są izolowane.

**Pamięć wirtualna — stronicowanie i segmentacja.** **Stronicowanie** — podział pamięci na stałej wielkości **strony/ramki**, mapowanie przez tablicę stron, brak fragmentacji zewnętrznej (jest wewnętrzna). **Segmentacja** — podział logiczny na segmenty zmiennej długości (kod/dane/stos), fragmentacja zewnętrzna. **Page fault** ładuje brakującą stronę z dysku. *Na teście:* stronicowanie = stały rozmiar + fragmentacja wewnętrzna; segmentacja = zmienny + zewnętrzna.

**Systemy czasu rzeczywistego.** Kluczowa jest **terminowość** (dotrzymanie deadline), nie sama szybkość. **Twarde (hard RT)** — przekroczenie terminu = katastrofa. **Miękkie (soft RT)** — dopuszczalne pogorszenie jakości. Wymagają determinizmu i przewidywalnego szeregowania. *Na teście:* RT = przewidywalność/terminy, niekoniecznie „najszybszy".

**Tworzenie procesów.** W UNIX: **fork()** tworzy kopię procesu (dziecko dziedziczy przestrzeń — copy-on-write), zwraca 0 dziecku, PID rodzicowi; **exec()** podmienia obraz procesu na nowy program; **wait()** — rodzic czeka na dziecko. *Na teście:* fork tworzy kopię, exec zastępuje kod; osierocony/zombie to stany procesu potomnego.

**Zakleszczenie (deadlock).** Grupa procesów wzajemnie czeka na zasoby. Cztery **warunki Coffmana** (konieczne): wzajemne wykluczanie, trzymaj i czekaj, brak wywłaszczania, **cykliczne oczekiwanie**. Strategie: zapobieganie, unikanie (algorytm bankiera), wykrywanie i usuwanie, ignorowanie. *Na teście:* zerwanie choć jednego z 4 warunków usuwa możliwość zakleszczenia; bankier = unikanie.

**Moduł — łączenie statyczne i dynamiczne.** **Statyczne** — biblioteka wkompilowana w plik wykonywalny (większy plik, samodzielny, aktualizacja = rekompilacja). **Dynamiczne** — biblioteka (.so/.dll) ładowana w czasie uruchomienia/działania, współdzielona między programami (mniejszy plik, łatwa aktualizacja, zależność od wersji). *Na teście:* dynamiczne = współdzielenie i mniejszy plik; statyczne = samodzielność.

---

## 14. Sieci komputerowe

**Cechy adresacji IP.** Adres logiczny warstwy sieciowej (L3), **hierarchiczny** (część sieci + host), routowalny. **IPv4** — 32 bity (4 oktety), maska/prefiks (CIDR), klasy historyczne, adresy prywatne/publiczne, NAT. **IPv6** — 128 bitów. *Na teście:* IP jest logiczny i hierarchiczny (routing po prefiksie); MAC — płaski i fizyczny.

**Cechy adresacji MAC.** Adres fizyczny warstwy łącza (L2), **płaski** (nie hierarchiczny), przypisany na stałe kartom sieciowym, lokalny dla segmentu sieci (nie routowalny). *Na teście:* MAC nie jest routowalny; działa w obrębie sieci lokalnej / domeny rozgłoszeniowej.

**Struktura adresu MAC.** 48 bitów = 6 bajtów, zapis heksadecymalny. Pierwsze 3 bajty = **OUI** (identyfikator producenta, nadawany przez IEEE), ostatnie 3 = numer nadany przez producenta. Bity w pierwszym bajcie: I/G (indywidualny/grupowy) i U/L (uniwersalny/lokalny). Adres rozgłoszeniowy = same jedynki (FF:FF:FF:FF:FF:FF). *Na teście:* MAC = 48 bitów, OUI identyfikuje producenta.

**Konfiguracja i autokonfiguracja hostów.** Ręczna (statyczna) lub automatyczna: **DHCP** (serwer przydziela IP, maskę, bramę, DNS — dzierżawa). W IPv6 dodatkowo **SLAAC** (bezstanowa autokonfiguracja z prefiksu ogłaszanego przez router) i APIPA/link-local. *Na teście:* DHCP = stanowe przydzielanie adresów; SLAAC = bezstanowe w IPv6.

**Protokoły warstwy transportowej.** **TCP** — połączeniowy, niezawodny (potwierdzenia, retransmisje, numeracja), kontrola przepływu i przeciążenia, strumień, wolniejszy. **UDP** — bezpołączeniowy, zawodny, bez potwierdzeń, mały narzut, szybki (VoIP, streaming, DNS). *Na teście:* TCP niezawodny i połączeniowy; UDP szybki bez gwarancji dostarczenia.

**Routing w sieciach IP.** Węzeł podejmuje decyzję na podstawie **tablicy routingu** — dopasowanie adresu docelowego do wpisów regułą **najdłuższego pasującego prefiksu** (longest prefix match); przekazanie do next-hop lub bramy domyślnej. *Na teście:* wybór trasy = najdłuższy pasujący prefiks; brak trasy → brama domyślna.

**Wirtualne sieci lokalne (VLAN).** Logiczny podział sieci L2 na odrębne domeny rozgłoszeniowe niezależnie od fizycznego okablowania (znakowanie ramek **802.1Q**). Zalety: segmentacja, bezpieczeństwo, ograniczenie broadcastu, elastyczność. Ruch między VLAN wymaga routera/L3. *Na teście:* VLAN dzieli domeny rozgłoszeniowe; komunikacja między VLAN wymaga routingu.

**Klasyfikacja protokołów routingu dynamicznego.** Wg zasięgu: **IGP** (wewnątrz systemu autonomicznego: RIP, OSPF, EIGRP) i **EGP** (między AS: BGP). Wg algorytmu: **wektor odległości** (distance-vector, RIP — wymiana tablic z sąsiadami) i **stan łącza** (link-state, OSPF — pełna mapa topologii, Dijkstra). *Na teście:* OSPF = link-state; RIP = distance-vector; BGP = między systemami autonomicznymi.

**Odwzorowanie IPv4 → MAC (ARP).** Protokół **ARP** znajduje adres MAC odpowiadający znanemu IP w sieci lokalnej: rozgłoszenie „kto ma ten IP?", odpowiedź z MAC, buforowanie w tablicy ARP. W IPv6 zastępuje to NDP. *Na teście:* ARP mapuje IP→MAC przez broadcast; działa w obrębie sieci lokalnej.

**Protokół STP (802.1d).** Zapobiega **pętlom** w przełączanej sieci L2 z redundantnymi łączami. Wybiera **root bridge** (najniższy Bridge ID), liczy najkrótsze ścieżki i **blokuje** nadmiarowe łącza, budując drzewo rozpinające. Awaria łącza → rekonfiguracja. *Na teście:* STP eliminuje pętle L2 blokując porty; wybiera most główny wg Bridge ID.

---

## 15. Systemy rozproszone

**Teoria CAP.** W systemie rozproszonym z danymi replikowanymi nie da się jednocześnie zapewnić wszystkich trzech: **Consistency** (spójność — każdy odczyt widzi najnowszy zapis), **Availability** (dostępność — każde żądanie dostaje odpowiedź), **Partition tolerance** (odporność na podział sieci). Przy podziale sieci wybieramy C albo A. *Na teście:* w razie partycji trzeba poświęcić C lub A; P jest w praktyce nieunikniona. (Uwaga: w oryginale błędnie „Atomicity" — poprawnie **Availability**.)

**Zadania warstwy pośredniczącej (middleware).** Warstwa między systemem operacyjnym/siecią a aplikacją: ukrywa heterogeniczność i szczegóły komunikacji, zapewnia **przezroczystość**, zdalne wywołania (RPC/RMI), nazewnictwo, synchronizację, bezpieczeństwo, zarządzanie transakcjami. *Na teście:* middleware = warstwa ukrywająca rozproszenie i ułatwiająca komunikację.

**Systemy reaktywne (Reactive Manifesto).** Cztery cechy: **Responsive** (responsywny — szybka odpowiedź), **Resilient** (odporny na awarie — izolacja, replikacja), **Elastic** (elastyczny — skaluje się z obciążeniem), **Message-driven** (oparty na asynchronicznych komunikatach — luźne powiązanie). *Na teście:* fundament = przesyłanie komunikatów; z niego wynikają elastyczność i odporność, a efektem jest responsywność.

**Zegar Lamporta.** Logiczny licznik porządkujący zdarzenia w systemie bez wspólnego zegara. Reguły: inkrementacja przy każdym zdarzeniu; przy wysłaniu dołącz znacznik; przy odbiorze `zegar = max(lokalny, otrzymany) + 1`. Zapewnia: jeśli a→b (przyczynowość), to L(a) < L(b) (nie odwrotnie). *Na teście:* zegar Lamporta daje częściowy porządek zgodny z przyczynowością; nie wykrywa współbieżności (od tego zegary wektorowe).

**Wzorzec REST.** Styl architektoniczny usług sieciowych oparty na HTTP: **bezstanowość** (każde żądanie kompletne), **zasoby** identyfikowane przez URI, operacje metodami HTTP (GET/POST/PUT/DELETE), reprezentacje (JSON/XML), jednolity interfejs, klient-serwer, cache. *Na teście:* REST jest bezstanowy i zasobowy; stan sesji nie jest trzymany po stronie serwera.

**Przezroczystość w systemach rozproszonych.** Ukrywanie faktu rozproszenia przed użytkownikiem. Typy: **dostępu** (jednolity dostęp lokalny/zdalny), **położenia** (nie wiadomo gdzie zasób), **migracji**, **replikacji**, **współbieżności**, **awarii**, **skalowania**. *Na teście:* przezroczystość położenia = użytkownik nie zna fizycznej lokalizacji zasobu.

**Komunikacja przez gniazda (sockets).** Interfejs programistyczny do komunikacji sieciowej (para: IP + port). **Strumieniowe (TCP)** — niezawodne, połączeniowe; **datagramowe (UDP)** — szybkie, bezpołączeniowe. Zalety: uniwersalność, kontrola. Wady: niski poziom abstrakcji, ręczna obsługa błędów/serializacji. *Na teście:* gniazdo = IP+port; TCP-socket niezawodny, UDP-socket szybki.

---

## 16. Teoria automatów i języków formalnych

**Klasyfikacja Chomsky'ego.** Hierarchia gramatyk/języków: **Typ 0** — rekurencyjnie przeliczalne (maszyna Turinga). **Typ 1** — kontekstowe (automat liniowo ograniczony). **Typ 2** — bezkontekstowe (automat ze stosem). **Typ 3** — regularne (automat skończony). Każdy wyższy typ zawiera niższe. *Na teście:* regularne ⊂ bezkontekstowe ⊂ kontekstowe ⊂ rekurencyjnie przeliczalne; typ 3 = automat skończony, typ 2 = stosowy.

**Postać normalna Chomsky'ego (CNF).** Gramatyka bezkontekstowa, w której każda produkcja ma postać A→BC (dwa nieterminale) lub A→a (jeden terminal). Umożliwia algorytm **CYK** rozpoznawania słów O(n³). *Na teście:* CNF = produkcje do dwóch nieterminali albo jednego terminala; podstawa CYK.

**Postać normalna Greibach (GNF).** Każda produkcja postaci A→aα, gdzie a to terminal, a α to (możliwie pusty) ciąg nieterminali. Terminal na początku prawej strony → brak lewostronnej rekurencji, przydatne w analizie zstępującej. *Na teście:* GNF zaczyna prawą stronę terminalem; eliminuje rekurencję lewostronną.

**Wieloznaczność gramatyki.** Gramatyka jest **wieloznaczna**, jeśli istnieje słowo z więcej niż jednym drzewem wyprowadzenia (lub skrajnie lewym wyprowadzeniem). Problem przy parsowaniu (np. „dangling else"). Niektóre języki są **istotnie wieloznaczne** (brak jednoznacznej gramatyki). *Na teście:* wieloznaczność = ≥2 drzewa wywodu dla jednego słowa; problem nierozstrzygalny ogólnie.

---

## 17. Teoria obliczeń i złożoności obliczeniowej

**Problem stopu.** Czy dowolny program zatrzyma się dla danego wejścia — **nierozstrzygalny** (dowód Turinga przez przekątniową sprzeczność). Fundamentalne ograniczenie obliczalności. *Na teście:* nie istnieje ogólny algorytm rozstrzygający zatrzymanie; klasyczny problem nierozstrzygalny.

**Problem P vs NP.** **P** — problemy rozwiązywalne w czasie wielomianowym. **NP** — rozwiązanie da się **zweryfikować** w czasie wielomianowym. Pytanie: czy P = NP (nierozstrzygnięte). Problemy **NP-zupełne** — najtrudniejsze w NP; jeśli którykolwiek jest w P, to P=NP. *Na teście:* NP = łatwa weryfikacja, niekoniecznie łatwe znajdowanie; SAT to pierwszy problem NP-zupełny (Cook-Levin).

**Rozstrzygalność problemu.** Problem **rozstrzygalny** — istnieje algorytm zawsze kończący się poprawną odpowiedzią TAK/NIE. **Częściowo rozstrzygalny (rekurencyjnie przeliczalny)** — algorytm zatrzymuje się dla „TAK", ale może nie kończyć dla „NIE". *Na teście:* rozstrzygalny = zawsze się zatrzymuje z odpowiedzią; problem stopu jest r.p. ale nierozstrzygalny.

**Złożoność obliczeniowa problemów.** Bada zasoby (czas, pamięć) niezbędne do rozwiązania problemu (nie konkretnego algorytmu). Dolne granice, złożoność najgorszego/średniego przypadku. *Na teście:* złożoność problemu = najlepsza możliwa, złożoność algorytmu = konkretnej metody.

**Klasy złożoności.** **P** (czas wielomianowy), **NP** (weryfikacja wielomianowa), **PSPACE** (pamięć wielomianowa), **EXPTIME**, **L/NL** (logarytmiczna pamięć). Zależności: P ⊆ NP ⊆ PSPACE ⊆ EXPTIME. *Na teście:* znaj inkluzje; NP ⊆ PSPACE; wiadomo, że P ⊊ EXPTIME.

**Maszyna Turinga.** Abstrakcyjny model obliczeń: nieskończona taśma, głowica (czyta/pisze/przesuwa), zbiór stanów, funkcja przejścia. Podstawa **tezy Churcha-Turinga** (definicja obliczalności). Warianty: deterministyczna, niedeterministyczna, wielotaśmowa (równoważne co do mocy). *Na teście:* MT = model obliczalności; niedeterministyczna nie jest silniejsza (rozpoznaje te same języki), tylko potencjalnie szybsza.

**Dowodzenie przynależności do klasy złożoności.** Przynależność (membership): wskaż algorytm o danym zasobie. Trudność (hardness): **redukcja wielomianowa** znanego trudnego problemu do badanego. **Zupełność** = przynależność + trudność (np. NP-zupełność przez redukcję z SAT). *Na teście:* NP-zupełność dowodzi się redukcją z problemu już NP-zupełnego + pokazaniem, że problem jest w NP.

**PSPACE a gry dwuosobowe z pełną informacją.** Problem ustalenia zwycięzcy w wielu grach dwuosobowych o pełnej informacji (uogólnione szachy, go, geografia) jest **PSPACE-zupełny** — odpowiada kwantyfikowanym formułom logicznym (QBF: „istnieje ruch, taki że dla każdego ruchu przeciwnika..."). *Na teście:* naprzemienne kwantyfikatory (∃∀∃...) = istota PSPACE; QBF jest PSPACE-zupełny.

---

## 18. Teoria współbieżności

**Algebra CSP (Communicating Sequential Processes).** Formalizm Hoare'a opisujący procesy współbieżne komunikujące się przez **synchroniczne kanały** (rendez-vous — nadawca i odbiorca czekają na siebie). Operatory: prefiks, wybór, komunikacja, kompozycja równoległa. Podstawa m.in. kanałów w Go/occam. *Na teście:* CSP = komunikacja przez synchroniczne kanały (spotkanie), brak dzielonej pamięci.

**Sieci Petriego.** Graf dwudzielny: **miejsca** (warunki, przechowują żetony) i **tranzycje** (zdarzenia). Tranzycja jest **aktywna (odpala)**, gdy miejsca wejściowe mają dość żetonów; odpalenie przesuwa żetony. Opis macierzowy: macierze **wejść, wyjść i incydencji** (C = wyjścia − wejścia), równanie stanu. Modeluje współbieżność, synchronizację, konflikty, zakleszczenia. *Na teście:* macierz incydencji = wyjścia − wejścia; znakowanie (marking) = rozmieszczenie żetonów.

**Relacja Lamporta (happened-before).** Częściowy porządek „→": (1) zdarzenia w jednym procesie są uporządkowane; (2) wysłanie → odebranie tego samego komunikatu; (3) przechodniość. Zdarzenia nieporównywalne = **współbieżne**. Podstawa zegarów logicznych. *Na teście:* happened-before to porządek częściowy (nie każde dwa zdarzenia są porównywalne); brak relacji = współbieżność.

**Wykonanie współbieżne a równoległe.** **Współbieżność (concurrency)** — zarządzanie wieloma zadaniami w tym samym okresie (mogą przeplatać się na jednym rdzeniu — kwestia struktury). **Równoległość (parallelism)** — faktyczne jednoczesne wykonanie na wielu jednostkach (wymaga wielu rdzeni — kwestia wykonania). *Na teście:* współbieżność ≠ równoległość; można być współbieżnym na jednym rdzeniu, równoległość wymaga wielu jednostek.
