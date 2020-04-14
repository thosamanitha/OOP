import fractions
import math
class Fraction(object):
    def __init__(self,numerator,denominator):
        self._numerator=numerator
        self._denominator=denominator
        if numerator>0 and denominator<0:
            self._numerator=-(self._numerator)
            self._denominator=abs(self._denominator)
        elif numerator<0 and denominator<0:
            self._numerator=abs(self._numerator)
            self._denominator=abs(self._denominator)
              
        gcd=math.gcd(self._numerator,self._denominator)
        self._numerator=int(self._numerator/gcd)
        self._denominator=int(self._denominator/gcd)
    @property
    def numerator(self):
        return self._numerator
    @property
    def denominator(self):
        return self._denominator
    def __str__(self):
        return '{}/{}'.format(self._numerator,self._denominator)
    def __truediv__(self,other):
        r_num=self._numerator*other._denominator
        r_deno=self._denominator*other._numerator
        r=Fraction(r_num,r_deno)
        '''print('{}/{} / {}/{} = {}/{}'.format(self._numerator,self._denominator,other._numerator,other._denominator,r._numerator,r._denominator))'''
        '''print('{} / {} = {}'.format(str(fraction_one),str(fraction_two),str(r)))'''
        print('{} / {} = {}'.format(self,other,r))
        return r

if __name__ == "__main__":
    import json

    input_args = list(json.loads(input()))

    fraction_one = Fraction(*input_args[0])
    fraction_two = Fraction(*input_args[1])

    result_fraction = fraction_one / fraction_two

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
