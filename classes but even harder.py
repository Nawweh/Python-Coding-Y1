import math

class Shapes:
    def areaa():
        pass
    def perimiterr():
        pass

class circle(Shapes):
    def __init__(self,radius):
        self.radius = radius
        self.pi=math.pi

    def areaa(self):
        self.area=self.pi*(self.radius*self.radius)
        return self.area
    
    def perimiterr(self):
        self.perimiter=2*(self.pi*self.radius)
        return self.perimiter

class triangle(Shapes):
    def __init__(self,side_a,side_b,side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.s=(self.side_a + self.side_b + self.side_c)/2


    def areaa(self):
        self.area=(self.s*(self.s - self.side_a)*(self.s - self.side_b)*(self.s - self.side_c))**0.5
        return self.area
    
    def perimiterr(self):
        self.perimiter=self.side_a + self.side_b + self.side_c
        return self.perimiter

class rectangle(Shapes):
    def __init__(self,height,width):
        self.height=height
        self.width=width
    
    def areaa(self):
        self.area=self.height*self.width
        return self.area
    
    def perimiterr(self):
        self.perimiter=(2*self.height),(2*self.width)
        return self.perimiter
    
def print_out():
    
    circle_1=circle(10)
    print("circle radius and perimiter: ",circle_1.perimiterr(), circle_1.areaa())
    
    triangle_1=triangle(10,7,5)
    print("triangle radius and perimiter: ",triangle_1.perimiterr(), triangle_1.areaa())

    rectangle_1=rectangle(3,6)
    print("rectangle radius and perimiter: ",rectangle_1.perimiterr(), rectangle_1.areaa())



class product():
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class electronics(product):
    def __init__(self,name,price,quantity,batteries_needed, batteries_included):
        self.batteries_needed=batteries_needed
        self.batteries_included=batteries_included
        super().__init__(name,price,quantity)
        
    def product_description(self):
        if self.batteries_included==True:
            bat_included="batteries included"
        else:
            bat_included="batteries not included"
        
        if self.batteries_needed==True:
            bat_needed="batteries needed"
        else:
            bat_needed="batteries not needed"
        self.product_desc=(f"name: {self.name}, price: £{self.price}, quantity: {self.quantity}, {bat_included}, {bat_needed}")
        return self.product_desc
    
class books(product):
    def __init__(self,name,price,quantity,author):
        self.author=author
        super().__init__(name,price,quantity)
        
    def product_description(self):
        self.product_desc=(f"name: {self.name}, price: £{self.price}, quantity: {self.quantity}, author: {self.author}")
        return self.product_desc
    
class clothes(product):
    def __init__(self,name,price,quantity,size,category):
        self.size=size
        self.category=category
        super().__init__(name,price,quantity)
        
    def product_description(self):
        self.product_desc=(f"name: {self.name}, price: £{self.price}, quantity: {self.quantity}, size: {self.size}, category: {self.category}")
        return self.product_desc
    
TV_1=electronics("TV","£5,000","74",False, True)
зD_Printer_1=electronics("3D_Printer 😊",682.83,3,False, False)

book_1=books("100 ways to cook eggs",12.50,5789,"John Egg")
book_2=books("250 ways to make malware",3.00,3,"Alex")

clothing_item_1=clothes("Grey T-shirt",27.50,65,"S","Shirt")
clothing_item_2=clothes("Green boots",92.50,65,"13","Shoes")

    
print(TV_1.product_description())
print(зD_Printer_1.product_description())
print(book_1.product_description())
print(book_2.product_description())
print(clothing_item_1.product_description())
print(clothing_item_2.product_description())


