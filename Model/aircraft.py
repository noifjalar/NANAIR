class Airplane :
    def __init__(self,planeInsignia, planeId) :
        self.planeInsignia = planeInsignia
        self.planeId = planeId

    def __str__(self) :
        return "planeInsignia: {self.planeInsignia} - planeID: {self.planeID}"

    