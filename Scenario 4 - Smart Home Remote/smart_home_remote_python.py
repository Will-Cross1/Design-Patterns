# Command Design pattern

# Appliance
# The classes that represent the actual devices for the smart home
# These have the appliance logic within ready to be called by commands.
class Light:
    def on(self):
        print("*Sigh* Turning light on")
    def off(self):
        print("Light off. Please make up your mind")

class Door:
    def lock(self):
        print("Door locked, See you real soon...")
    def unlock(self):
        print("Door unlocked, Welcome!")

class Thermostat:
    def set_temperature(self, temperature):
        if temperature < 18:
            print("Where do you live? A fridge?")
        elif temperature > 32:
            print("Do you love the desert that much?")
        print(f"Thermostat set to {temperature} degrees")


# Every command will inherit this class
# Not necessarily needed, but for this design pattern it guarantees each Command has an execute method for RemoteControl.
class Command:
    def execute(self):
        print("Command not linked to an application function!")

# In python, these would not be individual classes for each application command
# but could be a generic Command that can be filled in with any action from the applications.
# For simplicity and to demonstrate the pattern better, this splits each command.
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

class DoorLockCommand(Command):
    def __init__(self, door):
        self.door = door

    def execute(self):
        self.door.lock()

class DoorUnlockCommand(Command):
    def __init__(self, door):
        self.door = door

    def execute(self):
        self.door.unlock()

class SetTemperatureCommand(Command):
    def __init__(self, thermostat, temperature):
        self.thermostat = thermostat
        self.temperature = temperature

    def execute(self):
        self.thermostat.set_temperature(self.temperature)

class BlenderOnCommand(Command):
    # No Application is linked to this command to demonstrate Command inheritance
    def __init__(self, blender):
        self.blender = blender



# Invoker
# The class that triggers commands. It stores command objects and executes them
# This class does not know about the actual appliances, just how to execute the commands
class RemoteControl:
    def __init__(self):
        self.buttons = {}

    def set_command(self, button_name, command):
        self.buttons[button_name] = command

    def press_button(self, button_name):
        if button_name in self.buttons:
            print(f"{button_name} command found... Executing")
            self.buttons[button_name].execute()
        else:
            print("No command assigned")


if __name__ == "__main__":
    # Initial setup, assign a button for each command
    light = Light()
    door = Door()
    thermostat = Thermostat()

    remote = RemoteControl()


    remote.set_command("light_on", LightOnCommand(light))
    remote.set_command("light_off", LightOffCommand(light))
    
    remote.set_command("lock_door", DoorLockCommand(door))
    remote.set_command("unlock_door", DoorUnlockCommand(door))
    
    remote.set_command("temp_wake_up", SetTemperatureCommand(thermostat, 22))
    remote.set_command("temp_leave_house", SetTemperatureCommand(thermostat, 16))
    remote.set_command("temp_winter_here", SetTemperatureCommand(thermostat, 34))
    
    remote.set_command("blender_on", BlenderOnCommand(None))
    
    
    # User usage, simulates a user selecting a button from their remote control
    remote.press_button("light_on")
    print("")
    remote.press_button("light_off")
    
    print("\n"*2)
    remote.press_button("lock_door")
    print("")
    remote.press_button("unlock_door")
    
    print("\n"*2)
    remote.press_button("temp_wake_up")
    print("")
    remote.press_button("temp_leave_house")
    print("")
    remote.press_button("temp_winter_here")
    
    # This command does not exist, and should say "No command assigned"
    print("\n"*2)
    remote.press_button("make_tea")
    
    # The blender appliance does not exist, yet there is a BlenderOn command (likely included as a company promotion)
    # This should say "Command not linked to any application!" as the command is not linked to an appliance.
    print("\n"*2)
    remote.press_button("blender_on")
