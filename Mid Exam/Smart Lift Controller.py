print("welcome to the Smart Lift Controller")
class Lift:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        self.max_floor = 10
    def move_to_floor(self, target_floor):
        if target_floor < 0 or target_floor > self.max_floor:
            print("invalid floor.please enter a floor between 0 and 10.")
            return
        if target_floor == self.current_floor:
            print(f"Lift is already on floor {self.current_floor}.")
            return
        print(f"Moving lift from floor {self.current_floor} to floor {target_floor}.")
        self.current_floor = target_floor
lift = Lift()
print(f"Current floor: {lift.current_floor}")
print(f"Arrived at floor {lift.move_to_floor(3)}")
print(f"Arrived at floor {lift.move_to_floor(5)}")
print(f"Arrived at floor {lift.move_to_floor(11)}")
