class Refrigerator:
    def __init__(self, manufacturer, capacity, model_name):
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.model_name = model_name
        self.door_open = False

    def open_door(self):
        if not self.door_open:
            self.door_open = True
            print(f"Дверца холодильника {self.model_name} открыта.")
        else:
            print(f"Дверца холодильника {self.model_name} уже открыта.")

    def close_door(self):
        if self.door_open:
            self.door_open = False
            print(f"Дверца холодильника {self.model_name} закрыта.")
        else:
            print(f"Дверца холодильника {self.model_name} уже закрыта.")

    def turn_on(self):
        print(f"Холодильник {self.model_name} включен.")


my_fridge = Refrigerator("Samsung", 300, "35AAAAa")
my_fridge.turn_on()
my_fridge.open_door()
my_fridge.close_door()

