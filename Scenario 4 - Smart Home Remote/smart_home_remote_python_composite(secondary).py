# Composite Design Pattern

# Component class
# the parent class for the leaves and the interface.
# allows for the composite to be treated like a single action, even though it is a collection of actions.
class SmartHomeAction:
    def execute(self):
        pass


# Leaf classes
# Smart home commands that can be executed individually, however must manually be added 
# as the composite design pattern does not have a command interface to link to the appliance logic.
# This can be used effectively with the command design pattern, but on its own it does not meet the requirements
class LightOff(SmartHomeAction):
    def execute(self):
        print("Turning light off")
        

class LightOn(SmartHomeAction):
    def execute(self):
        print("Turning light on")


class DoorLock(SmartHomeAction):
    def execute(self):
        print("Locking door")


class SetTemperature(SmartHomeAction):
    def __init__(self, temperature):
        self.temperature = temperature

    def execute(self):
        print(f"Setting thermostat to {self.temperature} degrees")


# Composite
# Stores leaf actions and executes them as a group.
class ActionGroup(SmartHomeAction):
    def __init__(self, name):
        self.name = name
        self.actions = []

    def add(self, action):
        self.actions.append(action)

    def execute(self):
        print(f"Executing macro: {self.name}")

        for action in self.actions:
            action.execute()


if __name__ == "__main__":

    # Individual actions
    light_off = LightOff()
    light_on = LightOn()
    lock_door = DoorLock()
    lower_temp = SetTemperature(16)
    sauna = SetTemperature(50)

    # Composite macros
    leave_house = ActionGroup("Leave House")
    leave_house.add(light_off)
    leave_house.add(lock_door)
    leave_house.add(lower_temp)
    
    annoy_neighbors = ActionGroup("Annoy Neighbors")
    annoy_neighbors.add(light_off)
    annoy_neighbors.add(light_on)
    annoy_neighbors.add(light_off)
    annoy_neighbors.add(light_on)
    annoy_neighbors.add(light_off)
    annoy_neighbors.add(light_on)
    annoy_neighbors.add(light_off)
    
    # Even single action macros are allowed
    sauna_active = ActionGroup("Sauna Active")
    sauna_active.add(sauna)
    

    # Composite can be treated exactly like a single action
    leave_house.execute()
    print("")
    
    annoy_neighbors.execute()
    print("")
    
    sauna_active.execute()