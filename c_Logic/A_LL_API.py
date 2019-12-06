from c_Logic.LL_Employee import Employee_LL
from d_Data.A_Data_API import DataAPI
#import os

class LL_API :
    def __init__(self) :
        self.__dapi = DataAPI( )
        self.empll = Employee_LL( self.__dapi )

    def addnewemplyee( self, new_empl ):
        self.empll.addnewemployee( new_empl ) 