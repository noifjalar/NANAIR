class Destination:
    def __init__(self, id, destination, flight_time) :
        self.id = id
        self.destination = destination
        self.flight_time = flight_time

    def __str__(self) :
        return "id: {id} - destination: {destination} - Flight time: {flight_time}"

    def dest_comma_to_string (self):
        ret = self.id + ","\
              + self.destination + ","\
              + self.flight_time
        return ret