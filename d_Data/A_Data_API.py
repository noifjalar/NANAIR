# VIRKAAAAAAAAR!
# its true
# omg

#from Model import *
from d_Data.Data_Employee import Employee_Data


class DataAPI : 
    def __init__(self) :
        self.demp = Employee_Data( )

    def storenewemplyee (self, new_empl ):
        return self.demp.register_employee_Data ( new_empl )

    def myprint(self):
        return "datamanager str"


        