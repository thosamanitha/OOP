Welcome to World of Cars Contd.
In this assignment we will try to simulate different types of vehicles

# Submission Guidelines
Create a folder /home/ec2-user/environment/oop/oop_submissions/oop_assignment_003. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/oop/oop_submissions/oop_assignment_003
You can make use of the Car class you have built
Write all your code in race_car.py file
Using the below snippet download a program which should be used to submit code
$ wget https://itp-tech-training.s3.ap-south-1.amazonaws.com/common_resources/submit_assignment
$ chmod +x submit_assignment
To submit your assignment execute the below code snippet in the assignment folder i.e /home/ec2-user/environment/oop/oop_submissions/oop_assignment_001 here
cloud9$ ./submit_assignment
On submission you will get results.txt in your assignment folder. results.txt gives you the test case results.
#Task1: RaceCar
Now we need a RaceCar in our cars world.
A RaceCar is a Car but with the following additional behaviours.

horn sounds like “Peep Peep\nBeep Beep”
When a RaceCar is created it has 0 nitro points.
On applying brakes at more than half the max speed a Car gets 10 nitro.
When car accelerates & the nitro is available it gets additional 30% of acceleration value (rounded to int - ceil) as speed within max limits. And nitro get reduced by 10 points
Should be able to see nitro
Coding Guidelines:

Continue writing code in the same race_car.py file
>>> racecar = RaceCar(color="Red", max_speed=250, acceleration=50, tyre_friction=30)  
>>> racecar.start_engine()  
>>> racecar.accelerate()  
>>> racecar.accelerate()  
>>> racecar.accelerate()  
>>> racecar.current_speed  
150  
>>> racecar.apply_brakes()  
>>> racecar.current_speed  
120  
>>> racecar.nitro  
10  
>>> racecar.accelerate()  
>>> racecar.current_speed  
185 # 120 + 50 + (50 * 30 / 100)  
>>> racecar.nitro  
0  
>>> car.sound_horn()  # Prints
Peep Peep
Beep Beep

---------------ANSWER1:-----------

import math
class Car:
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0):
        self._color=color
        self._max_speed=max_speed
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        self._is_engine_started=False
        self._current_speed=0
        if self._max_speed<0:
            raise ValueError("Invalid value for max_speed")
        if self._acceleration<0:
            raise ValueError("Invalid value for acceleration")
        if self._tyre_friction<0:
            raise ValueError("Invalid value for tyre_friction")
    @property
    def color(self):
        return self._color
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def current_speed(self):
        return self._current_speed
        
    def accelerate(self):
        if self._is_engine_started==True:
            if self._current_speed+self._acceleration<=self._max_speed:
                self._current_speed+=self._acceleration
            else: 
                self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
            
    def start_engine(self):
        self._is_engine_started=True
    def apply_brakes(self):
        if self._current_speed>=self._tyre_friction:
            self._current_speed-=self._tyre_friction
        else:
            self._current_speed=0
            
    def sound_horn(self):
        if self._is_engine_started==False:
            print("Start the engine to sound_horn")
        else:
            print("Beep Beep")
            
    def stop_engine(self):
        self._is_engine_started=False
class RaceCar(Car):
    def __init__(self,color=None, max_speed=0,acceleration=0,tyre_friction=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro=0
    @property
    def nitro(self):
        return self._nitro
    
    def accelerate(self):
        s = 0
        if self._is_engine_started==True:
            if self._nitro>0:
                s=math.ceil(self._acceleration*30/100)
                self._nitro-=10 
            if self._current_speed+self._acceleration+s<=self._max_speed:
                self._current_speed+=self._acceleration+s
            else: 
                self._current_speed = self._max_speed
        else:
           print("Start the engine to accelerate")
          
    def apply_brakes(self):
        if self._current_speed>=self._max_speed//2:
            self._nitro+=10
        if self._current_speed>=self._tyre_friction:
            self._current_speed-=self._tyre_friction
        else:
            self._current_speed=0
    def sound_horn(self):
        if self._is_engine_started:
            print("Peep Peep\nBeep Beep")
        else:
            print("Start the engine to sound_horn")

            
            
 ------ANSWER2-----------




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
            
    
