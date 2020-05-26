import random
class Pound:
    
    def __init__(self,rare=False):
        self.rare=rare
        if self.rare:
            self.value=1.25
        else:
            self.value=1.00
            
      
        self.colour="gold"
        self.num_edges=1
        self.diameter=22.5#in mm
        self.thickness=3.15#in mm
        self.heads=True
        
    def __del__(self):
        print("coin spent")
        
    def rust(self):
        self.colour="greenish"
        
    def clean(self):
        self.colour="gold"
        
    def flip(self):
        head_options=[True,False]
        choice=random.choice(head_options)
        self.heads=choice
    
   
    
   
