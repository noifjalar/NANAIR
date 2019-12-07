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
                    key = emp.ssn


                    
                crew_file.close()      
        except FileNotFoundError :
            return None 



    def change_emp_addr_data(self, new_address, emp_ssn) :
        #new_addr = Employee(new_address) #vantar 6 annað ssn, simanr ofl þarf að sækja það úr file og tengja saman eða ehv 
        pass

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