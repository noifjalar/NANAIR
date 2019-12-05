class Employee :
    def __init__(self, ssn, name, role, rank, licence, address, phonenumber):
        self.ssn = ssn
        self.name = name
        self.role = role 
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phonenumber = phonenumber

    def __str__(self):
        return "Name: {self.name} - SSN: {self.ssn} - role: {self.role} - licence: {self.licence} - address: {self.address} - phonenumber: {self.phonenumber} "

    def get_ssn(self, ssn):
        return self.ssn

    def set_ssn(self, ssn_in):
        ssn_in.isdigit
        self.ssn = ssn_in

    def toCommaSparatedString (self):
        ret = self.ssn + ","\
              + self.name + ","\
              + self.address + ","\
              + self.role + ","\
              + self.rank + ","\
              + self.licence + ","\
              + self.phonenumber
        return ret
