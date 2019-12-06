from d_Data.A_Data_API import DataAPI
from d_Data.Data_Employee import Employee_Data

class Employee_LL :
    def __init__ (self):
        #self.dapi = dapi_in
        self.dapi = Employee_Data()

    '''def register_employee_LL(self):
        if 
        new_emp_ready_for_print = new_emp.emp_comma_to_string
    '''
    """
    def addnewemployee(self, dapi_in, new_empl ) :
        # first we should check if this is a doubel registration .. 
        if ( self.dapi.getemployee( new_empl.ssn) == None ) :
            # kasta villu til baka um að notandi er þegar til. 
            pass
        
        # svörum svarinu sem við fáum þegar við köstum þessu niður í skrá 
        return self.dapi.storenewemplyee( new_empl )
    """
    def addnewemployee(self, ssn, name, role, rank, licence, address, phonenumber):
        '''Vantar að tékka hvort emp sé til með ssn tékki'''
        self.dapi.register_employee_Data(ssn, name, role, rank, licence, address, phonenumber)
        


    def change_employee_info(self):
        pass
        # open file 
        # read file
        # insert file content into dict in a list
    # def new_emp_id(self):
    #     rugl = DataAPI()
    #     the_new_emp_id = rugl.new_emp_id()
    #     return the_new_emp_id
        






        

    def assign_cabin_pilot_to_voyage(self):
        pass
    def display_voyage(self):
        pass
    
