class Animal:
    def __init__(self, animal_type, age, description):
        self.animal_type = animal_type
        self.age = age
        self.description = description

    def bite_owner(self):
        print(f"⚠️ Обережно! {self.animal_type} покусав хазяїна!")

    def __str__(self):
        return f"🐾 Тварина: {self.animal_type}, Вік: {self.age}, Опис: {self.description}"

class Car:
    def __init__(self, brand, model, color, fuel=50):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel = fuel

    def drive(self, distance):
        fuel_needed = distance * 0.1
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"🚗 {self.brand} проїхала {distance} км. Пального лишилось: {self.fuel:.1f}л")
        else:
            print(f"🪫 Мало пального для поїздки на {distance} км!")

    def refuel(self, liters):
        self.fuel += liters
        print(f"⛽ Заправлено {liters}л. В баку: {self.fuel}л")

    def __str__(self):
        return f"🚗 Авто: {self.brand} {self.model}, Колір: {self.color}, Пальне: {self.fuel}л"

class Human:
    def __init__(self, name, gender, age, race, job):
        self.name = name
        self.gender = gender
        self.age = age
        self.race = race
        self.job = job
        self.children = []
        self.partner = None
        self.pets = []
        self.car = None

    def buy_car(self, car):
        self.car = car
        print(f"🔑 {self.name} купив машину: {car.brand} {car.model}")

    def add_child(self, child):
        self.children.append(child)
        print(f"👶 У {self.name} з'явилася дитина: {child.name}")

    def marry(self, partner):
        self.partner = partner
        partner.partner = self
        print(f"💍 {self.name} та {partner.name} тепер одружені")

    def add_pet(self, pet):
        self.pets.append(pet)
        print(f"🐶 {self.name} завів тваринку: {pet.animal_type}")

    def __str__(self):
        car_info = f"{self.car.brand} {self.car.model}" if self.car else "Немає"
        return f"👤 {self.name} | Вік: {self.age} | Робота: {self.job} | Машина: {car_info}"

class Child(Human):
    def __init__(self, name, gender, age, race, job="Учень"):
        super().__init__(name, gender, age, race, job)
        self.height = 100

    def grow(self):
        self.age += 1
        self.height += 5
        print(f"📈 {self.name} підріс! Вік: {self.age}, зріст: {self.height}")

nick = Human("Nick", "male", 30, "European", "Developer")
kate = Human("Kate", "female", 28, "European", "Designer")
cat = Animal("Кіт", 3, "Дуже пухнастий")
tesla = Car("Tesla", "Model S", "Black")

nick.marry(kate)
nick.buy_car(tesla)
tesla.drive(120)
tesla.refuel(30)

little_tom = Child("Tom", "male", 5, "European")
nick.add_child(little_tom)
little_tom.grow()
cat.bite_owner()

print("\n=== РЕЗУЛЬТАТИ ===")
print(nick)
print(kate)
print(little_tom)
print(tesla)
print(cat)