import random


class CarLane:
    def __init__(self, color):
        self.cars = []
        self.color = color
        self.x_start = 0
        self.y_start = 0
        self.wave_length = random.choice([1, 2])
        self.last_release_time = None
        if self.wave_length > 1:
            self.release_interval = 2
            self.wave_interval = random.randint(3, 5)
            self.last_wave_time = None
        else:
            self.release_interval = random.randint(3, 5)
            self.wave_interval = None

        self.wave_released = 0
        self.lane_speed = random.randint(5, 8)

    def car_release_timer(self, current_time):
        current_rounded = round(current_time)
        if self.last_release_time is None:
            self.last_release_time = current_rounded
        if current_rounded - self.last_release_time >= self.release_interval:
            self.last_release_time = current_rounded
            return True
        return False

    def new_wave_timer(self, current_time):
        if self.wave_interval is None:
            return True
        current_rounded = round(current_time)
        if self.last_wave_time is None:
            self.last_wave_time = current_rounded
        if current_rounded - self.last_wave_time >= self.wave_interval:
            self.last_wave_time = current_rounded
            return True
        return False

    def release_car(self, current_time):
        if self.wave_released == self.wave_length and self.new_wave_timer(current_time):
            self.wave_released = 0

        if (self.car_release_timer(current_time) and len(self.cars) >= self.wave_length and
                self.wave_released < self.wave_length):
            car = self.cars[0]
            self.cars.pop(0)
            self.wave_released += 1
            return car
        return None

    def reset_car(self, car):
        car.goto(self.x_start, self.y_start)
        self.cars.append(car)

    def on_level_cleared(self, factor):
        self.lane_speed *= factor
        self.wave_released = 0
        self.last_release_time = None
        self.last_wave_time = None
        if self.wave_interval is not None and self.wave_interval > 1:
            self.wave_interval -= 1
        if self.release_interval > 2:
            self.release_interval -= 1
        for car in self.cars:
            car.car_speed = self.lane_speed


