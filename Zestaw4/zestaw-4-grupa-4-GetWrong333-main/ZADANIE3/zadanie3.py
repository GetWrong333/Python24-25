from functools import singledispatch, singledispatchmethod

# Singledispatch: globalna funkcja do logowania zdarzeń
@singledispatch
def log_event(event):
    raise NotImplementedError(f"Brak implementacji dla typu: {type(event)}")


@log_event.register
def _(event: str):
    print(f"[LOG - STRING] Zdarzenie tekstowe: {event}")


@log_event.register
def _(event: int):
    print(f"[LOG - INT] Kod zdarzenia: {event}")


@log_event.register
def _(event: dict):
    print("[LOG - DICTIONARY] Szczegóły zdarzenia:")
    for key, value in event.items():
        print(f"  {key}: {value}")


class EventHandler:
    def __init__(self):
        self.event_count = 0  # Licznik obsłużonych zdarzeń

    @singledispatchmethod
    def handle_event(self, event):
        """Domyślna obsługa zdarzeń"""
        raise NotImplementedError(f"Nieobsługiwany typ zdarzenia: {type(event)}")

    @handle_event.register
    def _(self, event: str):
        self.event_count += 1
        print(f"[HANDLER - STRING] Zdarzenie: {event} | Obsłużono zdarzeń: {self.event_count}")

    @handle_event.register
    def _(self, event: int):
        self.event_count += 1
        print(f"[HANDLER - INT] Kod zdarzenia: {event} | Obsłużono zdarzeń: {self.event_count}")

    @handle_event.register
    def _(self, event: list):
        self.event_count += 1  # Liczymy listę jako jedno zdarzenie
        print(f"[HANDLER - LIST] Lista zdarzeń: {event} | Łączna liczba obsłużonych zdarzeń: {self.event_count}")


class DerivedHandler(EventHandler):

    @EventHandler.handle_event.register
    def _(self, event: int):
        self.event_count += 1
        print(f"[DERIVED HANDLER - INT] Nowa obsługa liczby całkowitej: {event} | Obsłużono zdarzeń: {self.event_count}")

    @EventHandler.handle_event.register
    def _(self, event: float):
        self.event_count += 1
        print(f"[DERIVED HANDLER - FLOAT] Zdarzenie typu float: {event} | Obsłużono zdarzeń: {self.event_count}")


if __name__ == "__main__":
    print("=== Globalne logowanie zdarzeń ===")
    log_event("Uruchomienie systemu")
    log_event(404)
    log_event({"typ": "error", "opis": "Nieznany błąd"})

    print("\n=== Klasa EventHandler ===")
    handler = EventHandler()
    handler.handle_event("Zdarzenie logowania")
    handler.handle_event(123)
    handler.handle_event(["zdarzenie1", "zdarzenie2", "zdarzenie3"])

    print("\n=== Obsługa nieobsługiwanego typu ===")
    try:
        log_event(3.14)
    except NotImplementedError as e:
        print(e)

    try:
        handler.handle_event(set([1, 2, 3]))
    except NotImplementedError as e:
        print(e)

    print("\n=== Klasa DerivedHandler ===")
    derived_handler = DerivedHandler()
    derived_handler.handle_event("Inne zdarzenie tekstowe")
    derived_handler.handle_event(789)
    derived_handler.handle_event(3.14)

    print("\n=== Dziedziczenie: instancja EventHandler ===")
    handler.handle_event(12356789)

    print("\n=== Dziedziczenie: instancja DerivedHandler ===")
    derived_handler.handle_event(12356789)
