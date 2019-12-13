from d_Data.A_Data_API import DataAPI
from d_Data.Data_Employee import Employee_Data

class Employee_LL :
    def __init__ (self):
        #self.dapi = dapi_in
        self.demp = Employee_Data()

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
    def get_chosen_emp(self, emp_ssn) :
        return self.demp.get_chosen_emp(emp_ssn)
        
    def addnewemployee(self, ssn, name, role, rank, licence, address, phonenumber):
        '''Áfram senda skipun um að skrifa í csv skjal'''
        self.demp.register_employee_Data(ssn, name, role, rank, licence, address, phonenumber)

    def check_emp_ssn(self,ssn) :
        '''check if emp already exists by checkin curretn employees ssn'''
        counter = 1 
        crew_dict = self.demp.get_crew_dict()
        for key in crew_dict.keys() :
            if counter > 1 :
                if key == ssn :
                    return False
            counter += 1        
        return True

              
    def change_employee_address(self, new_address, emp_ssn) :
        '''passa að employeeinn sé til'''
        self.demp.change_emp_addr_data(new_address, emp_ssn)
    
    def change_employee_role_rank(self, new_role, new_rank, emp_ssn) :
        '''passa að employeeinn sé til'''
        self.demp.change_emp_role_rank_data(new_role, new_rank, emp_ssn)

    def change_employee_licence(self, new_licence, emp_ssn) :
        '''passa að employeeinn sé til'''
        self.demp.change_emp_lice_data(new_licence, emp_ssn)

    def change_employee_phonenumber(self, new_phonenumber,emp_ssn) :
        '''passa að employeeinn sé til'''
        self.demp.change_emp_phone_data(new_phonenumber, emp_ssn)

    

        

    def assign_cabin_pilot_to_voyage(self):
        pass

    
    def get_pilots(self):
        return self.demp.get_pilots()

    def get_cabin(self) :
        return self.demp.get_cabin()

    def get_pilots_with_NABAE146(self):
        return self.demp.get_pilots_with_NABAE146()

    def get_pilots_with_NAFokkerF28(self):
        return self.demp.get_pilots_with_NAFokkerF28()

    def get_pilots_with_NAFokker100(self):
        return self.demp.get_pilots_with_NAFokker100()