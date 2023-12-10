import string
import random


class VehicleRegistry:
    def generate_vehicle_id(self):
        return ''.join(random.choices(string.ascii_uppercase, k=12))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:
    def register_vehicle(self, brand: string):
        # create a register instance
        registry = VehicleRegistry()

        # generate a vehicle id
        vehicle_id = registry.generate_vehicle_id()

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # compute the catalog price
        catalog_price = 0
        if brand == 'Tesla Model 3':
            catalogue_price = 60000
        elif brand == 'Volkswagen ID3':
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric
        # cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalog_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")


app = Application()
app.register_vehicle("BMW 5")

# split
# 'ala ma kota'.split(sep=' ')  # sep = ' ' - separator
# ['ala', 'ma', 'kota']

# join
# ' '.join(['ala', 'ma', 'kota'])  # glue = ' '
# 'ala ma kota'

# w innych językach raczej tak
# ['ala', 'ma', 'kota'].join(glue=" ")  -> 'ala ma kota'
