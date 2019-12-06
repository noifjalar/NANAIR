from d_Data.A_Data_API import DataAPI

class Employee_LL :
    def __init__ (self, dapi_in):
        self.dapi = dapi_in

    '''def register_employee_LL(self):
        if 
        new_emp_ready_for_print = new_emp.emp_comma_to_string
    '''

    def addnewemployee(self, new_empl ) :
        # first we should check if this is a doubel registration .. 
        if ( self.dapi.getemployeee( new_empl.ssn) == None ) :
            # kasta villu til baka um að notandi er þegar til. 
            pass
        
        # svörum svarinu sem við fáum þegar við köstum þessu niður í skrá 
        return self.dapi.storenewemplyee( new_empl )
        


    def change_employee_info(self):
        # open file
        # read file
        # insert file content into dict in a list
        with open ("Crew.csv","r") as file_object:
            counter = 0
            for line in file_object:
                counter += 1
            new_emp_id = counter + 1






        pass

    def assign_cabin_pilot_to_voyage(self):
        pass
    def display_voyage(self):
        pass
    
