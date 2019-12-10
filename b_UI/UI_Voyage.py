from Model.voyage import Voyage
from c_Logic.A_LL_API import LL_API
import datetime


class voyage_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in


    def register_voyage_UI(self):
        

        flightNumber = input("Enter a flight number :")

        departingFrom =input("Enter departingFrom :")

        arrivingAt =input("Enter arrivingAt :")


        year= int(input('input a year:'))
        month= int(input('input a month:'))
        day= int(input('input a day:'))
        hour= int(input('input a hour:'))
        minute= int(input('input a minute:'))

        year, month, day, hour, minute = year, month, day, hour, minute
        departure = datetime.datetime(year, month, day, hour, minute).isoformat()
        
        arrival = ("Enter arrivingAt  TIME :")

        self.la.addnewvoyage(flightNumber, departingFrom, arrivingAt, departure, arrival)

