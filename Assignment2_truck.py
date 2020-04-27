Welcome to World of Cars Contd.
In this assignment we will try to simulate different types of vehicles

# Submission Guidelines
Create a folder /home/ec2-user/environment/oop/oop_submissions/oop_assignment_002. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/oop/oop_submissions/oop_assignment_002
You can make use of the Car class you have built
Write all your code in truck.py file
Using the below snippet download a program which should be used to submit code
$ wget https://itp-tech-training.s3.ap-south-1.amazonaws.com/common_resources/submit_assignment
$ chmod +x submit_assignment
To submit your assignment execute the below code snippet in the assignment folder i.e /home/ec2-user/environment/oop/oop_submissions/oop_assignment_001 here
cloud9$ ./submit_assignment
On submission you will get results.txt in your assignment folder. results.txt gives you the test case results.
#Task1: Truck
Now we need a Truck in our cars world.
A truck is a Car but with the following additional behaviours

Truck horn sounds “Honk Honk”
Truck can load some cargo within max_cargo_weight
Truck can load & unload the cargo only when the truck is at rest
load & unload method expect cargo_weight as argument which is a positive integer. Incase of invalid data raise the ValueError as shown in below code samples
Coding Guidelines:

In case of invalid data during the creation of car. Your code should raise ValueError as mentioned in the below code sample
>>> truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)  
>>> truck.load(50)  
>>> truck.load(100)  
Cannot load cargo more than max limit: 100  
>>> truck.load(-100) 
ValueError: Invalid value for cargo_weight

>>> truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)  
>>> truck.start_engine()  
>>> truck.accelerate()  
>>> truck.load(50) # Prints
Cannot load cargo during motion 
>>> truck.sound_horn() # Prints
Honk Honk  

>>> truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)  
>>> truck.start_engine() 
>>> truck.load(50)
>>> truck.accelerate()  
>>> truck.unload(50) # Prints
Cannot unload cargo during motion 
>>> truck.sound_horn() # Prints
Honk Honk  

>>> truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)  
>>> truck.start_engine() 
>>> truck.load(50)
>>> truck.unload(80)
>>> truck.load(100) # Prints
Cannot load cargo more than max limit: 100  
>>> truck.unload(50)
>>> truck.load(100)


ANSWER:



from car import Car
class Truck(Car):
    sound="Honk Honk"
    def __init__(self,color=None, max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._max_cargo_weight=max_cargo_weight
        self._loading_o=0
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    @property
    def loading_o(self):
        return self._loading_o
    def load(self,loading):
        if loading<0:
            raise ValueError("Invalid value for cargo_weight")
        elif  self._current_speed!=0:
            print("Cannot load cargo during motion")
        else:
            if self._loading_o+loading>self._max_cargo_weight:
                print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                self._loading_o+=loading
                
    def unload(self,loading1):
        if loading1<0:
            raise ValueError("Invalid value for cargo_weight")
        elif self._current_speed!=0:
            print("Cannot unload cargo during motion")
        else:
            self._loading_o-=loading1
            
    
