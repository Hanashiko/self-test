class Car01:
	def __init__(this, brand: str, fuel_type: str) -> None:
		this.brand = brand
		this.fuel_type = fuel_type

class Car02:
	def __init__(inst, brand: str, fuel_type: str) -> None:
		inst.brand = brand
		inst.fuel_type = fuel_type


class Car:
	def __init__(self, brand: str, fuel_type: str) -> None:
		self.brand = brand
		self.fuel_type = fuel_type

	def drive(self, distance: float) -> None:
		print(f"Driving {self.brand} for {distance}km [{self.fuel_type}]")

	@staticmethod
	def test() -> None:
		print("Testing...")


volvo: Car = Car(brand="Volvo", fuel_type="Diesel")
bmw: Car = Car(brand="BMW", fuel_type="Electric")

print(volvo.brand)
print(volvo.fuel_type)
volvo.drive(distance=10)

Car.test()
volvo.test()