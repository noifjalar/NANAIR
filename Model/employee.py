class Employee :
    def __init__(self, ssn, name, role, rank, licence, address, phonenumber, emp_id):
        self.ssn = ssn
        self.name = name
        self.role = role 
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phonenumber = phonenumber
        self.emp_id = emp_id

    def __str__(self):
        return "Name: {self.name} - SSN: {self.ssn} - role: {self.role} - licence: {self.licence} - address: {self.address} - phonenumber: {self.phonenumber} - employee id: {self.emp_id}"

    def get_ssn(self, ssn):
        return self.ssn

    def set_ssn(self, ssn_in):
        ssn_in.isdigit
        self.ssn = ssn_in

    def emp_comma_to_string (self):
        ret = self.ssn + ","\
              + self.name + ","\
              + self.address + ","\
              + self.role + ","\
              + self.rank + ","\
              + self.licence + ","\
              + self.phonenumber + ","\
              + self.emp_id
        return ret

    def new_emp_id (self):
        with open ("./csv/Crew.csv","r") as file_object:
            counter = 0
            for line in file_object:
                counter += 1
            new_emp_id = counter + 1
        return new_emp_id