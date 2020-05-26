known_users=['alice','bob','Vipul','Ram','kumar','harold']
print(len(known_users))

while True:
    print("Hi My name is Travis")
    name=input("what is your name?").strip().capitalize()
    if name in known_users:
        print("Hello  {}".format(name))
        remove=input("would you like to be removed from system(y/n?").lower()
        if remove=="y":
         
            known_users.remove(name)
        elif remove=="n":
            print("no problem,i didn't want you to leave")
            
         
    else:
        print("Hmm I dont think I have met you yet {}".format(name))
        add_me=input("would you like to be add in the system?(y/n)").lower()
        if add_me=='y':
            known_users.append(name)
        elif add_me=="n":
            print("No worries see you around")