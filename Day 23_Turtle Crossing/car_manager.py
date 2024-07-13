from display import Display
from car import Car
from car_lane import CarLane

CAR_COLORS = ["red", "blue", "orange", "pink", "purple", "yellow", "black", "gold", "aquamarine", "darkred", "magenta"]
CAR_NUM = 15
X_POS_OFFSET = 50
Y_POS_OFFSET = 50
DIFFICULTY_FACTOR = 1.5
COLLISION_CHECK = 25


class CarManager:
    def __init__(self):
        self.screen_borders = Display.get_screen_borders()
        self.left_destination = self.screen_borders["left"] - X_POS_OFFSET
        self.car_catalogue = self.generate_cars()
        self.active_cars = []

    def generate_cars(self):
        car_dict = {}
        x_pos = self.screen_borders["right"] + X_POS_OFFSET
        y_pos = self.screen_borders["top"] + (Y_POS_OFFSET // 2)
        for color in CAR_COLORS:
            y_pos -= Y_POS_OFFSET
            car_lane = CarLane(color)
            car_lane.x_start = x_pos
            car_lane.y_start = y_pos
            car_dict[color] = car_lane
            for i in range(CAR_NUM):
                car = Car(color)
                car.car_speed = car_lane.lane_speed
                car_lane.cars.append(car)
                car.goto(x_pos, y_pos)
        return car_dict

    def release_cars(self, current_time):
        for color in CAR_COLORS:
            car_lane = self.car_catalogue[color]
            car = car_lane.release_car(current_time)
            if car is not None:
                self.active_cars.append(car)

    def move_cars(self):
        for car in self.active_cars:
            car.forward(car.car_speed)

    def return_car_to_lane(self, car):
        index = self.active_cars.index(car)
        self.active_cars.pop(index)
        car_lane = self.car_catalogue[car.pencolor()]
        car_lane.reset_car(car)

    def check_collision(self, player):
        for car in self.active_cars:
            if car.distance(player) <= COLLISION_CHECK:
                print("GAME OVER")
                return True


    def try_requeue_car(self):
        for car in self.active_cars:
            if car.xcor() < self.left_destination:
                self.return_car_to_lane(car)

    def on_level_clear(self):
        while len(self.active_cars) > 0: # without while it doesn't clean up completely
            for car in self.active_cars:
                self.return_car_to_lane(car)
        for color in self.car_catalogue:
            car_lane = self.car_catalogue[color]
            car_lane.on_level_cleared(DIFFICULTY_FACTOR)
