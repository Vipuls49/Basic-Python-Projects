from random import choice
questions=["why is the sky blue?","why isthe face on the moon?","where are all dinosaurs?"]

questions=choice(questions)
answer=input(questions).strip().lower()
while answer!="just beacuse":
    answer=input("why?").strip().lower()
    
