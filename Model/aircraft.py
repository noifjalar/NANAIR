class Aircraft :
    def __init__(self,nickname, aircraftID, planeTypeId,capacity,manufacturer) :
        self.nickname = nickname
        self.aircraftID = aircraftID
        self.planeTypeId = planeTypeId
        self.capacity = capacity
        self.manufacturer = manufacturer

    def __str__(self) :
        return "Nickname: {self.nickname} - Aircraft ID: {self.aircraftID} - Plane Type ID: {self.planeTypeId} - Capacity: {self.capacity} - Manufacturer: {self.manufacturer}"

    def aircraft_comma_to_string (self):
        ret = self.nickname + ","\
              + self.aircraftID + ","\
              + self.planeTypeId + ","\
              + self.capacity + ","\
              + self.manufacturer
        return ret


