from c_Logic.A_LL_API import LL_API

class UI_Destination:
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in

    def register_destination_UI(self):
        ''' Registers destinations and appends it to CSV '''
        print("-=x="*15)
        print(" "*20 + "Register destination")
        print("-=x="*15 + "\n")
        identity = input("ID: ")
        destination = input("Destination: ")
        flight_time = input("Flight time: ")
        # new_destination = Destination(identity, destination, flight_time)
        self.la.addnewdestination(identity, destination, flight_time)