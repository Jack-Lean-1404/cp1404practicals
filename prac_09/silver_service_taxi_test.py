from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class"""
    silver_taxi = SilverServiceTaxi("silverbox 1", 100, 4)
    silver_taxi.drive(38)
    print(silver_taxi)
    total_fare = silver_taxi.get_fare()
    print(f"${total_fare:.2f}")

main()
