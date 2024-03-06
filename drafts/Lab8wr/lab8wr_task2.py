class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed


if __name__ == "__main__":
    my_car = Car(2020, "Toyota")

    
    for i in range(5):
        my_car.accelerate()
        print(f"The speed of the car after acceleration {i+1}: {my_car.get_speed()}")

    
    for i in range(5):
        my_car.brake()
        print(f"The speed of the car after brake {i+1}: {my_car.get_speed()}")
