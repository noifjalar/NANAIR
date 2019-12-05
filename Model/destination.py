class Destination:
    def __init__(self, id, destination) :
        self.id = id
        self.destination = destination

    def __str__(self) :
        return "id: {id} - destination: {destination}"

    def dest_comma_to_string (self):
        ret = self.id + ","\
              + self.destination
        return ret