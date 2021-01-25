"""
This module holds the class "Product" for Acme products,
as well as product subclasses.
"""

from random import randint


class Product:

    def __init__(self, name,
                 price=None, weight=None, flammability=None):
        """
        A product must be given a name, and instantiates with
        random id, default price, weight, and flammability.
        """

        self.id = randint(1000000, 10000000)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

        try:

            # Assign default values
            if name is None:
                raise ValueError
            if price is None:
                self.price = 10
            if weight is None:
                self.weight = 20
            if flammability is None:
                self.flammability = 0.5

        except ValueError:
            print("You must provide the product name.")
            return

    def stealability(self):
        """
        Prints the level of stealability based on price and weight.
        """

        result = "No stealability score yet ..."

        try:
            e = """
            Price and weight must be numerical values
            in order to calculate stealability.
            """
            score = round(self.price / self.weight, 2)

        except TypeError:
            print(e)
            return

        if score < 0.5:
            result = "Not very stealable."

        elif score < 1.0:
            result = "Kinda stealable ..."

        else:
            result = "Very stealable!"

        print(result)

    def explode(self):
        """
        Prints the level of explosion
        based on weight and flammability.
        """

        result = "No explode score yet ..."

        try:
            e = """
            Weight and flammability must be numerical values
            in order to calculate explosion.
            """
            score = round(self.weight * self.flammability, 2)

        except TypeError:
            print(e)
            return

        if score < 10:
            result = "... fizzle."

        elif score < 50:
            result = "... boom!"

        else:
            result = "... BABOOM!!"

        print(result)


#####################################################################


class BoxingGlove(Product):
    """A product with name='Boxing Glove' and weight=10."""

    def __init__(self):
        """A subclass of Product which is a boxing glove."""

        self.id = randint(1000000, 10000000)
        self.name = 'Boxing Glove'
        self.price = 10
        self.weight = 10
        self.flammability = 0.5

    def explode(self):
        """Prints explosion level for boxing glove."""
        print("... It's a glove.")

    def punch(self):
        """
            Prints the reaction to a punch from the glove,
            calculated based on the weight.
        """

        result = "No punch has happened yet ..."

        if self.weight < 5:
            result = "That tickles."

        elif self.weight < 15:
            result = "Hey that hurts!"

        else:
            result = "OUCH!"

        print(result)
