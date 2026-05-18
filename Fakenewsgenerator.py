#import the random module
import random

#ceate subjects

subjects = ["The government", 
           "A celebrity", "A scientist", 
           "An alien", "A politician", 
           "Prime Minister Modi" , 
           "genious Mohit" , "A dog" , 
            "A cat" , "A robot"]

# create actions 
actions = ["announced", "discovered", "invented",
             "danced with", "fought against", "fell in love with", 
             "won a Nobel Prize for", "was abducted by", 
             "became friends with", "started a new trend of"]

# create places or things
places_things = ["a new law", "a cure for cancer", "a new dance move",
                 "an alien species", "a new technology", 
                 "a secret society", "a new fashion trend", 
                 "a new planet", "a new social media platform", 
                 "a new type of food" , "at ganga ghat" , "in the moon" , "in the mars"]

# start the head;ine generator loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_thing = random.choice(places_things)

    headline = f" BREAKING NEWS :  {subject} {action} {place_thing}"
    print("\n" + headline )
    user_input = input("\n Do you want another headline? (yes/no) :").strip().lower()
    if user_input== "no":
        break
print("\n Thank you for using the Fake News Generator! Stay informed and have a great day!")
