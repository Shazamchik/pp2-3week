class Car:
  def __init__(cars, brand, model, year):
    cars.brand = brand
    cars.model = model
    cars.year = year

  def display(cars):
    print(f"{cars.brand} {cars.model} {cars.year}")

car1 = Car("Toyota", "55", 2022)
car1.display()