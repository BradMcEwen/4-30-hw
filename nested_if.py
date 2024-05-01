place = input("choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("invalid input")
        pass
elif place == "cave":
    print("You find a hidden treasure!")
    action = input("light a torch or proceed into the dark?")
    if action == "light a torch":
        print("the light illuminates the long narrow cave")
    elif action == "proceed into the dark":
        print("You were eaten by wolves in the dark :(")
    else:
        print("invalid input")
        pass 
else:
    print("invalid input")
    pass


attendees = int(input("Enter number of attendees:"))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
audio_system = "massive speakers" if attendees > 100 else "mini speakers"
projector = "big screen" if attendees > 100 else "no projector needed"
print(venue, audio_system, projector)

attendees = int(input("Enter number of attendees: "))
food_preference = input("Would you like vegetarian food? Yes or No? ")
venue = "large hall" if attendees > 100 else "conference room"
audio_system = "massive speakers" if attendees > 100 else "mini speakers"
projector = "120 inch projector" if attendees > 100 else "50 inch projector"
food = "you can bring on the meat" if attendees > 100 else "we must have vegetarian options"
print(f"The event will be held in a {venue} and include {audio_system} to produce the music. The dance floor will be live streamed on a {projector} and for the meals {food}!")

