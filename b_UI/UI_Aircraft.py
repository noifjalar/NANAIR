from Model.aircraft import Aircraft
from c_Logic.A_LL_API import LL_API
from d_Data.Data_Aircraft import Aircraft_Data



class UI_Aircraft :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in

    def register_aircraft_UI(self):
        planeInsignia = input("Plane insignia: ")
        planeTypeId = input("Plane Type ID: ")
        
        #de = Employee_Data()
        #emp_id = self.la.new_emp_id()
        #emp_id = la.new_emp_id()
        #new_emp = Employee(ssn, name, role, rank, licence, address, phonenumber, emp_id)
        self.la.addnewaircraft(planeInsignia, planeTypeId)