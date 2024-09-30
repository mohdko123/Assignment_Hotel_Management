class Employee:
    def __init__(self, employee_id, name, address):
        self.__employee_id = employee_id
        self.__name = name
        self.__address = address

    # getter and setter methods
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


class Visitor:
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__booking = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def book_room(self, room_type, start_date, end_date, room_list):
        print("Method Function: This method will take the details and send a room booking request")

    def view_booking(self):
        '''
        This method will show the details of the bookings

        '''
        if self.__booking is not None:
            booking = self.__booking
            print(f"Booking Details for {self.__name}:")
            print(f"Room Number: {booking.get_room().get_room_number()}")
            print(f"Room Type: {booking.get_room().get_room_type()}")
            print(f"Check-in Date: {booking.get_check_in_date()}")
            print(f"Check-out Date: {booking.get_check_out_date()}")
            print(f"Is Checked In: {booking.get_is_checked_in()}")
            print(f"Is Canceled: {booking.get_is_canceled()}")
        else:
            print(f"{self.__name} has no booking.")

    def cancel_booking(self):
        print("Method Function: this method will sends a request to cancel their booking.")


class Room:
    def __init__(self, room_number, accommodation_size):
        self.__room_number = room_number
        self.__accommodation_size = accommodation_size
        self.__is_booked = False

    # getter and setter methods
    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_accommodation_size(self):
        return self.__accommodation_size

    def set_accommodation_size(self, accommodation_size):
        self.__accommodation_size = accommodation_size

    def is_available(self, start_date, end_date):
        return not self.__is_booked


class SingleBedRoom(Room):
    def __init__(self, room_number, accommodation_size):
        super().__init__(room_number, accommodation_size)
        self.__room_type = "Single"

    def get_room_type(self):
        return self.__room_type


class DoubleBedRoom(Room):
    def __init__(self, room_number, accommodation_size):
        super().__init__(room_number, accommodation_size)
        self.__room_type = "Double"

    def get_room_type(self):
        return self.__room_type


class Booking:
    def __init__(self, visitor, room, check_in_date, check_out_date):
        self.__visitor = visitor
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_checked_in = False
        self.__is_canceled = False

    # getter and setter methods
    def get_visitor(self):
        return self.__visitor

    def set_visitor(self, visitor):
        self.__visitor = visitor

    def get_room(self):
        return self.__room

    def set_room(self, room):
        self.__room = room

    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    def get_is_checked_in(self):
        return self.__is_checked_in

    def set_is_checked_in(self, is_checked_in):
        self.__is_checked_in = is_checked_in

    def get_is_canceled(self):
        return self.__is_canceled

    def set_is_canceled(self, is_canceled):
        self.__is_canceled = is_canceled

    def view_booking(self):
        print("Method Function: This method will show the booking details")

    def cancel_booking(self):
        self.__is_canceled = True

    def update_booking(self, room=None, check_in_date=None, check_out_date=None):
        print("Method Function: This method will update the details of the booking")


class DeskAgent(Employee):
    def __init__(self, employee_id, name, address):
        super().__init__(employee_id, name, address)

    def book_room(self, visitor, room, check_in_date, check_out_date):
        print("Method Function: This method will allow the agent to book the room.")

    def check_room_availability(self, room_type, check_in_date, check_out_date, room_list):
        print("Method Function: This method will allow the agent to check if the room is available.")


# creating afent, visitors and rooms
desk_agent = DeskAgent(employee_id=1, name="Agent", address="UAE")

visitor1 = Visitor(name="Visitor_1", email="visitor1@gmail.com", phone_number="123-555-1234")
visitor2 = Visitor(name="Visitor_2", email="visitor2@gmail.com", phone_number="123-555-5678")
visitor3 = Visitor(name="Visitor_3", email="visitor3@gmail.com", phone_number="123-555-5678")

room1 = SingleBedRoom(room_number=101, accommodation_size=1)
room2 = DoubleBedRoom(room_number=102, accommodation_size=2)

# booking for visitor 1
booking1 = Booking(visitor=visitor1, room=room1, check_in_date="2024-10-01", check_out_date="2024-10-05")
visitor1._Visitor__booking = booking1

# booking for visitor 2
booking2 = Booking(visitor=visitor2, room=room2, check_in_date="2024-10-02", check_out_date="2024-10-06")
visitor2._Visitor__booking = booking2

# viewing the bookings for visitors
visitor1.view_booking()
visitor2.view_booking()
visitor3.view_booking()
