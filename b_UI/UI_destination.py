from c_Logic.A_LL_API import A_LL_API

class Destination_UI:
    def __init__(self):
        pass

    def register_destination_UI(self):
        identity = input("ID: ")
        destination = input("Destination: ")
        new_destination = Destination(identity, destination)