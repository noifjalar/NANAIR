from d_Data.Data_Employee import Employee_Data
from d_Data.Data_Destination import Destination_Data


class DataAPI : 
    def __init__(self) :
        self.demp = Employee_Data( )
        self.ddes = Destination_Data( )

    def storenewemplyee (self, new_empl ):
        return self.demp.register_employee_Data ( new_empl )

    def new_emp_id(self):
        the_new_emp_id = new_emp_id()
        return the_new_emp_id

    def get_counter_from_data_emp(self):
        emp_data = Employee_Data()
        the_id = emp_data.new_emp_id()
        return the_id
        
    def get_pilots(self):
        return self.demp.get_pilots()
    
    def get_dest(self) :
        return self.ddes.get_dest()