class Family:
    def call_dinner(self):
        print("Seetha, Ram — come for dinner!")

my_family = Family()
my_family.call_dinner()

class Mother:
    def calm_child(self, is_crying):
        if is_crying:
            print("Don't cry, Seetha. Here's a toy for you!")
        else:
            print("Seetha is happy")

mom = Mother()
mom.calm_child(False)
mom.calm_child(False)

class Family:
    def check_noise(self, sleeping):
        if sleeping:
            print("Rama is sleeping")
        else:
            print("Rama is awake.")

family = Family()
family.check_noise(True)
family.check_noise(False)

class FamilyRoutine:
    def wake_up_children(self):
        print("Wake up, children")

    def brush_teeth(self):
        print("Brush your teeth")

    def pack_bag(self):
        print("Pack your school bags")

    def morning_routine(self):
        print("Starting the morning routine...")
        self.wake_up_children()
        self.brush_teeth()
        self.pack_bag()

routine = FamilyRoutine()
routine.morning_routine()

class FamilyMobileUsageTracker:
    def __init__(self):
        self.children_screen_time = {}

    def add_child(self, child_name, screen_time):
        self.children_screen_time[child_name] = screen_time

    def report_screen_time(self):
        print("Family Screen Time Report:")
        for child, hours in self.children_screen_time.items():
            print(f"{child}: {hours} hours")

tracker = FamilyMobileUsageTracker()

tracker.add_child("Seetha", 2.5)
tracker.add_child("Ram", 3)
tracker.add_child("Latha", 1.75)

tracker.report_screen_time()

class FamilyHomework:
    def assign_homework(self, age):
        if age < 6:
            print("Homework assigned: Drawing️")
        elif 6 <= age < 10:
            print("Homework assigned: Math")
        elif age >= 10:
            print("Homework assigned: Science")
        else:
            print("Invalid age!")


homework = FamilyHomework()
homework.assign_homework(4)
homework.assign_homework(7)
homework.assign_homework(12)

class FamilyHealthTracker:
    def __init__(self, family_health):
        self.family_health = family_health

    def doctor(self, child_name):
        print(f"Emergency! Calling the doctor for {child_name}.")

    def check_health(self):
        for child, health_status in self.family_health.items():
            if health_status.lower() == "sick":
                self.doctor(child)
family_health = {
    "Seetha": "healthy",
    "Ram": "sick",
    "Latha": "healthy",
    "Arjun": "sick",
}
tracker = FamilyHealthTracker(family_health)
tracker.check_health()

class Child:
    def __init__(self):
        self.fav_food = {
            "Seetha": "Pizza",
            "Ram": "Pasta",
            "Latha": "Ice Cream",
            "Arjun": "Burger"
        }

    def serve_food(self, name):
        if name in self.fav_food:
            print(f"{name} is being served their favorite food: {self.fav_food[name]}")
        else:
            print(f"Sorry, we don't know {name}'s favorite food.")

children = Child()

children.serve_food("Seetha")
children.serve_food("Ram")
children.serve_food("John")

class Birthday:
    def __init__(self):
        self.wish_list = {
            "Seetha": "Doll",
            "Ram": "Football",
            "Latha": "Painting Kit",
            "Arjun": "Drone"
        }

    def distribute_gifts(self):
        print("Distributing Birthday Gifts")
        for child, gift in self.wish_list.items():
            print(f"{child} receives: {gift}")

bday = Birthday()
bday.distribute_gifts()

class DailyBudgetTracker:
    def __init__(self):
        self.pocket_money = {
            "Seetha": 5,
            "Ram": 8,
            "Latha": 6,
            "Arjun": 10
        }

    def calculate_total_spent(self):
        total_spent = sum(self.pocket_money.values())
        print(f"Total daily expense for pocket money: ${total_spent}")

tracker = DailyBudgetTracker()
tracker.calculate_total_spent()
