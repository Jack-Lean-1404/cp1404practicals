from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes different costs."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but for a Silver one instead :)."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price of the fare."""
        return self.flagfall + super().get_fare()
