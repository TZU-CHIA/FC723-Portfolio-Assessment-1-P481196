# FC723 Project 1 - Part B
# Apache Airlines final seat booking system
# Student GUID: P481196

import random
import string
from database_manager import DatabaseManager


class SeatBookingSystem:
    def __init__(self):
        self.rows = ["A", "B", "C", "D", "E", "F"]
        self.columns = 80
        self.database = DatabaseManager()
        self.seats = {}
        self.create_seats()

    def create_seats(self):
        # The seat map is stored as a dictionary of lists.
        # F = free seat, S = storage space, and a booking reference = reserved seat.
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

    def generate_booking_reference(self):
        # The reference must be exactly 8 alphanumeric characters.
        # The loop continues until a unique reference is made.
        characters = string.ascii_uppercase + string.digits
        while True:
            reference = ""
            for i in range(8):
                reference += random.choice(characters)

            if not self.database.reference_exists(reference):
                return reference

    def check_availability(self, row, column):
        row = row.upper()
        if not self.valid_seat(row, column):
            return "Invalid seat."

        status = self.seats[row][column - 1]
        seat_name = str(column) + row

        if status == "F":
            return "Seat " + seat_name + " is free."
        elif status == "S":
            return "Seat " + seat_name + " is a storage area and cannot be booked."
        else:
            return "Seat " + seat_name + " is booked. Reference: " + status

    def book_seat(self, row, column, passport_number, first_name, last_name):
        row = row.upper()
        if not self.valid_seat(row, column):
            return "Invalid seat."

        status = self.seats[row][column - 1]
        if status == "S":
            return "This is a storage area and cannot be booked."
        if status != "F":
            return "This seat is already booked."

        reference = self.generate_booking_reference()
        self.seats[row][column - 1] = reference
        self.database.add_booking(reference, passport_number, first_name, last_name, row, column)
        return "Booking successful. Seat: " + str(column) + row + ". Reference: " + reference

    def free_seat(self, row, column):
        row = row.upper()
        if not self.valid_seat(row, column):
            return "Invalid seat."

        status = self.seats[row][column - 1]
        if status == "S":
            return "Storage area cannot be freed."
        if status == "F":
            return "This seat is already free."

        self.seats[row][column - 1] = "F"
        self.database.delete_booking_by_seat(row, column)
        return "Seat " + str(column) + row + " has been freed and the passenger record has been removed."

    def make_status_text(self):
        lines = []
        lines.append("F = free, S = storage, X = aisle, booking reference = booked")
        for row in ["A", "B", "C"]:
            lines.append("Row " + row + ": " + " ".join(self.seats[row]))
        lines.append("Aisle: " + " ".join(["X"] * self.columns))
        for row in ["D", "E", "F"]:
            lines.append("Row " + row + ": " + " ".join(self.seats[row]))
        return "\n".join(lines)

    def count_seats(self):
        free_count = 0
        booked_count = 0
        storage_count = 0

        for row in self.rows:
            for status in self.seats[row]:
                if status == "F":
                    free_count += 1
                elif status == "S":
                    storage_count += 1
                else:
                    booked_count += 1

        return free_count, booked_count, storage_count

    def show_database_records(self):
        records = self.database.get_all_bookings()
        if len(records) == 0:
            return "No passenger records are currently stored."

        lines = []
        for record in records:
            reference, passport, first_name, last_name, row, column = record
            line = reference + " | " + first_name + " " + last_name + " | Passport: " + passport + " | Seat: " + str(column) + row
            lines.append(line)
        return "\n".join(lines)
