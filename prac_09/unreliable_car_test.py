from prac_09.unreliable_car import UnreliableCar


def main():
    """Test unreliable_Car class"""
    my_unreliable_car = UnreliableCar("Shitbox 1", 100, 30)
    print(my_unreliable_car)
    print(f"{my_unreliable_car.name} drove {my_unreliable_car.drive(50):2}km")


main()
