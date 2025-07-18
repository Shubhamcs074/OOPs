"""Q9: Create a base class Device with a constructor that sets brand and power_status. Then create a
subclass Phone that adds number_of_cameras, and another subclass SmartPhone that adds
os_version.
Use super() in each constructor to properly initialize the full inheritance chain."""

class Device:
    def __init__(self, brand, power_status):
        self.brand = brand
        self.power_status = power_status

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Power Status: {self.power_status}")

class Phone(Device):
    def __init__(self, brand, power_status,number_of_cameras):
        super().__init__(brand, power_status)
        self.number_of_cameras = number_of_cameras

    def display_details(self):
        super().display_details()
        print(f"Number of Cameras: {self.number_of_cameras}")

class SmartPhone(Phone):
    def __init__(self, brand, power_status, number_of_cameras, os_version):
        super().__init__(brand, power_status, number_of_cameras)
        self.os_version = os_version
    
    def display_details(self):
        super().display_details()
        print(f"OS Version: {self.os_version}")

Device1 = SmartPhone("Samsung", "On", 3, "Android 13")
Device1.display_details()

    

