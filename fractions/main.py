import math


class Rational:

    def __init__(self, a: int, b: int):
        """

        :param a: divisible
        :param b: divider
        """
        if not isinstance(a, int):
            raise TypeError('Wrong type of variable A, only int accepted')
        if not isinstance(b, int):
            raise TypeError('Wrong type of variable B, only int accepted')
        if not b:
            raise ZeroDivisionError

        self.a = a
        self.b = b

    def __str__(self):
        """

        :return: string view of fraction
        """
        sign = '' if self.a * self.b > 0 else '-'
        a, b = abs(self.a), abs(self.b)
        gdc = math.gcd(a, b)
        a //= gdc
        b //= gdc

        if a == b:
            return f'{sign}1'

        if b == 1:
            return f'{sign}{a}'

        if a > b:
            return f'{sign}{a // b} {a - a // b * b}/{b}'

        return f'{sign}{a}/{b}'

    def __sub__(self, other):
        """

        :param other: subtrahend fraction
        :return: fraction (class Rational)
        """
        if isinstance(other, int):
            other = Rational(other, 1)

        common_divisor = self.b * other.b

        a = common_divisor // self.b * self.a -\
            common_divisor // other.b * other.a

        return Rational(a, common_divisor)

    def __rsub__(self, other):
        """

        :param other: subtrahend fraction
        :return: fraction (class Rational)
        """
        if isinstance(other, int):
            other = Rational(other, 1)

        common_divisor = self.b * other.b

        a = common_divisor // other.b * other.a - \
            common_divisor // self.b * self.a

        return Rational(a, common_divisor)

    def __add__(self, other):
        """

        :param other: addendum
        :return: fraction (class Rational)
        """
        if isinstance(other, int):
            other = Rational(other, 1)

        common_divisor = self.b * other.b

        a = common_divisor // self.b * self.a + \
            common_divisor // other.b * other.a

        return Rational(a, common_divisor)

    def __radd__(self, other):
        """

        :param other: addendum
        :return:
        """
        if isinstance(other, int):
            other = Rational(other, 1)

        common_divisor = self.b * other.b

        a = common_divisor // self.b * self.a + \
            common_divisor // other.b * other.a

        return Rational(a, common_divisor)

    def __mul__(self, other):
        """

        :param other: multiplier
        :return:
        """
        if isinstance(other, int):
            other = Rational(other, 1)

        a = self.a * other.a
        b = self.b * other.b

        return Rational(a, b)

    def __rmul__(self, other):
        """

        :param other: multiplier
        :return:
        """
        if isinstance(other, int):
            other = Rational(other, 1)

        a = self.a * other.a
        b = self.b * other.b

        return Rational(a, b)

    def __truediv__(self, other):
        """

        :param other: divider
        :return:
        """

        if isinstance(other, int):
            other = Rational(other, 1)

        a = self.a * other.b
        b = self.b * other.a

        return Rational(a, b)

    def __rtruediv__(self, other):
        """

        :param other: divider
        :return: fraction (class Rational)
        """

        if isinstance(other, int):
            other = Rational(other, 1)

        a = other.a * self.b
        b = other.b * self.a

        return Rational(a, b)


if __name__ == "__main__":
    first = Rational(1, 2)
    second = Rational(1, 2)
    num = 5
    sub = first - num
    add = first + num
    mul = first * num
    truediv = first / num

    print(f'{first} - {num} = {sub}')
    print(f'{first} + {num} = {add}')
    print(f'{first} * {num} = {mul}')
    print(f'{first} / {num} = {truediv}')
