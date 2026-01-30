class Vehicle:
  def __init__(self,spot_size):
    self._spot_size = spot_size
    
  def get_spot_size(self):
    return self._spot_size
    
    
class Car(Vehicle):
  def __init__(self):
    super()._init__(self, 1)
    
class Limo(Vehicle):
  def __init__(self):
    super()._init__(self, 2)

class SemiTruck(Vehicle):
  def __init__(self):
    super()._init__(self, 3)    
        
    

class Driver:
  def __init__(self,id,vehicle):
    self._id = id
    self._vehicle = vehicle
    self._payment_due = 0
    
  def get_id(self):
    return self._id
  
  def get_vehicle(self):
    return self._vehicle
    
  def charge(self,amount):
     self._payment_due += amount
    

class ParkingFloor:
  def __init__(self,spot_count):
    self._spots = [0] * spot_count
    self._vehicle_map = {}
    
    def park_vehicle(self,vehicle) :
      size = vehicle.get_spot_size()
      l,r = 0, 0
      while r < len(self._spots):
        if self._spots[r] !=0:
          l = r+1 
        if r-l+1 == size:
            for k in range(l,r+1):
              self._spots[k] = 1 
            self._vehicle_map[vehicle] = [l,r]
            return True
        r +=1       
      
    def remove_vehicle(self,vehicle):
        start,end = self._vehicle_map[vehicle]
        for i in range(start,end+1):
          self._spots[i] = 0
        del self._vehicle_map[vehicle]    
    
    def get_parking_spots(self):
      return self._spots
    
    def get_vehicle_spots(self,vehicle):
      return self._vehicle_map.get(vehicle)
