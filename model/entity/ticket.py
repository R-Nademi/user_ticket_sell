from model.tools.validation_ticket import *




class Ticket:
    def __init__(self, code, name, family,birth_date, origin, destination, start_date_time,
                 end_date_time, ticket_type,seat_number, price):
        self.code = code
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.origin = origin
        self.destination = destination
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.ticket_type = ticket_type
        self.seat_number = seat_number
        self.price = price




    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        code_validator(value)
        self._code = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        family_validator(value)
        self._family = value

    @property
    def birth_date(self):
        return  self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        birth_date_validator(value)
        self._birth_date = value

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        origin_validator(value)
        self._origin = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        destination_validator(value)
        self._destination = value

    @property
    def start_date_time(self):
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        start_date_time_validator(value)
        self._start_date_time = value

    @property
    def end_date_time(self):
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, value):
        end_date_time_validator(value)
        self._end_date_time = value

    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        ticket_type_validator(value)
        self._ticket_type = value

    @property
    def seat_number(self):
         return  self._seat_number

    @seat_number.setter
    def seat_number(self, value):
        seat_number_validator(value)
        self._seat_number = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        price_validator(value)
        self._price = value




    def __repr__(self):
        return f"{self.__dict__}"(tuple(self.__dict__))