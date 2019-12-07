import csv
from Model.employee import Employee 

class Employee_Data :
    def __init__(self):
        self.filename = "./a_csv/Crew.csv"
        

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
                return crew_dict     
                crew_file.close()      
        except FileNotFoundError :
            return None 

    def get_chosen_emp(self, emp_ssn) :
        ''' ath þurfum að senda þetta upp en ekki prenta hér! '''
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                print("SSN: {}, Name: {} - Address: {}, Role: {}, Rank: {}, Licence: {}, Phonenumber: {}".format(emp_ssn, value[0], value[1], value[2], value[3], value[4], value[5]))
                return value 

    def change_emp_addr_data(self, new_address, emp_ssn) :
        #new_addr = Employee(new_address) #vantar 6 annað ssn, simanr ofl þarf að sækja það úr file og tengja saman eða ehv 
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                '''
                employee_choice=[]
                employee_choice = crew_dict.items
                '''
                value[4] = new_address
        return crew_dict         


    def change_emp_role_data(self, new_role, emp_ssn) :
        pass

    def change_emp_rank_data(self, new_rank, emp_ssn) :
        pass

    def change_emp_lice_data(self, new_licence, emp_ssn) :
        pass

    def change_emp_phone_data(seld, new_phonenumber, emp_ssn) :
        pass




# Gylfi gerði counter sem enginn skilur ;)
    # def getNextID( ):
    #     f = open( self.filename, "r") 
    #     ret = f.readlines().count
    #     f.close()
    #     return ret + 1 