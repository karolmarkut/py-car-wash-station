class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        if 0 > comfort_class > 7:
            raise ValueError
        self.comfort_class = comfort_class
        if 0 > clean_mark > 10:
            raise ValueError
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int, average_rating: float,
                 count_of_ratings: float):
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError
        self.distance_from_city_center = distance_from_city_center
        if not (0 <= clean_power <= 10):
            raise ValueError
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car):
        if self.clean_power < car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list):
        income = 0.0
        for car in cars:
            if car.clean_mark < car.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                income += price
        return round(income, 1)

    def calculate_washing_price(self, car: Car):
            difrent = 0
            difrent  = self.clean_power - car.clean_mark
            price =  (car.comfort_class * difrent * self.average_rating) / self.distance_from_city_center
            return round(price,1)

    def rate_service(self, new_rating: float):
        total_rating = (self.average_rating + self.count_of_ratings)
        total_rating += new_rating
        new = round((total_rating + new_rating) / self.count_of_ratings, 1)
        self.count_of_ratings += 1
        self.average_rating = round(new, 1)
