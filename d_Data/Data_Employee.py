import csv
from Model.employee import Employee 

class Employee_Data :
    def __init__(self):
        self.filename = "./a_csv/Crew.csv"
        
        ''' Choose 1 in menu '''

    def register_employee_Data(self, ssn, name, role, rank, licence, address, phonenumber):
        new_emp = Employee(ssn, name, role, rank, licence, address, phonenumber)
        try :
            with open( self.filename ,"a") as crew_file:
                crew_file.write("\n")
                crew_file.write(new_emp.emp_comma_to_string())
                crew_file.close()      
        except FileNotFoundError :
            return None       
        #except expression as identifier:
            #pass
        #finally:
            #return False
    #return True 


    
        ''' Choose 2 in menu '''

    def get_crew_dict(self) :
        crew_dict = {}
        try :
            with open( self.filename ,"r") as crew_file:
                for line in crew_file :
                    ssn, name, role, rank, licence, address, phonenumber = line.strip().split(",")
                    emp = Employee(ssn, name, role, rank, licence, address, phonenumber)
                    emp_list = [emp.name, emp.role, emp.rank, emp.licence, emp.address, emp.phonenumber]
                    key = emp.ssn 
                    crew_dict[key] = (emp_list)
                #crew_dict = self.overwrite_crew_file()
                return crew_dict     
                crew_file.close()      
        except FileNotFoundError :
            return None 

        ''' Choose 2 in menu '''

    def get_chosen_emp(self, emp_ssn) :
        ''' ath þurfum að senda þetta upp en ekki prenta hér! '''
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                return value 

        ''' Choose 2 in menu ''' 

    def change_emp_addr_data(self, new_address, emp_ssn) :
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                value[4] = new_address
    

    def 
            

                
         
        #return crew_dict         

        ''' Choose 2 in menu ''' 

    def change_emp_role_data(self, new_role, emp_ssn) :
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                value[1] = new_role

        ''' Choose 2 in menu ''' 

    def change_emp_rank_data(self, new_rank, emp_ssn) :
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                value[2] = new_rank

        ''' Choose 2 in menu ''' 

    def change_emp_lice_data(self, new_licence, emp_ssn) :
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                value[3] = new_licence

        ''' Choose 2 in menu ''' 
        
    def change_emp_phone_data(self, new_phonenumber, emp_ssn) :
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                value[5] = new_role

        ''' Choose 2 in menu ''' 
    
    def overwrite_crew_file(self):
        crew_dict = self.get_crew_dict()
        print(crew_dict)