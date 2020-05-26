films={"Finding Dory":[3,5],
       "Bourne":[18,5],
       "Tarzan":[15,5],
       "Ghost Busters":[12,5]
       }

while True:
    choice=input("what film would you like to watch?").strip().title()
    
    if choice in films:
        
        age=int(input("how old are you?").strip())
        #check age
        if age>=films[choice][0]:
            
            #check tickets
            if films[choice][1]>0:
                
                print("enjoy the film")
                films[choice][1]=films[choice][1]-1
            else:
                print("sorry we are sold out")
        else:
            print("you are too young to see that film")
    else:
        print("we don't have that film..")