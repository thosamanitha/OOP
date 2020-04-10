'''
input:
12.2
10
output:
122.0
44.4
'''

class Rectangle:

    def __init__(self, length, breadth):
        # TODO: write your code here
        self.length=length
        self.breadth=breadth
        #self.rectangle=0
        pass

    def get_area(self):
        s=self.length*self.breadth
        return s
        # TODO: write your code here
        pass

    def get_perimeter(self):
        s1=2*(self.length+self.breadth)
        return s1
        # TODO: write your code here
        pass


if __name__ == "__main__":
    length = float(input())
    breadth = float(input())

    rectangle = Rectangle(length=length, breadth=breadth)
    print(rectangle.get_area())
    print(rectangle.get_perimeter())44
