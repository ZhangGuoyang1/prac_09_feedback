class Band:
    """Band class to represent a band that has multiple musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make each musician in the band play their instrument."""
        for musician in self.musicians:
            musician.play()

    def __str__(self):
        """Return a string representation of the Band."""
        musician_strings = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"
