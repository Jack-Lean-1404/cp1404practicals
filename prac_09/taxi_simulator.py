from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4), SilverServiceTaxi("Lindsay Mobile", 150, 20)]
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ")
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive Distance: "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill = total_bill + trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i}. {taxi}")


main()
