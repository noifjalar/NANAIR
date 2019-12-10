class Destination:
    def __init__(self, identity, destination, flight_time) :
        self.identity = identity
        self.destination = destination
        self.flight_time = flight_time

    def __str__(self) :
        return "id: {identity} - destination: {destination} - Flight time: {flight_time}"

    def dest_comma_to_string (self):
        ret = self.identity + ","\
              + self.destination + ","\
              + self.flight_time
        return ret