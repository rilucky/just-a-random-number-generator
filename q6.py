import random


class RandomNumber:
    def generator(self, amount, minRange, maxRange):

        # Pre-conditions:
        # Check type of inputs
        if type(amount) != int or type(minRange) != int or type(maxRange) != int:
            raise Exception("Program only accepts integers")

        # Checks that amount is greater than 1
        if amount < 1:
            raise Exception("Amount must be greater than 0")

        # Check that starting range is less that end range
        if minRange >= maxRange:
            raise Exception("Starting point must be less than end point")

        result = []
        for i in range(amount):
            number = random.randint(minRange, maxRange)
            result.append(number)

        # Post-conditions
        # Check that there is some numbers has been generated
        if len(result) == 0:
            raise Exception("No numbers has been generated")

        # Check if amount passed and amount of numbers in result are the same
        if len(result) == amount:
            return result
        # Raise exception if not
        else:
            raise Exception("No numbers has been generated")


rand = RandomNumber()

rand.generator(5, 1, 10)
