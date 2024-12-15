from abc import ABC, abstractmethod


class Pojazd(ABC):
    def __init__(self, model: str, rok: int):
        self._model = model
        self._rok = rok
        self._predkosc = 0

    @property
    def predkosc(self) -> float:
        """Getter dla prędkości."""
        return self._predkosc

    @predkosc.setter
    def predkosc(self, value: float):
        """Setter dla prędkości z walidacją."""
        if value < 0:
            raise ValueError("Prędkość nie może być ujemna!")  # Poprawa: dodano "!"
        self._predkosc = value

    @predkosc.deleter
    def predkosc(self):
        """Deleter resetujący prędkość."""
        self._predkosc = 0


class Samochod(Pojazd):
    def __init__(self, model: str, rok: int, liczba_drzwi: int):
        super().__init__(model, rok)
        self.liczba_drzwi = liczba_drzwi


class Autobus(Pojazd):
    def __init__(self, model: str, rok: int, liczba_miejsc: int):
        super().__init__(model, rok)
        self.liczba_miejsc = liczba_miejsc


class FabrykaPojazdow(ABC):
    def __init__(self, nazwa: str):
        self._nazwa = nazwa
        self._liczba_wyprodukowanych = 0

    @property
    def nazwa(self) -> str:
        """Getter dla nazwy fabryki."""
        return self._nazwa

    @abstractmethod
    def stworz_pojazd(self, *args, **kwargs) -> Pojazd:
        """Metoda abstrakcyjna do tworzenia pojazdów."""
        pass

    @classmethod
    def utworz_fabryke(cls, typ: str, nazwa: str) -> 'FabrykaPojazdow':
        """Metoda klasowa tworząca odpowiednią fabrykę na podstawie typu."""
        if typ == 'samochod':
            return FabrykaSamochodow(nazwa)
        elif typ == 'autobus':
            return FabrykaAutobusow(nazwa)
        else:
            raise ValueError("Nieznany typ fabryki: '{}'".format(typ))

    @staticmethod
    def sprawdz_rok(rok: int) -> bool:
        """Sprawdza, czy rok produkcji mieści się w przedziale 1900–2024."""
        return 1900 <= rok <= 2024

    def _zwieksz_licznik(self):
        """Zwiększa licznik wyprodukowanych pojazdów."""
        self._liczba_wyprodukowanych += 1

    def ile_wyprodukowano(self) -> int:
        """Zwraca liczbę wyprodukowanych pojazdów."""
        return self._liczba_wyprodukowanych


class FabrykaSamochodow(FabrykaPojazdow):
    def stworz_pojazd(self, model: str, rok: int, liczba_drzwi: int = 4) -> Samochod:
        """Tworzy nowy samochód."""
        if not self.sprawdz_rok(rok):
            raise ValueError("Nieprawidłowy rok produkcji!")  # Poprawa: dodano "!"
        samochod = Samochod(model, rok, liczba_drzwi)
        self._zwieksz_licznik()
        return samochod


class FabrykaAutobusow(FabrykaPojazdow):
    def stworz_pojazd(self, model: str, rok: int, liczba_miejsc: int = 50) -> Autobus:
        """Tworzy nowy autobus."""
        if not self.sprawdz_rok(rok):
            raise ValueError("Nieprawidłowy rok produkcji!")  # Poprawa: dodano "!"
        autobus = Autobus(model, rok, liczba_miejsc)
        self._zwieksz_licznik()
        return autobus


def main():
    # Utworz fabryki pojazdow (samochodow i autobusow)
    fabryka_samochodow = FabrykaPojazdow.utworz_fabryke('samochod', "Fabryka Samochodów Warszawa")
    fabryka_autobusow = FabrykaPojazdow.utworz_fabryke('autobus', "Fabryka Autobusów Kraków")

    # Utworzone fabryki - demonstracja @property nazwa
    print(f"Nazwa fabryki: {fabryka_samochodow.nazwa}")
    print(f"Nazwa fabryki: {fabryka_autobusow.nazwa}")

    # Utworz pojazdy
    samochod = fabryka_samochodow.stworz_pojazd("Fiat", 2023, liczba_drzwi=5)
    autobus = fabryka_autobusow.stworz_pojazd("Solaris", 2023, liczba_miejsc=60)

    # Demonstracja dzialania gettera, settera i deletera
    samochod.predkosc = 50  # uzycie setter
    print(f"Prędkość samochodu: {samochod.predkosc}")  # uzycie getter
    del samochod.predkosc  # uzycie deleter
    print(f"Prędkość po reset: {samochod.predkosc}")

    # Pokazanie ile pojazdow wyprodukowano
    print(f"Wyprodukowano samochodów: {fabryka_samochodow.ile_wyprodukowano()}")
    print(f"Wyprodukowano autobusów: {fabryka_autobusow.ile_wyprodukowano()}")


if __name__ == "__main__":
    main()
