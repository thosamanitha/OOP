class Pokemon:
    SOUND=''
    RUN=''
    SWIM=''
    FLY=''
    def __init__(self,name='',level=1):
        if name=='':
            raise ValueError("name cannot be empty")
        if level<=0:
            raise ValueError("level should be > 0")
        self._name=name
        self._level=level
        self._master=None
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
    @classmethod
    def make_sound(self):
        print(self.SOUND)
    @classmethod
    def run(self):
        print(self.RUN)
    @classmethod
    def swim(self):
        print(self.SWIM)
    @property
    def master(self):
        if self._master==None:
            print("No Master")
        else:
            return self._master
            
    @classmethod
    def fly(self):
        print(self.FLY)
    def __str__(self):
        return "{} - Level {}".format(self.name,self.level)
class Pikachu(Pokemon):
    SOUND='Pika Pika'
    RUN='Pikachu running...'
    def attack(self):
        print("Electric attack with {} damage".format(10*self._level))
class Squirtle(Pokemon):
    SOUND='Squirtle...Squirtle'
    RUN='Squirtle running...'
    SWIM='Squirtle swimming...'
    def attack(self):
        print("Water attack with {} damage".format(9*self._level))
class Pidgey(Pokemon):
    SOUND='Pidgey...Pidgey'
    RUN='Pidgey running...'
    FLY='Pidgey flying...'
    def attack(self):
        print("Air attack with {} damage".format(5*self._level))
class Swanna(Pokemon):
    SOUND='Swanna...Swanna'
    FLY='Swanna flying...'
    SWIM='Swanna swimming...'
    def attack(self):
        print("Water attack with {} damage".format(9*self._level))
        print("Air attack with {} damage".format(5*self._level))
class Zapdos(Pokemon):
    SOUND='Zap...Zap'
    FLY='Zapdos flying...'
    def attack(self):
        print("Electric attack with {} damage".format(10*self._level))
        print("Air attack with {} damage".format(5*self._level))
class Island:
    get_island=[]
    def __init__(self,name=None,max_no_of_pokemon=0,total_food_available_in_kgs=0):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.get_island.append(self)
        #print(self.get_island)
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self.name,self._pokemon_left_to_catch,self.total_food_available_in_kgs)
    def add_pokemon(self,obj):
        if self._pokemon_left_to_catch>=self.max_no_of_pokemon:
            print("Island at its max pokemon capacity")
        else:
            self._pokemon_left_to_catch+=1
    @classmethod
    def get_all_islands(self):
        return self.get_island
       
        
class Trainer:
    def __init__(self,name='',experience=100,max_food_in_bag=0,food_in_bag=0):
        self._name=name
        self._experience=experience
        self._max_food_in_bag=self.experience*10
        self._food_in_bag=0
        self._current_island=None
        self.pokemon=[]

    @property
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property
    def food_in_bag(self):
        return self._food_in_bag
    @property
    def current_island(self):
        if(self._current_island==None):
            print("You are not on any island")
        else:
            return self._current_island
    def __str__(self):
       return "{}".format(self.name)
    def move_to_island(self,island):
        self._current_island=island
    def catch(self,pokemon_obj):
        pokemon_obj._master = self
        self.pokemon.append(pokemon_obj)
        if self._experience>=100*pokemon_obj.level:
            self._experience+=20
            print("You caught {}".format(pokemon_obj.name))
        else:
            print("You need more experience to catch {}".format(pokemon_obj.name))
    
    def collect_food(self):
        if self._current_island==None:
           print("Move to an island to collect food")
        else:
            if self._current_island._total_food_available_in_kgs>self._max_food_in_bag:
                if self._food_in_bag<self._max_food_in_bag:
                    self._current_island._total_food_available_in_kgs-=self._max_food_in_bag
                    self._food_in_bag+=self._max_food_in_bag
                else:
                    self._food_in_bag=self._max_food_in_bag
                
            else:
                self._food_in_bag=self._current_island._total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs=0
                
    def get_my_pokemon(self):
        return self.pokemon

