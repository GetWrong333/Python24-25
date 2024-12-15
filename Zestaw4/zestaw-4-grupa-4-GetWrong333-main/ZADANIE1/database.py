import sqlite3
import pandas as pd


def create_table(max_repeats, databasefile="flights.db"):
    """
    Tworzy tabelę 'airport_atl' w bazie SQLite. Jeśli max_repeats > 0,
    usuwa istniejącą tabelę i tworzy nową.
    """
    # Połączenie z bazą danych
    connection = sqlite3.connect(databasefile)
    cursor = connection.cursor()

    if max_repeats > 0:
        # Usuń tabelę, jeśli istnieje
        cursor.execute('''DROP TABLE IF EXISTS airport_atl''')
        print("Tabela 'airport_atl' została usunięta.")

    # Tworzenie nowej tabeli
    cursor.execute('''CREATE TABLE IF NOT EXISTS airport_atl (
        icao24 TEXT,
        callsign TEXT,
        origin_country TEXT,
        time_position INTEGER,
        last_contact INTEGER,
        long REAL,
        lat REAL,
        baro_altitude REAL,
        on_ground TEXT,
        velocity REAL,
        true_track REAL,
        vertical_rate REAL,
        sensors TEXT,
        geo_altitude REAL,
        squawk TEXT,
        spi TEXT,
        position_source INTEGER
    )''')
    print("Tabela 'airport_atl' została utworzona.")

    # Zamknij połączenie
    connection.commit()
    connection.close()


def save_to_db(flight_df, databasefile="flights.db"):
    """
    Zapisuje dane z obiektu DataFrame do bazy SQLite.
    """
    connection = sqlite3.connect(databasefile)
    flight_df.to_sql("airport_atl", connection, if_exists="append", index=False)
    connection.close()
    print("Dane zostały zapisane do bazy danych.")


def load_flight_data(databasefile="flights.db"):
    """
    Wczytuje dane z bazy SQLite do obiektu DataFrame.
    """
    connection = sqlite3.connect(databasefile)
    flight_df = pd.read_sql_query("SELECT * FROM airport_atl", connection)
    connection.close()
    return flight_df
