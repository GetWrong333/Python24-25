import pandas as pd
import matplotlib.pyplot as plt
import requests
from ZADANIE1.database import save_to_db, load_flight_data


def fetch_flight_data(databasefile="flights.db"):
    """
    Pobiera dane z OpenSky Network API i zapisuje je do bazy danych SQLite.
    """
    # Współrzędne ATL (Atlanta Airport)
    lon_min, lat_min = -85.4277, 32.6407
    lon_max, lat_max = -83.4277, 34.6407

    # Logowanie do API (wprowadź własne dane!)
    user_name = "twojlogin"  # Wstaw swoją nazwę użytkownika
    password = "twojehaslo"  # Wstaw swoje hasło

    # Budowanie URL
    url_data = (
        f"https://{user_name}:{password}@opensky-network.org/api/states/all?"
        f"lamin={lat_min}&lomin={lon_min}&lamax={lat_max}&lomax={lon_max}"
    )

    try:
        # Pobieranie danych z API
        response = requests.get(url_data)
        response.raise_for_status()
        data = response.json()

        # Lista kolumn danych
        col_name = [
            'icao24', 'callsign', 'origin_country', 'time_position', 'last_contact',
            'long', 'lat', 'baro_altitude', 'on_ground', 'velocity',
            'true_track', 'vertical_rate', 'sensors', 'geo_altitude',
            'squawk', 'spi', 'position_source'
        ]

        # Przekształcanie danych do DataFrame
        flight_df = pd.DataFrame(data['states'], columns=col_name)
        flight_df = flight_df.dropna(subset=['velocity', 'geo_altitude'])

        # Zapis danych do bazy SQLite
        save_to_db(flight_df, databasefile)
        print("Dane zostały pobrane i zapisane do bazy danych.")

    except Exception as e:
        print(f"Błąd podczas pobierania danych: {e}")


def plot_flight_data(databasefile="flights.db", show_plot=True):
    """
    Tworzy wykres wysokości samolotu względem jego prędkości.
    """
    flight_df = load_flight_data(databasefile)

    # Czyszczenie i przetwarzanie danych
    flight_df = flight_df.dropna(subset=['velocity', 'geo_altitude'])
    flight_df['velocity_kmh'] = flight_df['velocity'] * 3.6  # Konwersja prędkości na km/h
    flight_df['geo_altitude_km'] = flight_df['geo_altitude'] / 1000  # Konwersja wysokości na km

    # Usunięcie duplikatów dla samolotów (największa prędkość)
    flight_df = flight_df.sort_values(by='velocity', ascending=False).drop_duplicates(subset='icao24')

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))
    plt.scatter(flight_df['velocity_kmh'], flight_df['geo_altitude_km'], alpha=0.7, color='blue', s=10, marker='o')
    plt.title('Zależność wysokości od prędkości lotu', fontsize=14)
    plt.xlabel('Prędkość (km/h)', fontsize=12)
    plt.ylabel('Wysokość (km)', fontsize=12)
    plt.xlim(0, 1200)
    plt.ylim(0, 14)
    plt.grid(True)
    plt.tight_layout()

    if show_plot:
        plt.show()
    print("Wykres został wygenerowany.")
