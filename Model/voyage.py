class Voyage :
    def __init__(self, flightNumber, departingFrom, arrivingAt, departure, arrival):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt 
        self.departure = departure
        self.arrival = arrival
       

    def __str__(self):
        return "Flight number: {self.flightNumber} - Departing from: {self.departingFrom} - Arriving at: {self.arrivingAt} - Departure: {self.departure} - Arrival: {self.arrival}"


    def voy_comma_to_string (self):
        ret = self.flightNumber + ","\
              + self.departingFrom + ","\
              + self.arrivingAt + ","\
              + self.departure + ","\
              + self.arrival
        return ret


class Voyage_2 :
    def __init__(self, aircraftID, captain, copilot, fsm, fa1, fa2):
        self.aircraftID = aircraftID
        self.captain = captain
        self.copilot = copilot 
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2


    def __str__(self):
        return "Aircraft ID: {self.aircraftID} - Captain: {self.captain} - Copilot: {self.copilot} - Flight service manager: {self.fsm} - Flight attndant: {self.fa1} - Flight attendant: {self.fa2}"


    def voy_comma_to_string_2 (self):
        ret = self.aircraftID + ","\
              + self.captain + ","\
              + self.copilot + ","\
              + self.fsm + ","\
              + self.fa1 + ","\
              + self.fa2
        return ret