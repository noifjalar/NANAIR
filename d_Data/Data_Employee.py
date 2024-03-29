import csv
import re
import os
from Model.employee import Employee 

class Employee_Data :
    def __init__(self):
        self.filename = "./a_csv/Crew.csv"
        self.trash_file = "./a_csv/Crew_Trash.csv"
        
        
        ''' Choose 1 in menu '''

    def register_employee_Data(self, ssn, name, role, rank, licence, address, phonenumber):
        '''appends new employee information into the crew csv file'''
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
        '''creates a dictionary with all the crew members'''
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

        '''gets the employee from the user ssn input for changing employees info'''
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                return value

        ''' Choose 2 in menu ''' 

    def change_emp_addr_data(self, new_address, emp_ssn) :
        '''changes the address of a chosen employee'''
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                value[4] = new_address
                self.overwrite_crew_file(crew_dict)


                
         
        #return crew_dict         

        ''' Choose 2 in menu ''' 

    def change_emp_role_rank_data(self, new_role, new_rank, emp_ssn) :
        '''changes the role of a chosen employee'''
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                value[1] = new_role
                value[2] = new_rank
                self.overwrite_crew_file(crew_dict)

        ''' Choose 2 in menu ''' 
        
    def change_emp_lice_data(self, new_licence, emp_ssn) :
        '''changes the licence of a chosen employee'''
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn :
                value[3] = new_licence
                self.overwrite_crew_file(crew_dict)

        ''' Choose 2 in menu ''' 
        
    def change_emp_phone_data(self, new_phonenumber, emp_ssn) :
        '''changes the phone number of a chosen employee'''
        crew_dict = self.get_crew_dict()
        for key, value in crew_dict.items():
            if key == emp_ssn:


                #Skoða, new_role, hvað er það?

                value[5] = new_phonenumber
                self.overwrite_crew_file(crew_dict)

        ''' Choose 2 in menu ''' 
    
    def overwrite_crew_file(self, crew_dict):
        '''Creates a backup crew csv file, then overwrites the original file with the new information
        and deletes the backup file after overwriting'''
        string = ""

        dest = self.trash_file
        source = self.filename
        os.rename(source, dest)

        for key,value in crew_dict.items() :
            string = ''.join('{},{},{},{},{},{},{}'.format(key, value[0], value[1], value[2],value[3],value[4],value[5]))

            with open( self.filename ,"a") as crew_file:
                crew_file.write(string)
                crew_file.write("\n")
        
        os.remove(self.trash_file)
        
    def get_all_emp(self) :# þarf kannski að færa upp í LL_Employee?
        '''gets a list with all employees names, returns sorted'''
        crew_list = []
        crew_dict = self.get_crew_dict()
        for value in crew_dict.values() :
            crew_list.append(value[0])
        new_crew_list = crew_list[1:]
        return sorted(new_crew_list)

    def get_pilots(self):# þarf kannski að færa upp í LL_Employee?
        '''gets a list with all pilots names, returns sorted'''

        pilot_list = []
        pilot_dict = self.get_crew_dict()
        for value in pilot_dict.values():
            if value[1] == "Pilot":
                # print(value[1])
                pilot_list.append(value[0])
        return sorted(pilot_list)
        # input("nice")
        # return sorted(pilot_list)

    def get_cabin(self):# þarf kannski að færa upp í LL_Employee?
        '''gets a list with all cabincrew names, returns sorted'''
        cabin_list = []
        cabin_dict = self.get_crew_dict()
        for value in cabin_dict.values() :
            if value[1] == "Cabincrew":
                cabin_list.append(value[0])
        return sorted(cabin_list)

    def get_off_emp(self):
        pass

    def get_on_emp(self):
        pass

    def get_cert_worksheet(self):
        pass

    def get_pilots_with_NABAE146(self):# þarf kannski að færa upp í LL_Employee?
        '''gets a list with all pilots names that have NABAE146 licence, returns sorted'''

        nabae146_list = []
        nabae146_dict = self.get_crew_dict()
        for value in nabae146_dict.values() :
            if value[3] == "NABAE146":
                nabae146_list.append(value[0])
        return sorted(nabae146_list)

    def get_pilots_with_NAFokkerF28(self):# þarf kannski að færa upp í LL_Employee?
        '''gets a list with all pilots names that have NAFokkerF28 licence, returns sorted'''
        nafokkerf28_list = []
        nafokkerf28_dict = self.get_crew_dict()
        for value in nafokkerf28_dict.values() :
            if value[3] == "NAFokkerF28":
                nafokkerf28_list.append(value[0])
        return sorted(nafokkerf28_list)

    def get_pilots_with_NAFokker100(self):# þarf kannski að færa upp í LL_Employee?
        '''gets a list with all pilots names that have NAFokker100 licence, returns sorted'''

        nafokker100_list = []
        nafokker100_dict = self.get_crew_dict()
        for value in nafokker100_dict.values() :
            if value[3] == "NAFokkerF100":
                nafokker100_list.append(value[0])
        return sorted(nafokker100_list)

    def get_pilot_by_aircraft(self): # þarf kannski að færa upp í LL_Employee?
        pass

    

        
