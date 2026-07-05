# FC723 Project 1 - Part B
# Database manager for Apache Airlines booking system
# Student GUID: P481196

import sqlite3


class DatabaseManager:
    def __init__(self, database_name="bookings.db"):
        self.database_name = database_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.database_name)

    def create_table(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                booking_reference TEXT PRIMARY KEY,
                passport_number TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                seat_row TEXT NOT NULL,
                seat_column INTEGER NOT NULL
            )
        """)
        connection.commit()
        connection.close()

    def add_booking(self, booking_reference, passport_number, first_name, last_name, seat_row, seat_column):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO bookings
            (booking_reference, passport_number, first_name, last_name, seat_row, seat_column)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (booking_reference, passport_number, first_name, last_name, seat_row, seat_column))
        connection.commit()
        connection.close()

    def delete_booking_by_seat(self, seat_row, seat_column):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM bookings WHERE seat_row = ? AND seat_column = ?", (seat_row, seat_column))
        connection.commit()
        connection.close()

    def reference_exists(self, booking_reference):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT booking_reference FROM bookings WHERE booking_reference = ?", (booking_reference,))
        result = cursor.fetchone()
        connection.close()
        return result is not None

    def get_booking_by_seat(self, seat_row, seat_column):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT booking_reference, passport_number, first_name, last_name, seat_row, seat_column
            FROM bookings
            WHERE seat_row = ? AND seat_column = ?
        """, (seat_row, seat_column))
        result = cursor.fetchone()
        connection.close()
        return result

    def get_all_bookings(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT booking_reference, passport_number, first_name, last_name, seat_row, seat_column
            FROM bookings
            ORDER BY seat_row, seat_column
        """)
        results = cursor.fetchall()
        connection.close()
        return results
