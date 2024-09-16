class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

class Venue:  # Capitalize Venue for consistency
    def __init__(self, city):
        self.city = city

class Concert:
    def __init__(self, band, venue):
        self.band = band
        self.venue = venue

    def band(self):
        return self.band

    def venue(self):
        return self.venue  # Return the Venue object directly

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"  


# Test cases
print("**Test 1: Band playing in a different city**")
metallica = Band("Metallica", "Los Angeles")
madison_square_garden = Venue("New York City")
concert1 = Concert(metallica, madison_square_garden)

print(concert1.band.name)  # Access the name attribute of the Band object
print(concert1.venue.city)  # Access the city attribute of the returned Venue object
print(concert1.hometown_show())  # Output: False
print(concert1.introduction())  # Output: Hello New York City!!!!! We are Metallica and we're from Los Angeles
