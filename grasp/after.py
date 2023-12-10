import string
import random


class VehicleRegistry:
    def generate_vehicle_id(self):
        return ''.join(random.choices(string.ascii_uppercase, k=12))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def get_vehicle_licence(self):
        """Return licence of a vehicle"""
        vehicle_id = self.generate_vehicle_id()
        license_plate = self.generate_vehicle_license(vehicle_id)
        return license_plate


class VehicleInfo:
    def __init__(self, brand):
        self.brand = brand
        self.__price = self.__get_price()
        self.__payable_tax = self.__get_price()
    def __get_price(self):
        """Compute the catalog price"""
        catalog_price = 0
        if self.brand == 'Tesla Model 3':
            catalogue_price = 60000
        elif self.brand == 'Volkswagen ID3':
            catalogue_price = 35000
        elif self.brand == "BMW 5":
            catalogue_price = 45000

        return catalog_price

    def __get_tax(self):
        """Compute the tax percentage"""
        tax_percentage = 0.05
        if self.brand == "Tesla Model 3" or self.brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * self.__price

        return payable_tax

    def get_info(self):
        return {
            'price': self.__price,
            'tax': self.__payable_tax
        }


class Application:
    def register_vehicle(self, brand: string):
        # create a register instance
        registry = VehicleRegistry()

        # get a license plate
        license_plate = registry.get_vehicle_licence()

        # get vahicle info
        info = VehicleInfo(brand).get_info()

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {info.get('tax')}")



app = Application()
app.register_vehicle("BMW 5")
