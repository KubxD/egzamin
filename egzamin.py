# Program wypisujący liczby pierwsze z przedziału 2..100

def wypelnij_tablice(tablica):
    for i in range(2, 101):
        tablica.append(i)

def czy_liczba_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True

def main():
    liczby = []
    wypelnij_tablice(liczby)

    liczby_pierwsze = [x for x in liczby if czy_liczba_pierwsza(x)]

    print("Liczby pierwsze w przedziale 2–100:")
    print(", ".join(str(x) for x in liczby_pierwsze))

if __name__ == "__main__":
    main()
