class Flight:
    #class attributes
    airport = "Brussels South"
    #constructor
    def __init__(self, operator, destination):
        self.operator = operator
        self.destination = destination
    
    def __str__(self):
        return f"Flight from {self.airport} to {self.destination}"
    
    def takeoff(self, ready):
        if ready: 
            return f"{self} ready for take off"
        else: 
            return f"{self} still waiting"

# CommercialFlight inherits Flight
class CommercialFlight(Flight):

    def __init__(self, operator, destination, passengers):
        super().__init__(operator, destination)
        self.passengers = passengers

    def startboarding(self, ready):
      if ready:
          return f"{self.passengers} passengers can start boarding on {self}"
      else:
          return f"No boarding yet for {self}"


# instantiating CommercialFlight objects
c = CommercialFlight("Virgin","Copenhagen",120)
print(c.startboarding(True))
print(c.takeoff(True))



#instantiating Flight objects
a=Flight("Virgin","Amsterdam")
b=Flight("Ryanair","Berlin")
print (a)
print (b)
print (a.takeoff(False))
print (b.takeoff(True))

#print('From', a.airport,"to",a.destination)
#print('From', b.airport,"to",b.destination)
