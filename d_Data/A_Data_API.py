# VIRKAAAAAAAAR!
# its true
# omg

from Model import *
from .Data_Employee import Employee_Data


class DataManager : 
    def __init__(self) :
        self.demp = Employee_Data( )
        pass

    def storenewemplyee (self,  new_empl  ):
        return self.demp.register_employee_Data ( new_empl )

    def myprint(self):
        return "datamanager str"


        