from Model.destination import Destination
from c_Logic.A_LL_API import A_LL_API
from d_Data.Data_Destination import Destination_Data

class UI_Destination:
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in

    def register_destination_UI(self):
        identity = input("ID: ")
        destination = input("Destination: ")
        new_destination = Destination(identity, destination)
