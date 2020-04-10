'''input:[1,2]
output:
1
2'''


class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
    # TODO: write your code here
    #pass


if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number = ComplexNumber(*input_args)

    print(complex_number.real_part)
    print(complex_number.imaginary_part)
