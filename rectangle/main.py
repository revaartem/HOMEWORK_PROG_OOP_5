
class Rectangle:

    def __init__(self, a: int, b: int):
        """

        :param a: side of rectangle
        :param b: side of rectangle
        """
        self.a = a
        self.b = b

    def square(self):
        """

        :return: square of rectangle
        """
        return self.a * self.b

    def __add__(self, other):
        """

        :param other: addendum
        :return: sum
        """
        if isinstance(other, Rectangle):
            return self.square() + other.square()
        if isinstance(other, int):
            return self.square() + other
        return NotImplemented

    def __radd__(self, other):
        """

        :param other: addendum
        :return: sum
        """
        if isinstance(other, (int, float)):
            return self.square() + other
        return NotImplemented

    def __sub__(self, other):
        """

        :param other: subtrahend
        :return: difference
        """
        return self.square() - other.square()

    def __mul__(self, other):
        """

        :param other: multiplier
        :return: multiplication score
        """
        if isinstance(other, int):
            return self.square() * other
        else:
            raise TypeError ('Only int in multiplier accepted')

    def __truediv__(self, other):
        """

        :param other: divider
        :return: division result
        """
        if isinstance(other, int):
            return self.square() / other
        else:
            raise TypeError ('Only int in divider accepted')

    def __eq__(self, other):
        """

        :param other: isinstance class Rectangle
        :return: True or False
        """
        return self.square() == other.square()

    def __gt__(self, other):
        """

        :param other: isinstance class Rectangle
        :return: True or False
        """
        return self.square() > other.square()

    def __lt__(self, other):
        """

        :param other: isinstance class Rectangle
        :return: True or False
        """
        return self.square() < other.square()

    def __le__(self, other):
        """

        :param other: isinstance class Rectangle
        :return: True or False
        """
        return self.square() <= other.square()

    def __ge__(self, other):
        """

        :param other: isinstance class Rectangle
        :return: True or False
        """
        return self.square() >= other.square()

    def __str__(self):
        """

        :return: str vision of rectangle
        """
        return f'{self.a} x {self.b} rectangle'


if __name__ == "__main__":
    rec_1 = Rectangle(2, 3)
    rec_2 = Rectangle(1, 3)

    add = rec_1 + rec_2
    print(add)
    sub = rec_1 - rec_2
    print(sub)
    truediv = rec_1 / 2
    print(truediv)
    print(rec_1)