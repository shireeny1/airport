

class Flight_trip():
    def __init__(self, destination, origin, plane): # 'self' = instance of an object
        self.passengers = []
        self.destination = destination
        self.origin = origin
        self.plane = plane

    def add_plane(self, plane_number):
        self.plane = plane_number

    def add_destination(self, destination):
        self.destination = destination

    def add_origin(self, origin):
        self.origin = origin

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
