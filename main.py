# FC723 Project 1 - Part B final application
# Run this file to start the final Apache Airlines booking system.
# Student GUID: P481196

from booking_system import SeatBookingSystem


def get_seat_input():
    row = input("Enter seat row letter A-F: ")
    try:
        column = int(input("Enter seat column number 1-80: "))
    except ValueError:
        print("Column must be a number.")
        return None, None
    return row, column


def main():
    system = SeatBookingSystem()

    while True:
        print("\nApache Airlines Seat Booking System")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking status")
        print("5. Count available seats")
        print("6. Show passenger database records")
        print("7. Exit program")

        choice = input("Choose an option: ")

        if choice == "1":
            row, column = get_seat_input()
            if row is not None:
                print(system.check_availability(row, column))

        elif choice == "2":
            row, column = get_seat_input()
            if row is not None:
                passport_number = input("Enter passport number: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                print(system.book_seat(row, column, passport_number, first_name, last_name))

        elif choice == "3":
            row, column = get_seat_input()
            if row is not None:
                print(system.free_seat(row, column))

        elif choice == "4":
            print(system.make_status_text())

        elif choice == "5":
            free_count, booked_count, storage_count = system.count_seats()
            print("Free seats:", free_count)
            print("Booked seats:", booked_count)
            print("Storage spaces:", storage_count)

        elif choice == "6":
            print(system.show_database_records())

        elif choice == "7":
            print("Program closed.")
            break

        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()
