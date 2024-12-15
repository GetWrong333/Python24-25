import schedule
import time
from ZADANIE1.database import create_table
from ZADANIE1.flight_data import fetch_flight_data, plot_flight_data


def main(interval, max_repeats):
    create_table(max_repeats)

    # Licznik iteracji
    counter = 0

    def job_wrapper():
        nonlocal counter
        if counter < max_repeats:
            fetch_flight_data()
            counter += 1
        else:
            print("Wszystkie zadania zostały wykonane. Kończę harmonogram.")
            return schedule.CancelJob

    # Ustawianie harmonogramu
    schedule.every(interval).seconds.do(job_wrapper)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    FETCH_INTERVAL = 60  # Interwał pobierania w sekundach
    MAX_REPEATS = 10     # Maksymalna liczba powtórzeń
    main(FETCH_INTERVAL, MAX_REPEATS)
    plot_flight_data()
