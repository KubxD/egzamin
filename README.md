# 🧮 Egzamin – Program do wypisywania liczb pierwszych

Projekt konsolowy napisany w języku **Python**, którego zadaniem jest wypisanie wszystkich liczb pierwszych z przedziału **2–100**.  
Kod został napisany w sposób czytelny i zorganizowany, z wykorzystaniem funkcji do modularnego podejścia.

---

## 📂 Struktura projektu
egzamin/
├── inf04jp/
│ └── (plik pomocniczy, jeśli dotyczy)
├── egzamin.py
└── README.md


---

## ⚙️ Opis działania

Program wykonuje trzy główne kroki:

1. **Tworzy tablicę** z liczbami z zakresu 2–100.  
2. **Sprawdza każdą liczbę**, czy jest liczbą pierwszą (dzieli się tylko przez 1 i samą siebie).  
3. **Wypisuje wynik** w konsoli w formie czytelnej listy liczb pierwszych.

---

## 💻 Uruchamianie programu

Aby uruchomić projekt lokalnie:

```bash
# 1. Sklonuj repozytorium
git clone https://github.com/KubxD/egzamin.git

# 2. Przejdź do katalogu projektu
cd egzamin

# 3. Uruchom program
python egzamin.py

🧠 Główne funkcje
def wypelnij_tablice(tablica):
    """Wypełnia listę liczbami z przedziału 2–100."""

def czy_liczba_pierwsza(liczba):
    """Sprawdza, czy liczba jest pierwsza."""

def main():
    """Główna funkcja programu."""



🧩 Technologie

Język: Python 3.x

IDE: Dowolne środowisko obsługujące Python (VS Code, PyCharm, Thonny, itp.)

System operacyjny: Windows / Linux / macOS

🔍 Przykładowe rozszerzenia projektu

Jeśli chcesz rozbudować ten projekt, możesz dodać:

Możliwość wprowadzenia zakresu liczb przez użytkownika,

Zapis wyników do pliku tekstowego,

Interfejs graficzny (np. przy użyciu tkinter),

Testy jednostkowe dla funkcji sprawdzającej liczby pierwsze.

👨‍💻 Autor

KubxD
Projekt stworzony w celach edukacyjnych — egzamin INF.04
📅 Rok: 2025
