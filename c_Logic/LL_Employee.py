#from b_UI.UI_employee import Employee_UI

class Employee_LL :
    def __init__ (self, dapi_in):
        self.dapi = dapi_in

    '''def register_employee_LL(self):
        if 
        new_emp_ready_for_print = new_emp.emp_comma_to_string
    '''

    def addnewemplyee(self, new_empl ) :
        # first we should check if this is a doubel registration .. 
        if ( self.dapi.getemployeee( new_empl.ssn) == None ) :
            # kasta villu til baka um að notandi er þegar til. 
            pass
        
        # svörum svarinu sem við fáum þegar við köstum þessu niður í skrá 
        return self.dapi.storenewemplyee( new_empl )
        


    def change_employee_info(self):
        







        pass

    def assign_cabin_pilot_to_voyage(self):
        pass
    def display_voyage(self):
        pass
    
