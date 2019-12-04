class AircraftType :
    def __init__(self, planeTypeID, manufacturer, model, capacity, emptyWeight, maxTakeoffWeight, unitThrust, serviceCeiling, length, height, wingspan) :
        self.planeTypeID = planeTypeID
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.emptyWeight = emptyWeight
        self.maxTakeoffWeight = maxTakeoffWeight
        self.unitThrust = unitThrust
        self.serviceCeiling = serviceCeiling
        self.length = length
        self.height = height
        self.wingspan = wingspan

    def __str__(self) :
        return "{planeTypeID}, {manufacturer}, {model}, {capacity}, {emptyWeight}, {maxTakeoffWeight}, {unitThrust}, {serviceCeiling}, {length}, {height}, {wingspan}"
        