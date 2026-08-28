# -*- coding: utf-8 -*-
import csv

# (Dzial, Pytanie, Odpowiedz)
cards = [
# 1. UNIX
("UNIX","Co to jest PAM i jakie ma 4 typy modulow?","Pluggable Authentication Modules - modularne uwierzytelnianie oddzielajace aplikacje od metody. Typy: auth, account, password, session. Flagi: required, requisite, sufficient, optional."),
("UNIX","Co przechowuje i-wezel (inode), a czego NIE?","Metadane pliku: wlasciciel, prawa, rozmiar, wskazniki na bloki. NIE przechowuje nazwy pliku - nazwa jest w katalogu (para nazwa->numer inode)."),
("UNIX","Roznica: hard link vs symlink?","Hard link = kolejna nazwa tego samego inode, nie dziala miedzy systemami plikow. Symlink = plik ze sciezka, moze wskazywac gdziekolwiek."),
("UNIX","Czym jest ACL w systemach plikow?","Access Control List - rozszerzenie praw rwx pozwalajace nadac uprawnienia konkretnym uzytkownikom/grupom. Polecenia getfacl/setfacl, jest maska."),
("UNIX","Quota: roznica soft vs hard limit?","Soft = mozna przekroczyc na czas karencji (grace period). Hard = nieprzekraczalny. Quota liczy bloki (przestrzen) i i-wezly (liczba plikow)."),
("UNIX","Co to context switch i syscall?","Syscall = przejscie z trybu uzytkownika do jadra po uslugi. Context switch = zapis/odtworzenie stanu procesu (rejestry, PC, stos) przy zmianie procesu; ma koszt."),
("UNIX","Priorytet procesu - wartosc nice?","Nice od -20 (najwyzszy priorytet) do +19 (najnizszy). Nizsza wartosc = wyzszy priorytet. Zwykly user moze tylko obnizac priorytet (zwiekszac nice)."),
("UNIX","Ktory mechanizm IPC jest najszybszy i dlaczego?","Pamiec dzielona (shared memory) - brak kopiowania danych, ale wymaga wlasnej synchronizacji (semafory)."),
("UNIX","Co to LDAP?","Lightweight Directory Access Protocol - dostep do hierarchicznej uslugi katalogowej (drzewo DIT, wpisy z DN). Zoptymalizowany pod odczyt. Scentralizowane uwierzytelnianie."),
("UNIX","Na czym opiera sie Kerberos?","Klucze symetryczne + zaufany KDC (AS+TGS). Uzytkownik dostaje bilety (TGT), haslo nie idzie przez siec. Wymaga zsynchronizowanych zegarow. Uzycie: SSO, Active Directory."),
# 2. Wstep do informatyki
("Wstep","Co oznaczaja {} i [] w EBNF?","{} = powtorzenie 0 lub wiecej razy, [] = opcjonalnosc, () = grupowanie, | = alternatywa."),
("Wstep","Trzy aspekty jezyka programowania?","Skladnia (forma), semantyka (znaczenie), pragmatyka (sposob/cel uzycia). Poprawny skladniowo program moze byc bezsensowny semantycznie."),
("Wstep","Cel procedur i funkcji?","Modularnosc, reuzywalnosc (DRY), abstrakcja, czytelnosc, latwiejsze testowanie - nie 'przyspieszenie'."),
("Wstep","Jak koduje UTF-8?","Zmienna dlugosc 1-4 bajty. ASCII (0-127) = 1 bajt (kompatybilnosc). Bajt kontynuacji zaczyna sie od 10xxxxxx, bajt wiodacy od 110/1110/11110."),
("Wstep","By value vs by reference?","By value = kopia argumentu, zmiany lokalne (oryginal bez zmian). By reference/wskaznik = dostep do oryginalu, zmiany widoczne na zewnatrz."),
("Wstep","Czym jest funkcja lambda w Pythonie?","Anonimowa funkcja jednowyrazeniowa: lambda x: x+1. Zwraca wartosc wyrazenia bez return. Uzycie: map, filter, sorted(key=...)."),
("Wstep","Co jest niezbedne w rekurencji?","Warunek bazowy (stop) i krok zblizajacy do bazy. Brak bazy = nieskonczona rekurencja / stack overflow."),
("Wstep","Trzy sposoby przydzialu pamieci zmiennych?","Statyczny (caly czas zycia programu), automatyczny/stos (lokalne, szybki), dynamiczny/sterta (malloc/new, reczne zwalnianie, ryzyko wyciekow)."),
("Wstep","Kodowanie U2 - jak uzyskac liczbe ujemna i zakres?","Neguj bity i dodaj 1. Najstarszy bit ma wage ujemna. Zakres n bitow: od -2^(n-1) do 2^(n-1)-1. Jedno zero, o jedna liczba ujemna wiecej."),
("Wstep","Co to RPN i jak sie oblicza?","Odwrotna notacja polska (postfix): operator po operandach (3 4 +). Bez nawiasow, obliczana stosem."),
("Wstep","Kompilacja vs interpretacja?","Kompilacja = tlumaczenie calosci na kod maszynowy przed wykonaniem, wykrywa bledy wczesniej, szybkie wykonanie. Interpretacja = instrukcja po instrukcji w trakcie, bez pliku wykonywalnego."),
("Wstep","Co znacza O, Omega, Theta?","O = ograniczenie gorne, Omega = dolne, Theta = dokladne (asymptotyczne). Pomijamy stale i skladniki nizszego rzedu."),
("Wstep","Co to problem nierozstrzygalny?","Brak algorytmu dajacego zawsze poprawna odpowiedz w skonczonym czasie (np. problem stopu). To NIE to samo co 'trudny obliczeniowo'."),
("Wstep","Model von Neumanna - bloki?","ALU, jednostka sterujaca (CU), pamiec (WSPOLNA dla programu i danych), I/O, magistrala. Harvard = rozdzielona pamiec."),
# 3. Algorytmy
("Algorytmy","Dolna granica sortowan porownaniowych?","Omega(n log n). Zadne sortowanie porownaniowe nie zejdzie ponizej. Counting/radix moga O(n) przy zalozeniach o kluczach."),
("Algorytmy","Zlozonosc quicksort?","Srednio O(n log n), pesymistycznie O(n^2), w miejscu, niestabilne."),
("Algorytmy","Kiedy Dijkstra nie dziala i co uzyc?","Nie dziala dla ujemnych wag. Wtedy Bellman-Ford (O(VE), wykrywa ujemne cykle). Floyd-Warshall = wszystkie pary O(V^3)."),
("Algorytmy","Kiedy algorytm zachlanny daje optimum?","Gdy jest wlasnosc wyboru zachlannego i optymalna podstruktura (Kruskal, Dijkstra, Huffman). Nie dziala np. dla plecaka 0/1."),
("Algorytmy","Macierz vs lista sasiedztwa?","Macierz: O(V^2) pamieci, sprawdzenie krawedzi O(1), dla gestych. Lista: O(V+E) pamieci, dla rzadkich, szybka iteracja po sasiadach."),
("Algorytmy","Twierdzenie o maksymalnym przeplywie?","Max-flow = min-cut: maksymalny przeplyw = przepustowosc minimalnego przekroju. Algorytmy: Ford-Fulkerson, Edmonds-Karp O(VE^2)."),
("Algorytmy","Kiedy stosowac programowanie dynamiczne?","Gdy sa nakladajace sie podproblemy + optymalna podstruktura. Zapamietywanie (memoizacja/tablica) zmienia koszt wykladniczy na wielomianowy."),
# 4. Programowanie imperatywne
("C","Etapy budowy programu z kodu C?","Preprocesor -> kompilator -> asembler -> linker (konsolidacja). Blad 'undefined reference' = etap linkowania."),
("C","Jak przekazac tablice 2D do funkcji w C?","Trzeba podac rozmiar drugiego (i dalszych) wymiaru: void f(int a[][N]). Pierwszy wymiar mozna pominac (decay do wskaznika)."),
("C","Co to VLA?","Variable Length Array - tablica o rozmiarze ustalanym w runtime, alokowana na stosie (C99). Ryzyko przepelnienia stosu."),
("C","Od czego zalezy sizeof struktury w C?","Od wyrownania (padding/alignment) i kolejnosci pol. sizeof >= suma pol, nie zawsze rowna sumie."),
("C","Co robi qsort()?","Uniwersalne sortowanie: qsort(baza, liczba, rozmiar_elem, komparator). Komparator zwraca <0/0/>0. Srednio O(n log n), niestabilne."),
# 5. Funkcyjne i obiektowe
("Funkcyjne","Co to funkcja wyzszego rzedu?","Funkcja przyjmujaca inna funkcje jako argument i/lub zwracajaca funkcje. Przyklady: map, filter, reduce, kompozycja."),
("Funkcyjne","Typ algebraiczny - suma vs iloczyn?","Suma (wariant/union) = 'albo A albo B' (Maybe, Either). Iloczyn (rekord/krotka) = 'A i B naraz'. Rozroznianie: pattern matching."),
("Funkcyjne","Polimorfizm parametryczny vs ad-hoc?","Parametryczny = generyki (ta sama funkcja dla wszystkich typow). Ad-hoc = przeciazanie / klasy typow (rozne implementacje)."),
("Funkcyjne","Rekursja ogonowa - co szczegolnego?","Wywolanie rekurencyjne to ostatnia operacja; moze byc zoptymalizowane (TCO) do petli - stala pamiec stosu."),
("Funkcyjne","Co to leniwe obliczanie?","Call-by-need: wartosc liczona dopiero gdy potrzebna, z zapamietaniem. Umozliwia nieskonczone struktury (strumienie)."),
("Funkcyjne","Cztery cechy jezykow obiektowych?","Abstrakcja, hermetyzacja (enkapsulacja), dziedziczenie, polimorfizm."),
# 6. Bazy danych
("BD","Co oznacza ACID?","Atomicity (wszystko albo nic), Consistency (spojnosc), Isolation (izolacja wspolbieznych), Durability (trwalosc po awarii)."),
("BD","Zwiazek M:N w modelu relacyjnym?","Wymaga tabeli laczacej (posredniej) z dwoma kluczami obcymi."),
("BD","Klucz glowny vs obcy?","Glowny (primary): unikalny, NOT NULL, identyfikuje krotke. Obcy (foreign): odwolanie do klucza w innej tabeli, integralnosc referencyjna."),
("BD","Selekcja vs projekcja w algebrze relacji?","Selekcja (sigma) = wybor WIERSZY wg warunku. Projekcja (pi) = wybor KOLUMN. Join laczy relacje po warunku."),
("BD","Co usuwa 2NF, a co 3NF?","2NF = usuwa zaleznosci czesciowe od klucza. 3NF = usuwa zaleznosci przechodnie (nieklucz od nieklucza). 1NF = wartosci atomowe."),
("BD","Czy widok przechowuje dane?","Zwykly widok - nie (wirtualna tabela z zapytania). Materializowany - tak. Uzycie: uproszczenie, bezpieczenstwo."),
("BD","Wplyw indeksu na operacje?","Przyspiesza SELECT, spowalnia INSERT/UPDATE/DELETE (aktualizacja indeksu). B-drzewo = zakresy, hasz = rownosc."),
# 7. Technika cyfrowa
("Cyfrowa","Co to bramka trojstanowa?","Ma stany 0, 1 oraz Z (wysoka impedancja - odlaczenie). Stan Z pozwala podlaczyc wiele wyjsc do wspolnej magistrali."),
("Cyfrowa","Zasada tablic Karnaugha?","Minimalizacja funkcji logicznych. Sasiednie komorki roznia sie 1 bitem (kod Graya). Grupy jedynek = potegi 2, owijaja sie na brzegach."),
("Cyfrowa","Uklad synchroniczny vs asynchroniczny?","Synchroniczny = wspolny zegar (przewidywalny). Asynchroniczny = reaguje natychmiast bez zegara (szybszy, ryzyko hazardow)."),
("Cyfrowa","MUX - ile wejsc dla n linii adresowych?","2^n wejsc na 1 wyjscie. MUX = przelacznik, moze realizowac dowolna funkcje logiczna. DEMUX robi odwrotnie."),
("Cyfrowa","Co to hazard w technice cyfrowej?","Chwilowy niepozadany stan na wyjsciu przez rozne opoznienia propagacji sciezek. Statyczny/dynamiczny. Grozny w ukladach asynchronicznych."),
("Cyfrowa","Half adder vs full adder?","Polsumator: dodaje 2 bity (suma+carry), BEZ wejscia carry. Sumator pelny: dodaje 3 bity (w tym carry-in), daje sume i carry-out."),
("Cyfrowa","Rodzaje przerzutnikow?","SR (stan zabroniony), D (zatrzask danych), JK (uniwersalny, bez stanu zabronionego, toggle dla J=K=1), T (toggle - liczniki)."),
("Cyfrowa","Automat Moore vs Mealy?","Moore = wyjscie zalezy tylko od stanu. Mealy = wyjscie od stanu I wejscia (mniej stanow, szybsza reakcja)."),
("Cyfrowa","Uklad kombinacyjny vs sekwencyjny?","Kombinacyjny = wyjscie tylko od biezacych wejsc, bez pamieci (bramki, MUX, sumatory). Sekwencyjny = od wejsc i stanu, ma pamiec (przerzutniki, liczniki, automaty)."),
# 8. Technika mikroprocesorowa
("Mikro","Co robi DMA?","Direct Memory Access - kontroler przenosi dane pamiec<->I/O BEZ udzialu CPU. Odciaza procesor, kradnie cykle magistrali, zglasza przerwanie po zakonczeniu."),
("Mikro","SRAM vs DRAM?","SRAM = przerzutnik, szybka, droga, bez odswiezania (cache). DRAM = kondensator, tania, gesta, WYMAGA odswiezania, wolniejsza (pamiec glowna)."),
("Mikro","Cechy pamieci Flash?","Nieulotna, elektrycznie kasowalna BLOKAMI (odmiana EEPROM). NOR (kod) / NAND (dane, SSD). Ograniczona liczba cykli zapisu."),
("Mikro","RISC vs CISC?","RISC = malo prostych rozkazow stalej dlugosci, ~1 cykl, duzo rejestrow, load/store (ARM). CISC = zlozone rozkazy zmiennej dlugosci, operacje pamiec-pamiec (x86)."),
("Mikro","Co daje pipelining?","Nakladanie faz rozkazow - zwieksza przepustowosc (nie skraca czasu 1 rozkazu). Hazardy: strukturalne, danych, sterowania (skoki)."),
("Mikro","Co robi volatile w C/C++?","Mowi kompilatorowi ze zmienna moze zmienic sie z zewnatrz (przerwanie, sprzet, inny watek) - zakaz optymalizacji dostepow. NIE zapewnia atomowosci."),
# 9. Architektura
("Architektura","Dzieki czemu dziala cache?","Lokalnosc czasowa i przestrzenna odwolan. Male szybkie L1/L2/L3 miedzy CPU a RAM. Miss = siegniecie do wolniejszej pamieci."),
("Architektura","Prawo Amdahla vs Gustafsona?","Amdahl = staly rozmiar problemu, przyspieszenie ograniczone czescia sekwencyjna (pesymistyczne). Gustafson = rosnacy problem, skalowanie liniowe (optymistyczne)."),
("Architektura","HPL/LINPACK vs HPCG?","LINPACK (HPL) = geste macierze, szczytowe FLOPS, TOP500 (compute-bound). HPCG = rzadkie macierze, obciaza pamiec (memory-bound), realistyczniejszy, nizszy wynik."),
("Architektura","Taksonomia Flynna?","SISD (jednoprocesor), SIMD (wektory, GPU), MISD (rzadki), MIMD (wieloprocesory, klastry)."),
# 10. Inzynieria oprogramowania
("IO","Wady modelu kaskadowego?","Sztywnosc, pozne wykrycie bledow, kosztowne zmiany, klient widzi efekt na koncu. Zalety: prostota, dokumentacja, jasne kamienie milowe."),
("IO","Cztery wartosci Agile Manifesto?","Ludzie/interakcje > procesy; dzialajace oprogramowanie > dokumentacja; wspolpraca z klientem > umowy; reagowanie na zmiany > plan. ('>' = wieksza wartosc, nie 'zamiast')."),
("IO","Poziomy testow?","Jednostkowe (modul) -> integracyjne (wspolpraca) -> systemowe (calosc) -> akceptacyjne (klient/wymagania)."),
("IO","Weryfikacja vs walidacja?","Weryfikacja = 'czy budujemy poprawnie?' (wobec specyfikacji). Walidacja = 'czy budujemy wlasciwy produkt?' (wobec potrzeb uzytkownika)."),
("IO","Wymaganie funkcjonalne vs niefunkcjonalne?","Funkcjonalne = CO robi system (funkcje). Niefunkcjonalne = JAK (jakosc): wydajnosc, bezpieczenstwo, niezawodnosc. Np. 'odpowiedz <1s' = niefunkcjonalne."),
("IO","Scrum vs Kanban?","Scrum = role (PO, SM, Zespol), sprinty, artefakty, zdarzenia. Kanban = ciagly przeplyw, tablica, limity WIP, bez sprintow i wyznaczonych rol."),
("IO","Diagramy UML - strukturalne vs behawioralne?","Strukturalne: klas, obiektow, komponentow, wdrozenia. Behawioralne: przypadkow uzycia, sekwencji, aktywnosci, stanow."),
# 11. Metody obliczeniowe
("Numeryka","Cechy arytmetyki zmiennoprzecinkowej IEEE 754?","Skonczona precyzja, bledy zaokraglen, dodawanie NIE jest laczne, utrata cyfr przy odejmowaniu bliskich liczb, wartosci ±inf, NaN."),
("Numeryka","Dokladnosc kwadratury Gaussa?","n-wezlowa jest dokladna dla wielomianow stopnia <= 2n-1. Wezly = pierwiastki wielomianow ortogonalnych. Newton-Cotes = wezly rownoodlegle (Simpson)."),
("Numeryka","Do czego wielomiany ortogonalne?","Aproksymacja, kwadratury Gaussa (wezly = ich pierwiastki). Czebyszew minimalizuje blad maksymalny (ogranicza efekt Rungego)."),
("Numeryka","Metody bezposrednie vs iteracyjne dla ukladow liniowych?","Bezposrednie (Gauss, LU, Cholesky) = skonczona liczba krokow. Iteracyjne (Jacobi, Gauss-Seidel, CG) = dla duzych rzadkich. Zle uwarunkowanie = duze bledy."),
("Numeryka","Newton-Raphson vs bisekcja?","Newton = kwadratowa zbieznosc, wymaga pochodnej i dobrego startu, moze rozbiegac. Bisekcja = zawsze zbiezna w przedziale ze zmiana znaku, ale wolna (liniowa)."),
("Numeryka","Cechy generatora pseudolosowego (PRNG)?","Deterministyczny, okresowy, powtarzalny przy tym samym ziarnie (LCG, Mersenne Twister). To samo ziarno = ta sama sekwencja."),
# 12. Sztuczna inteligencja
("AI","Uczenie nadzorowane vs nienadzorowane?","Nadzorowane = dane etykietowane (klasyfikacja/regresja). Nienadzorowane = bez etykiet (klasteryzacja k-means, PCA)."),
("AI","Po co funkcja aktywacji w sieci?","Wprowadza nieliniowosc (sigmoid, tanh, ReLU). Bez niej siec wielowarstwowa = model liniowy."),
("AI","Jak dziala backpropagation?","Propagacja w przod (blad), potem wstecz - gradient straty wzgledem wag regula lancuchowa, aktualizacja wag (spadek gradientu). Wymaga rozniczkowalnych aktywacji."),
("AI","Do czego RNN i jaki maja problem?","Dla sekwencji (tekst, mowa, szeregi czasowe) - maja stan/pamiec. Problem zanikajacego/eksplodujacego gradientu -> LSTM/GRU z bramkami."),
("AI","Wzor i warunek optymalnosci A*?","f(n)=g(n)+h(n). Optymalny gdy heurystyka dopuszczalna (nie przeszacowuje) i spojna. h=0 -> A* = Dijkstra."),
# 13. Systemy operacyjne
("SO","Cechy SJF i Round Robin?","SJF minimalizuje sredni czas oczekiwania, ale glodzi dlugie zadania. RR = kwant czasu, sprawiedliwy; maly kwant = duzo przelaczen."),
("SO","Proces vs watek?","Proces = wlasna przestrzen adresowa, izolowany, kosztowny. Watek = w obrebie procesu, WSPOLDZIELI pamiec, lekki, wymaga synchronizacji."),
("SO","Stronicowanie vs segmentacja?","Stronicowanie = staly rozmiar stron, fragmentacja WEWNETRZNA. Segmentacja = zmienna dlugosc segmentow, fragmentacja ZEWNETRZNA. Page fault = brak strony."),
("SO","Cechy systemu czasu rzeczywistego?","Kluczowa terminowosc (deadline), nie sama szybkosc. Hard RT = przekroczenie = katastrofa. Soft RT = pogorszenie jakosci. Wymaga determinizmu."),
("SO","Co robi fork() i exec()?","fork() = tworzy kopie procesu (copy-on-write), zwraca 0 dziecku i PID rodzicowi. exec() = podmienia obraz procesu na nowy program. wait() = rodzic czeka."),
("SO","Cztery warunki Coffmana (zakleszczenie)?","Wzajemne wykluczanie, trzymaj i czekaj, brak wywlaszczania, cykliczne oczekiwanie. Zerwanie jednego = brak deadlocka. Bankier = unikanie."),
("SO","Laczenie statyczne vs dynamiczne?","Statyczne = biblioteka wkompilowana (wiekszy plik, samodzielny). Dynamiczne = .so/.dll ladowane w runtime, wspoldzielone (mniejszy plik, latwa aktualizacja)."),
# 14. Sieci
("Sieci","IP vs MAC - kluczowa roznica?","IP = adres logiczny L3, hierarchiczny, routowalny (32 bity IPv4). MAC = adres fizyczny L2, plaski, NIE routowalny, lokalny dla segmentu."),
("Sieci","Struktura adresu MAC?","48 bitow = 6 bajtow (hex). Pierwsze 3 bajty = OUI (producent, IEEE), ostatnie 3 = numer producenta. Broadcast = FF:FF:FF:FF:FF:FF."),
("Sieci","DHCP vs SLAAC?","DHCP = stanowe przydzielanie IP/maski/bramy/DNS (dzierzawa). SLAAC = bezstanowa autokonfiguracja IPv6 z prefiksu ogloszonego przez router."),
("Sieci","TCP vs UDP?","TCP = polaczeniowy, niezawodny (potwierdzenia, retransmisje), kontrola przeplywu/przeciazenia. UDP = bezpolaczeniowy, zawodny, maly narzut, szybki (VoIP, DNS)."),
("Sieci","Jak wezel wybiera trase?","Regula najdluzszego pasujacego prefiksu (longest prefix match) w tablicy routingu. Brak trasy -> brama domyslna."),
("Sieci","Po co VLAN?","Logiczny podzial L2 na odrebne domeny rozgloszeniowe (802.1Q). Segmentacja, bezpieczenstwo, mniej broadcastu. Ruch miedzy VLAN wymaga routingu (L3)."),
("Sieci","OSPF vs RIP vs BGP?","OSPF = link-state (mapa topologii, Dijkstra), IGP. RIP = distance-vector (wymiana tablic z sasiadami), IGP. BGP = miedzy systemami autonomicznymi (EGP)."),
("Sieci","Co robi ARP?","Mapuje znany IPv4 na MAC w sieci lokalnej: broadcast 'kto ma ten IP?', odpowiedz z MAC, buforowanie. W IPv6 zastapione przez NDP."),
("Sieci","Do czego STP (802.1d)?","Zapobiega petlom w przelaczanej sieci L2. Wybiera root bridge (najnizszy Bridge ID), blokuje nadmiarowe lacza, buduje drzewo rozpinajace."),
# 15. Systemy rozproszone
("Rozproszone","Co mowi teoria CAP?","Consistency, Availability, Partition tolerance - nie da sie miec wszystkich 3 naraz. Przy podziale sieci (P) wybieramy C albo A. (W dokumencie blad: nie 'Atomicity' tylko Availability.)"),
("Rozproszone","Zadania middleware?","Ukrywa heterogenicznosc i szczegoly komunikacji, zapewnia przezroczystosc, RPC/RMI, nazewnictwo, synchronizacje, bezpieczenstwo, transakcje."),
("Rozproszone","Cztery cechy systemu reaktywnego?","Responsive, Resilient, Elastic, Message-driven. Fundament = komunikaty; z nich elastycznosc i odpornosc; efekt = responsywnosc."),
("Rozproszone","Regula zegara Lamporta?","Inkrementuj przy zdarzeniu; dolacz znacznik przy wysylaniu; przy odbiorze zegar=max(lokalny, odebrany)+1. a->b => L(a)<L(b) (nie odwrotnie). Nie wykrywa wspolbieznosci."),
("Rozproszone","Podstawowe cechy REST?","Bezstanowosc (kazde zadanie kompletne), zasoby w URI, operacje metodami HTTP (GET/POST/PUT/DELETE), reprezentacje JSON/XML, jednolity interfejs, cache."),
("Rozproszone","Typy przezroczystosci?","Dostepu, polozenia, migracji, replikacji, wspolbieznosci, awarii, skalowania. Przezroczystosc polozenia = user nie zna fizycznej lokalizacji."),
# 16. Automaty i jezyki formalne
("Automaty","Hierarchia Chomsky'ego?","Typ 0 rekurencyjnie przeliczalne (MT), Typ 1 kontekstowe (LBA), Typ 2 bezkontekstowe (automat stosowy), Typ 3 regularne (automat skonczony). Regularne subset bezkontekstowych subset..."),
("Automaty","Postac normalna Chomsky'ego (CNF)?","Produkcje: A->BC (dwa nieterminale) lub A->a (jeden terminal). Podstawa algorytmu CYK O(n^3)."),
("Automaty","Postac normalna Greibach (GNF)?","Produkcje A->a alpha: terminal na poczatku, potem nieterminale. Eliminuje rekurencje lewostronna."),
("Automaty","Kiedy gramatyka jest wieloznaczna?","Gdy istnieje slowo z >=2 drzewami wyprowadzenia. Problem np. 'dangling else'. Ogolnie nierozstrzygalny."),
# 17. Teoria obliczen
("Zlozonosc","Dlaczego problem stopu jest wazny?","Jest nierozstrzygalny (dowod Turinga, przekatniowy). Nie ma ogolnego algorytmu rozstrzygajacego czy program sie zatrzyma."),
("Zlozonosc","Roznica P vs NP?","P = rozwiazywalne w czasie wielomianowym. NP = rozwiazanie da sie zweryfikowac w czasie wielomianowym. NP-zupelne = najtrudniejsze w NP (SAT, Cook-Levin)."),
("Zlozonosc","Rozstrzygalny vs czesciowo rozstrzygalny?","Rozstrzygalny = algorytm zawsze konczy z odpowiedzia TAK/NIE. Czesciowo (rekurencyjnie przeliczalny) = zatrzymuje sie dla TAK, moze nie konczyc dla NIE."),
("Zlozonosc","Inkluzje klas zlozonosci?","P subset NP subset PSPACE subset EXPTIME. Wiadomo ze P != EXPTIME."),
("Zlozonosc","Czym jest maszyna Turinga?","Model obliczen: nieskonczona tasma, glowica, stany, funkcja przejscia. Podstawa tezy Churcha-Turinga. Niedeterministyczna nie jest silniejsza (te same jezyki)."),
("Zlozonosc","Jak dowiesc NP-zupelnosci?","Pokaz ze problem jest w NP (weryfikacja wielomianowa) + redukcja wielomianowa ze znanego NP-zupelnego (np. SAT)."),
("Zlozonosc","Zwiazek PSPACE z grami?","Ustalenie zwyciezcy w grach 2-osobowych z pelna informacja (uogolnione szachy/go) jest PSPACE-zupelne. Odpowiada QBF (naprzemienne kwantyfikatory exists/forall)."),
# 18. Teoria wspolbieznosci
("Wspolbieznosc","Na czym opiera sie CSP?","Communicating Sequential Processes (Hoare): procesy komunikuja sie przez SYNCHRONICZNE kanaly (rendez-vous), bez dzielonej pamieci. Podstawa kanalow w Go/occam."),
("Wspolbieznosc","Co to macierz incydencji w sieci Petri?","C = macierz wyjsc - macierz wejsc. Miejsca (zetony) i tranzycje. Tranzycja odpala gdy miejsca wejsciowe maja dosc zetonow. Znakowanie = rozmieszczenie zetonow."),
("Wspolbieznosc","Relacja happened-before Lamporta?","Porzadek CZESCIOWY: (1) zdarzenia w procesie uporzadkowane, (2) wyslanie->odebranie, (3) przechodniosc. Zdarzenia nieporownywalne = wspolbiezne."),
("Wspolbieznosc","Wspolbieznosc vs rownoleglosc?","Wspolbieznosc = zarzadzanie wieloma zadaniami w tym samym okresie (moze byc 1 rdzen - struktura). Rownoleglosc = faktyczne jednoczesne wykonanie (wymaga wielu jednostek)."),
]

with open("fiszki-egzamin.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for dzial, q, a in cards:
        w.writerow([q, a, dzial])

print(f"Zapisano {len(cards)} fiszek do fiszki-egzamin.csv")
