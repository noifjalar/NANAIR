

class Employee_Data :
    def __init__(self):
        self.filename = "./csv/Crew.csv"
        

    def register_employee_Data():
       
        try :
            with open( self.filename ,"a") as crew_file:
                crew_file.write("\n")
                crew_file.write(new_emp_ready_for_print)
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