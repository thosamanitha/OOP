class Deer:
    sound='Buck Buck'
    breathe1='Breathe in air'
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        self.age=1
        self.kg=2
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    #@classmethod
    def grow(self):
        self._required_food_in_kgs+=self.kg
        self._age_in_months+=self.age
    @classmethod
    def make_sound(self):
        print(self.sound)
    @classmethod
    def breathe(self):
        print(self.breathe1)
class Lion(Deer):
    sound='Roar Roar'
    def __init__(self,age_in_months, breed, required_food_in_kgs):
       super().__init__(age_in_months,breed,required_food_in_kgs) 
       self.kg=4
       self.age=1
    def grow(self):
        self._required_food_in_kgs+=self.kg
        self._age_in_months+=self.age
class Shark(Deer):
    sound='Shark Sound'
    breathe1='Breathe oxygen from water'
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs) 
        self.kg=8
        self.age=1
    def grow(self):
        self._required_food_in_kgs+=self.kg
        self._age_in_months+=self.age
class GoldFish(Deer):
    sound='Hum Hum'
    breathe1='Breathe oxygen from water'
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs) 
        self.kg=0.2
        self.age=1
    def grow(self):
        self._required_food_in_kgs+=self.kg
        self._age_in_months+=self.age
   
class Snake(Deer):
    sound='Hiss Hiss'
    breathe1='Breathe in air'
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs) 
        self.kg=0.5
        self.age=1
    def grow(self):
        self._required_food_in_kgs+=self.kg
        self._age_in_months+=self.age
class Zoo:
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs=reserved_food_in_kgs
        self.count=0
        self.animals=[]
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    def count_animals(self):
        return len(self.animals)
    def add_food_to_reserve(self,value):
        self._reserved_food_in_kgs+=value
    def add_animal(self,obj):
        #self.count+=1
        self.animals.append(obj)
        #self._reserved_food_in_kgs=self._reserved_food_in_kgs+obj._required_food_in_kgs
        #class1._age_in_months=class1._age_in_months+class1._age_in_months
    
   
    def feed(self,class1):
        if self._reserved_food_in_kgs<=0:
            return 0
        else:
           self._reserved_food_in_kgs=self._reserved_food_in_kgs-class1._required_food_in_kgs
           class1._age_in_months=class1._age_in_months+class1._age_in_months
        #print(type(class1))
   
   
   
   
    
'''
zoo = Zoo()
print(zoo.reserved_food_in_kgs)
zoo.add_food_to_reserve(1000)
print(zoo.reserved_food_in_kgs)
#print(zoo.count_animals())
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=90)
zoo.add_animal(gold_fish)
#print(zoo.count_animals())
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=980)
zoo.add_animal(gold_fish)
print(zoo.count_animals())
print(zoo.reserved_food_in_kgs)
zoo.feed(gold_fish)
print(zoo.reserved_food_in_kgs)
print(gold_fish.age_in_months)
'''


  
'''
nehru_zoological_park = Zoo()
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=0.5)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)
print(nehru_zoological_park.count_animals())
lion.hunt(nehru_zoological_park)
print(nehru_zoological_park.count_animals())'''
#lion.hunt(nehru_zoological_park) 

'''

zoo=Zoo()
lion =Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=8)
zoo.add_animal(lion)
print(zoo.count_animals())
zoo.add_food_to_reserve(10000000)
print(zoo.reserved_food_in_kgs)
zoo.feed(lion)
print(zoo.reserved_food_in_kgs)
print(lion.age_in_months)
'''

        

#from zoo import Deer
'''
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
print(deer.age_in_months)
print(deer.breed)
#deer.required_food_in_kgs
deer.grow()
print(deer.required_food_in_kgs)
print(deer.age_in_months)
deer.make_sound() 
deer.breathe()
#class1._age_in_months+=getattr(class1,'_age_in_months')
    
'''
