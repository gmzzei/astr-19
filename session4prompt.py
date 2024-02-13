# Write a Python program that declares a class describing your favorite animal. Have the data members of the class
# represent the following physical parameters of the animal: length of the arms (float), length of the legs (float),
# number of eyes (int), does it have a tail? (bool), is it furry? (bool).
# Write an initialization function that sets the values of the data members when an instance of the class is created.
# Write a member function of the class to print out and describe the data members representing the physical
# characteristics of the animal.


class FavoriteAnimal:
    def __init__(self, name: str, arms: float, legs: float, eyes: int, tail: bool, furry: bool):
        self.name = name
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry

    def describe(self):
        print(
            f'name: {self.name}\nlength of arms: {self.arms} in\nlength of legs: {self.legs} in\nnumber of eyes: {self.eyes}\ndoes it have a tail? {self.tail}\nis it furry? {self.furry}')


if __name__ == '__main__':
    pika = FavoriteAnimal('pika', 2.0, 2.0, 2, False, True)

    pika.describe()