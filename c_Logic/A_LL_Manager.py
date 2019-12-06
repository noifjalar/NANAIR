#from Data.DataManager import DataManager
#from Model.employee import Employee
from c_Logic.LL_Employee import Employee_LL
import os

class LogicManager :
    def __init__(self) :
        self.__dapi = DataManager( )
        self.empll = Employee_LL( __dapi )
        pass 
    def addnewemplyee( self, new_empl ):
        self.empll.addnewemplyee( new_empl ) 