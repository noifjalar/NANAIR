from Model.employee import Employee 

class Employee_Data :
    def __init__(self):
        self.filename = "./a_csv/Crew.csv"
        

    def register_employee_Data(self, ssn, name, role, rank, licence, address, phonenumber):
        # id er hardkodad i bili
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




# Gylfi gerði counter sem enginn skilur ;)
    # def getNextID( ):
    #     f = open( self.filename, "r") 
    #     ret = f.readlines().count
    #     f.close()
    #     return ret + 1 