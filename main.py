import math


class Rational:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('Wrong type of variable, only int accepted')
        self.common_divisor = math.gcd(self.a, self.b)

    def __str__(self):
        if self.a / self.b > 1:
            ceil = self.a // self.b
            return f'{ceil} {int((self.a - (ceil * self.b)) / self.common_divisor)}/{int(self.b / self.common_divisor)}'
        else:
            return f'{int(self.a / self.common_divisor)}/{int(self.b / self.common_divisor)}'

    def __add__(self, other):
        if self.b == other.b:  # If divider A equal divider B

            gcd = math.gcd((self.a + other.a) - ((self.a + other.a) // self.b) * self.b, self.b)

            if (self.a + other.a) // self.b >= 1:  # if fraction have ceil part

                if ((self.a + other.a) - ((self.a + other.a) // self.b) * self.b) != 0:  # if the fraction doesn't
                    # have zero in dividend

                    return f'{(self.a + other.a) // self.b} ' \
                           f'{int(((self.a + other.a) - ((self.a + other.a) // self.b) * self.b) / gcd)}/' \
                           f'{int(self.b / gcd)}'

                else:
                    return f'{(self.a + other.a) // self.b}'
            else:
                return f'{int(((self.a + other.a) - ((self.a + other.a) // self.b) * self.b) / gcd)}/' \
                       f'{int(self.b / gcd)}'

        elif self.b != other.b:  # if divider A not equal divider B

            common_divider = (self.b * other.b // math.gcd(self.b, other.b))  # less common multiple of divider A and B
            a_divisor = int((common_divider / self.b) * self.a)  # recalculate divisor A with new divider
            b_divisor = int((common_divider / other.b) * other.a)  # recalculate divisor B with new divider
            common_divisor = math.gcd(((a_divisor + b_divisor) -
                                       ((a_divisor + b_divisor) // common_divider) * common_divider), common_divider)
            # greatest common divisor of rest of sum a_divisor with b_divisor and common_divider

            if (a_divisor + b_divisor) // common_divider >= 1:  # if fraction have ceil part

                if ((a_divisor + b_divisor) - ((a_divisor + b_divisor) // common_divider) * common_divider) != 0:
                    # if the fraction doesn't have zero in dividend

                    return f'''{
                    (a_divisor + b_divisor) // common_divider
                    } {
                    int(((a_divisor + b_divisor) - ((a_divisor + b_divisor) // common_divider) * common_divider)
                        / common_divisor)
                    }/{
                    int(common_divider / common_divisor)
                    }'''

                else:
                    return f'{(a_divisor + b_divisor) // common_divider}'
            else:
                return f'''{int(((a_divisor + b_divisor) - ((a_divisor + b_divisor) // common_divider) * common_divider)
                                / common_divisor)}/{int(common_divider / common_divisor)}'''

    def __sub__(self, other):
        if self.b == other.b:  # If divider A equal divider B
            gcd = math.gcd((self.a - other.a) - ((self.a - other.a) // self.b) * self.b, self.b)
            if (self.a - other.a) // self.b >= 1:  # if fraction have ceil part

                if ((self.a - other.a) - ((self.a - other.a) // self.b) * self.b) != 0:  # if the fraction doesn't
                    # have zero in dividend

                    return f'{(self.a - other.a) // self.b} ' \
                           f'{int(((self.a - other.a) - ((self.a - other.a) // self.b) * self.b) / gcd)}/' \
                           f'{int(self.b / gcd)}'

                else:
                    return f'{(self.a - other.a) // self.b}'

            elif (self.a - other.a) <= 0:
                return f'-({other - self})'

            else:
                return f'{int(((self.a - other.a) - ((self.a - other.a) // self.b) * self.b) / gcd)}/{int(self.b / gcd)}'

        elif self.b != other.b:  # if divider A not equal divider B

            common_divider = (self.b * other.b // math.gcd(self.b, other.b))  # less common multiple of divider A and B
            a_divisor = int((common_divider / self.b) * self.a)  # recalculate divisor A with new divider
            b_divisor = int((common_divider / other.b) * other.a)  # recalculate divisor B with new divider
            common_divisor = math.gcd(((a_divisor - b_divisor) -
                                       ((a_divisor - b_divisor) // common_divider) * common_divider), common_divider)
            # greatest common divisor of rest of sum a_divisor with b_divisor and common_divider

            if (a_divisor - b_divisor) // common_divider >= 1:  # if fraction have ceil part

                if ((a_divisor - b_divisor) - ((a_divisor - b_divisor) // common_divider) * common_divider) != 0:
                    # if the fraction doesn't have zero in dividend

                    return f'''{
                    (a_divisor - b_divisor) // common_divider
                    } {
                    int(((a_divisor - b_divisor) - ((a_divisor - b_divisor) // common_divider) * common_divider)
                        / common_divisor)
                    }/{
                    int(common_divider / common_divisor)
                    }'''

                else:
                    return f'{(a_divisor - b_divisor) // common_divider}'

            elif int(((a_divisor - b_divisor) - ((a_divisor - b_divisor) // common_divider) * common_divider)
                     / common_divisor) == 0:
                return '0'

            else:
                return f'''{int(((a_divisor - b_divisor) - ((a_divisor - b_divisor) // common_divider) * common_divider)
                                / common_divisor)}/{int(common_divider / common_divisor)}'''

    def __mul__(self, other):
        multed_a = self.a * other.a  # result of multiplying self.a on other.a
        multed_b = self.b * other.b  # result of multiplying self.b on other.b
        gcd = math.gcd(multed_a, multed_b)  # greatest common divisor of multed_a and multed_b

        if multed_a // multed_b >= 1:
            ceil = multed_a // multed_b  # if fraction have ceil part
            if multed_a - (ceil * multed_b) != 0:
                return f'{ceil} {int((multed_a - (ceil * multed_b)) / gcd)}/{int(multed_b / gcd)}'
            else:
                return f'{ceil}'
        elif multed_a == 0:
            return '0'
        elif multed_a < 0:
            multed_a *= -1
            return f'-({int(multed_a / gcd)}/{int(multed_b / gcd)})'
        elif multed_b < 0:
            multed_b *= -1
            return f'-({int(multed_a / gcd)}/{int(multed_b / gcd)})'
        else:
            multed_fraction = f'{int(multed_a / gcd)}/{int(multed_b / gcd)}'

            return multed_fraction

    def __truediv__(self, other):
        return self * Rational(other.b, other.a)  # To divide a fraction,
        # multiply the fraction by the reciprocal of the divisor


first = Rational(1, 1)
second = Rational(1, 3)
w = first + second
x = first - second
z = first * second
q = first / second
print(w)
print(x)
print(z)
print(q)
