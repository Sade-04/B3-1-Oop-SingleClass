class RideCoaster:
    #class level scope variables
    total_created = 0
    active_count = 0
    total_capacity = 0

    def __init__(self, coaster_number, name, capacity=25):
        #encapulation of instance variables
        self.__coaster_number = coaster_number
        self.__name = name
        self.__capacity = capacity
        self.__active = True

        #initization 
        RideCoaster.total_created += 1
        RideCoaster.total_capacity += capacity
        RideCoaster.active_count += 1

    #getters
    def get_id(self):
        return self.__coaster_number

    def get_name(self):
        return self.__name

    def get_capacity(self):
        return self.__capacity

    def is_active(self):
        return self.__active

    #safeguards
    def set_capacity(self, new_capacity):
        if new_capacity <= 0:
            print("Error: Capacity must be greater than 0.")
            return False

        if self.__active:
            RideCoaster.total_capacity += (new_capacity - self.__capacity)

        self.__capacity = new_capacity
        return True

    def deactivate(self):
        if not self.__active:
            print(f"Error: Coaster {self.__name} is already inactive.")
            return False

        self.__active = False
        RideCoaster.active_count -= 1
        RideCoaster.total_capacity -= self.__capacity
        print(f"Coaster {self.__name} has been deactivated.")
        return True

    #class level methods
    @classmethod
    def get_total_created(cls):
        return cls.total_created

    @classmethod
    def get_active_count(cls):
        return cls.active_count

    @classmethod
    def get_total_capacity(cls):
        return cls.total_capacity


    def __str__(self):
        return f"Coaster Number: {self.__coaster_number}, Name: {self.__name}, Capacity: {self.__capacity}, Active: {self.__active}"


# Testing the RideCoaster class
if __name__ == "__main__":
    print("THEME PARK RIDE OPERATIONS TEST SUITE")

    print("--- Phase 1: Instantiation ---")
    c1 = RideCoaster("RC-001", "Journey to Atlantis", 24)
    c2 = RideCoaster("RC-002", "Splash Mountain", 16)
    c3 = RideCoaster("RC-003", "Wave Breaker", 20)

    print(c1)
    print(c2)
    print(c3)
    print(f"Global State -> Total Spawned: {RideCoaster.get_total_created()} | Active Count: {RideCoaster.get_active_count()} | Total Capacity: {RideCoaster.get_total_capacity()}")

    print("--- Phase 2: Mutator Bounds Validation ---")
    c1.set_capacity(0)

    print("--- Phase 3: Valid State Mutation ---")
    print(f"Upgrading {c2.get_name()} Capacity to 20...")
    c2.set_capacity(20)
    print(f"Global State -> Total Capacity: {RideCoaster.get_total_capacity()}")

    print("--- Phase 4: Lifecycle Transformation ---")
    c3.deactivate()
    print(f"Global State -> Active Count: {RideCoaster.get_active_count()} | Total Capacity: {RideCoaster.get_total_capacity()}")

    print("--- Phase 5: Redundant Safeguards ---")
    c3.deactivate()
    print(f"Global State -> Active Count: {RideCoaster.get_active_count()} | Total Capacity: {RideCoaster.get_total_capacity()}")

    print("=== Testing Complete! ===")




