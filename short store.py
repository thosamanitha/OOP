class Item:
    def __init__(self,name=None,price=0,category=None):
        if price<=0:
            raise ValueError("Invalid value for price, got {}".format(price))
        self.name=name
        self.price=price
        self.category=category
    def __str__(self):
        return "{}@{}-{}".format(self.name,self.price,self.category)
class Query:
    def __init__(self,field,operation,value):
        op=['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if operation not in op:
            raise ValueError('Invalid value for operation, got {}'.format(operation))
        self.field=field
        self.operation=operation
        self.value=value
    def __str__(self):
        return "{} {} {}".format(self.field,self.operation,self.value)
class Store:
    def __init__(self):
        self.items=[]
    def add_item(self,item):
        self.items.append(item)
    def count(self):
        return len(self.items)
    def __str__(self):
        if len(self.items)>0:
            return "\n".join(map(str,self.items))
        else:
            return 'No items'
    def filter(self,query):
        obj1=Store()
        if query.operation=='EQ':
            for i in self.items:
                if query.value==i.name or query.value==i.price or query.value==i.category:
                    obj1.add_item((i))
            return obj1
        if query.operation=='GT':
            for i in self.items:
                if i.price>query.value:
                    obj1.add_item((i))
            return obj1
        if query.operation=='GTE':
            for i in self.items:
                if i.price>=query.value:
                    obj1.add_item((i))
            return obj1
        if query.operation=='LT':
            for i in self.items:
                if i.price<query.value:
                    obj1.add_item((i))
            return obj1
        if query.operation=='LTE':
            for i in self.items:
                if i.price<=query.value:
                    obj1.add_item((i))
            return obj1
        if query.operation=='STARTS_WITH':
            for i in self.items:
                if i.name.startswith(query.value) or i.category.startswith(query.value):
                    obj1.add_item((i))
            return obj1
        if query.operation=='ENDS_WITH':
            for i in self.items:
                if i.name.endswith(query.value) or i.category.endswith(query.value):
                    obj1.add_item((i))
            return obj1
        if query.operation=='CONTAINS':
            for i in self.items:
                if (query.field == 'name' and i.name.__contains__(query.value)) or (query.field=='category' and i.category.__contains__(query.value)):
                            obj1.add_item((i))
            return obj1
        if query.operation=='IN':
            for i in self.items:
                if i.name in query.value or i.price in query.value or i.category in query.value:
                    obj1.add_item((i))
            return obj1
    def exclude(self,query):
        obj2=Store() 
        x=self.filter(query)#creating a store object which contains filtered items of the given query
        for i in self.items:#iterating through the lis which we created at first
            if i not in x.items:#checking the condition the items that are not in filtered store
                obj2.add_item(i)
        return obj2
            
