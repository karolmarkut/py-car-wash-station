class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):

        if not 1 <= comfort_class < 8:
            raise ValueError
        self.comfort_class = comfort_class
        if not 1 <= clean_mark < 11:
            raise ValueError
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: int,
                    clean_power: int, average_rating: int, count_of_rating: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_rating = count_of_rating

    def calculate_washing_price(self, car):
            price = ((car.comfort_class
                      * (self.clean_power - self.car.clean_mark)
                      * self.average_rating)
                     / self.distance_from_city_center)
            return round(price, 1)

    def wash_single_car(self, car):
            if self.clean_power > car.clean_mark:
                car.clean_mark = self.clean_power
