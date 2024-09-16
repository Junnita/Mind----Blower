import sqlite3

class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    @staticmethod
    def concerts(venue_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM concerts WHERE venue_id = ?
        ''', (venue_id,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts

    @staticmethod
    def bands(venue_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT DISTINCT bands.* FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?
        ''', (venue_id,))
        bands = cursor.fetchall()
        conn.close()
        return bands

    @staticmethod
    def concert_on(venue_id, date):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM concerts WHERE venue_id = ? AND date = ?
        ''', (venue_id, date))
        concert = cursor.fetchone()
        conn.close()
        return concert

    @staticmethod
    def most_frequent_band(venue_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT bands.*, COUNT(concerts.id) as concert_count FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY concert_count DESC
        LIMIT 1
        ''', (venue_id,))
        band = cursor.fetchone()
        conn.close()
        return band

# Test cases
def venue_methods():
    venue_id = 1  # Example venue ID
    date = '2024-09-14'  # Example date

    print("Concerts at venue:", Venue.concerts(venue_id))
    print("Bands at venue:", Venue.bands(venue_id))
    print("Concert on specific date:", Venue.concert_on(venue_id, date))
    print("Most frequent band at venue:", Venue.most_frequent_band(venue_id))

# Run test cases
venue_methods()
