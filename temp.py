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

            if (self.a - other.a) // self.b >= 1:  # if fraction have ceil part

                if ((self.a - other.a) - ((self.a - other.a) // self.b) * self.b) != 0:  # if the fraction doesn't
                    # have zero in dividend

                    return f'{(self.a - other.a) // self.b} ' \
                           f'{((self.a - other.a) - ((self.a - other.a) // self.b) * self.b)}/{self.b}'

                else:
                    return f'{(self.a - other.a) // self.b}'

            elif (self.a - other.a) <= 0:
                other.__rsub__(self)

            else:
                return f'{((self.a - other.a) - ((self.a - other.a) // self.b) * self.b)}/{self.b}'

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
            else:
                return f'''{int(((a_divisor - b_divisor) - ((a_divisor - b_divisor) // common_divider) * common_divider) 
                    / common_divisor)}/{int(common_divider / common_divisor)}'''

    def __rsub__(self, other):
        if self.b == other.b:  # If divider A equal divider B

            if (self.a - other.a) // self.b >= 1:  # if fraction have ceil part

                if ((self.a - other.a) - ((self.a - other.a) // self.b) * self.b) != 0:  # if the fraction doesn't
                    # have zero in dividend

                    return f'{(self.a - other.a) // self.b} ' \
                           f'{((self.a - other.a) - ((self.a - other.a) // self.b) * self.b)}/{self.b}'

                else:
                    return f'{(self.a - other.a) // self.b}'

            elif (self.a - other.a) <= 0:
                return NotImplemented

            else:
                return f'-({((self.a - other.a) - ((self.a - other.a) // self.b) * self.b)}/{self.b})'

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
            else:
                return f'''{int(((a_divisor - b_divisor) - ((a_divisor - b_divisor) // common_divider) * common_divider) 
                    / common_divisor)}/{int(common_divider / common_divisor)}'''

first = Rational(2, 9)
second = Rational(3, 9)
x = first - second
print(x)
