from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class"""
    silver_taxi = SilverServiceTaxi("silverbox 1", 100, 4)
    silver_taxi.drive(30)
    print(silver_taxi)
    print(silver_taxi.get_fare())


main()
