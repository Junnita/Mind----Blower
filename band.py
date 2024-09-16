import sqlite3


class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    def __db__(self):               #the __db__(self) method provides a convenient way to obtain a database connection within the 
                                            #Band class, encapsulating the database connection logic and making it reusable in other methods.
        return sqlite3.connect('band.db')

    def create_tables(self):
        with self.__db__() as conn:
            cursor = conn.cursor()     #It executes SQL statements and fetches  info from database 
            cursor.execute('''          # it is the placeholder of the actual SQL query you want to execute 
                CREATE TABLE IF NOT EXISTS concerts (
                    id INTEGER PRIMARY KEY,
                    band_name TEXT,
                    venue TEXT,
                    date TEXT
                )
            ''')

    def play_in_venue(self, venue, date):
        with self.__db__() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO concerts (band_name, venue, date) VALUES (?, ?, ?)
            ''', (self.name, venue, date))

    def concerts(self):
        with self.__db__() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM concerts WHERE band_name = ?
            ''', (self.name,))
            return cursor.fetchall()

    def venues(self):
        with self.__db__() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT DISTINCT venue FROM concerts WHERE band_name = ?
            ''', (self.name,))
            return [row[0] for row in cursor.fetchall()]

    def all_introductions(self):
        return [f"Hello {venue}!!!!! We are {self.name} and we're from {self.hometown}" for venue in self.venues()]

    @staticmethod
    def most_performances():
        with sqlite3.connect('band.db') as conn: # This part is a context manager. It creates a new connection to the SQLite database named "band.db" and assigns it to the variable 
            cursor = conn.cursor()
            cursor.execute('''
                SELECT band_name, COUNT(*) as concert_count FROM concerts GROUP BY band_name ORDER BY concert_count DESC LIMIT 1
            ''')
            result = cursor.fetchone()     #This line calls the fetchone() method on the cursor object. 
            return result[0] if result else None   #This is a conditional expression that checks if the result is not None. If it's not, it returns the first element of the
                                                     #result tuple. Otherwise, it returns None.


# Create tables (uncomment if needed)
# Band.create_tables()  # Run once to create tables

# Test cases
band1 = Band("The Rockers", "New York")
band2 = Band("Jazz Masters", "Chicago")

band1.play_in_venue("Madison Square Garden", "2023-09-14")
band1.play_in_venue("Central Park", "2023-09-15")
band2.play_in_venue("Chicago Theatre", "2023-09-14")

print("Band 1 Concerts:", band1.concerts())
print("Band 1 Venues:", band1.venues())
print("Band 1 Introductions:", band1.all_introductions())
print("Band with Most Performances:", Band.most_performances())