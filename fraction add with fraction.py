import fractions
class Fraction(object):
    def __init__(self,numerator,denominator):
        self._numerator=numerator
        self._denominator=denominator
    @property
    def numerator(self):
        pass
    @property
    def denominator(self):
        pass
    def __add__(self,other):
        f_one = fractions.Fraction(self._numerator,self._denominator)
        f_two = fractions.Fraction(other._numerator,other._denominator)
        a=str((f_one)._numerator)+'/'+str((f_one)._denominator)
        b=str((f_two)._numerator)+'/'+str((f_two)._denominator)
        final=str((f_one+f_two).numerator)+'/'+str((f_one+f_two).denominator)
        print('{} + {} = {}'.format(a, b, final))
        return f_one + f_two
if __name__ == "__main__":
    import json

    input_args = list(json.loads(input()))

    fraction_one = Fraction(*input_args[0])
    fraction_two = Fraction(*input_args[1])

    result_fraction = fraction_one + fraction_two

    try:
        fraction_one._numerator
    except AttributeError:
        print("Missed protecting numerator")

    try:
        fraction_one._denominator
    except AttributeError:
        print("Missed protecting denominator")

    try:
        fraction_one.numerator = 1
        print("Missed setting safe access to numerator")
    except AttributeError:
        pass

    try:
        fraction_one.denominator = 1
        print("Missed setting safe access to numerator")
    except AttributeError:
        pass

    print(isinstance(fraction_one, Fraction))
    print(isinstance(fraction_two, Fraction))
    print(result_fraction.numerator)
    print(result_fraction.denominator)
    
    
    
 input:
 [[-5, 2], [3, 2]]
 output:
-5/2 + 3/2 = -1/1
True
True
-1
1

    
