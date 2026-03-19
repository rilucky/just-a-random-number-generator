import random


class RandomNumber:

    # The generator function takes 3 positional arguments.
    # amount = how many numbers to be generated
    # minRange = starting range of number to be generated
    # maxRange = ending range of numbers to be generated

    def generator(self, amount, minRange, maxRange):

        # Pre-conditions:
        # Check type of inputs using a single isinstance check instead
        # of three separate type() comparisons
        if not all(isinstance(x, int) for x in (amount, minRange, maxRange)):
            raise TypeError("Program only accepts integers")

        # Checks that amount is greater than 1
        if amount < 1:
            raise ValueError("Amount must be greater than 0")

        # Check that starting range is less than end range
        if minRange >= maxRange:
            raise ValueError("Starting point must be less than end point")

        # Use a list comprehension instead of a loop with append.
        # List comprehensions are faster because they avoid repeated
        # attribute lookups for the append method and are optimized
        # at the bytecode level.
        result = [random.randint(minRange, maxRange) for _ in range(amount)]

        return result


rand = RandomNumber()
rand.generator(5, 1, 10)
