# FC723 Project 1 - Part A
# Apache Airlines basic seat booking system
# Student GUID: P481196

class PartABookingSystem:
    def __init__(self):
        self.rows = ["A", "B", "C", "D", "E", "F"]
        self.columns = 80
        self.seats = {}
        self.create_seats()

    def create_seats(self):
        # F means a free seat.
        # S means storage area and must not be booked.
        for row in self.rows:
            self.seats[row] = []
            for column in range(1, self.columns + 1):
                if row in ["D", "E", "F"] and column in [77, 78]:
                    self.seats[row].append("S")
                else:
                    self.seats[row].append("F")

    def valid_seat(self, row, column):
        row = row.upper()
        if row not in self.rows:
            return False
        if column < 1 or column > self.columns:
            return False
        return True

    def check_availability(self, row, column):
        row = row.upper()
        if not self.valid_seat(row, column):
            print("Invalid seat.")
            return

        status = self.seats[row][column - 1]
        if status == "F":
            print("Seat", str(column) + row, "is free.")
        elif status == "R":
            print("Seat", str(column) + row, "is already booked.")
        elif status == "S":
            print("Seat", str(column) + row, "is a storage area and cannot be booked.")

    def book_seat(self, row, column):
        row = row.upper()
        if not self.valid_seat(row, column):
            print("Invalid seat.")
            return

        status = self.seats[row][column - 1]
        if status == "F":
            self.seats[row][column - 1] = "R"
            print("Seat", str(column) + row, "has been booked.")
        elif status == "R":
            print("Seat is already booked.")
        elif status == "S":
            print("This is a storage area and cannot be booked.")

    def free_seat(self, row, column):
        row = row.upper()
        if not self.valid_seat(row, column):
            print("Invalid seat.")
            return

        status = self.seats[row][column - 1]
        if status == "R":
            self.seats[row][column - 1] = "F"
            print("Seat", str(column) + row, "has been freed.")
        elif status == "F":
            print("Seat is already free.")
        elif status == "S":
            print("Storage area cannot be changed.")

    def show_booking_status(self):
        print("\nCurrent booking status")
        print("F = free, R = reserved, S = storage, X = aisle")
        for row in ["A", "B", "C"]:
            print("Row", row + ":", " ".join(self.seats[row]))
        print("Aisle:", " ".join(["X"] * self.columns))
        for row in ["D", "E", "F"]:
            print("Row", row + ":", " ".join(self.seats[row]))
        print()

    def count_available_seats(self):
        free_count = 0
        booked_count = 0
        storage_count = 0
        for row in self.rows:
            for status in self.seats[row]:
                if status == "F":
                    free_count += 1
                elif status == "R":
                    booked_count += 1
                elif status == "S":
                    storage_count += 1
        print("Free seats:", free_count)
        print("Booked seats:", booked_count)
        print("Storage spaces:", storage_count)


def get_seat_input():
    row = input("Enter seat row letter A-F: ")
    try:
        column = int(input("Enter seat column number 1-80: "))
    except ValueError:
        print("Column must be a number.")
        return None, None
    return row, column


def main():
    system = PartABookingSystem()

    while True:
        print("\nApache Airlines Seat Booking System - Part A")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking status")
        print("5. Count available seats")
        print("6. Exit program")

        choice = input("Choose an option: ")

        if choice == "1":
            row, column = get_seat_input()
            if row is not None:
                system.check_availability(row, column)
        elif choice == "2":
            row, column = get_seat_input()
            if row is not None:
                system.book_seat(row, column)
        elif choice == "3":
            row, column = get_seat_input()
            if row is not None:
                system.free_seat(row, column)
        elif choice == "4":
            system.show_booking_status()
        elif choice == "5":
            system.count_available_seats()
        elif choice == "6":
            print("Program closed.")
            break
        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()
