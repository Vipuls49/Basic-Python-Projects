#ask user for name
name=input("what is your name ?")
print(name)
#ask user for age
age=input("How old are you ?")
print(age)
#ask user for city
city=input("In which city do you live?")
print(city)
#ask user what they enjoy
love=input("What do you enjoy?")
print(love)
#create outut text
string="Your name is {} and you are {} years old.You live in {} and you love {}"
output=string.format(name,age,city,love)
#print output screen
print(output)

