#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:54:53 2018

@author: charlesvillazor
"""
#Game demo, text based. Project 1
#Stuck in Korea
import random
'''
Useful Commands:
    random.randint <-- random integer
'''
class person(object):
    def __init__(self, dan, voz, rhy, vis):
        assert type(dan) == int, "Stats must be integers!"
        assert type(voz)== int, "Stats must be integers!"
        assert type(rhy) == int, "Stats must be integers!"
        assert type(vis) == int, "Stats must be integers!"
        self.dan = dan
        self.voz = voz
        self.rhy = rhy
        self.vis = vis
    def __str__(self):
        print("Dance: "+str(self.dan))
        print("Vocal: "+str(self.voz))
        print("Rhythm: "+str(self.rhy))
        return ("Visuals: "+str(self.vis))
def stat_check():
    '''
    This input is nothing, I just needed a way to loop input information.
    This function is only used once, thankfully.
    '''
    print("Choose your stats, you only have 20 points to spare, so choose wisely! All stats max out at 10.")
    print()
    print("Dance is the stat that determines your dancing ability! This is useful in dance battles!")
    print()
    print("Vocals is the stat that determines your singing ability! Wow the audience with your beautiful voice!")
    print()
    print("Rhythm is the stat that is used in rap battles! Spit firey rhymes that make people want to be you!")
    print()
    print("Visuals is how you look! Captivate the crowd and get presents from fans with your looks!")
    print()
    main_dan = int(input("Enter your Dance stat: "))
    while main_dan > 10:
        main_dan = int(input("Your body is a board! Choose your Dance stat again: "))
    main_voc = int(input("Enter your Vocal stat: "))
    while main_voc > 10:
        main_voc = int(input("Your voice is trash! Choose your Vocal stat again: "))
    main_rhy = int(input("Enter your Rhythm stat: "))
    while main_rhy > 10:
        main_rhy = int(input("You're not black! Choose your Rhythm stat again: "))
    main_vis = int(input("Enter your Visual stat: "))
    while main_vis > 10:
        main_vis = int(input("You're kinda ugly! Choose your Visual stat again: "))
    if main_dan+main_voc+main_rhy+main_vis < 20:
        print(" ")
        print("You have remaining points left, are you sure you want to continue?")
        value = str(input())
        if value == "no" or "No":
            return stat_check()
        else:
            pass
    elif main_dan+main_voc+main_rhy+main_vis > 20:
        print(" ")
        print("Your stats are more than 20 points, please input them again.")
        print("-----------------------------------------------------------------------")
        stat_check()
    else:
        print(' ')
        print("You're already a Kpop god! Are you sure you want to continue with these stats?")
        value = str(input("yes/no?: "))
        if value == "no":
            print("-----------------------------------------------------------------------")
            stat_check()
        else:
            print("Okay, let's get started!")
    stat_list = list()
    stat_list.append(main_dan)
    stat_list.append(main_voc)
    stat_list.append(main_rhy)
    stat_list.append(main_vis)
    return stat_list
print("In the year 20xx, the Hallyu wave of Korea was at it's peak. The Korean culture was spreading across the world.")
print()
print("You are a rising trainee and must get prove yourself as a person in order to debut.")
print()
print("This story starts as any story would, in a training room.")
name = input("Enter your name to continue: ")
print(" ")
stat_list = stat_check()
main_dan = stat_list[0] #This part was confusing, I wrote went through the entire program like twice.
main_voc = stat_list[1] #Turns out I forgot python actually starts lists at zero and not 1.
main_rhy = stat_list[2] #I hate my life.
main_vis = stat_list[3]
main_char = person(main_dan, main_voc, main_rhy, main_vis)
print(" ")
if max(stat_list) == main_dan:
    print("As you flip across the practice room, everyone compliments the inhuman way in which your limbs move.")
elif max(stat_list) == main_voc:
    print("You hum as you walk across the practice room, calling the angels down from the heavens as you trap on your fellow trainees.")
elif max(stat_list) == main_rhy:
    print("You turn head as you walk across the practice room, as even your footsteps are starting to sound like bars.")
elif max(stat_list) == main_vis:
    print("As you stand in the practice room, your visuals are so strong it convinces other trainees to lift you up to wherever you want to go.")
else:
    print("You walk across the practice room, like an average person with average ability.")
print("")
print("Just then, your sunbae Taemin moonwalks into the room. His facial structure makes you question your sexuality.")
print("")
print("How do you respond?")
print("")
print("a. 'Taemin-sunbaenim! I'm in love with you!'")
print("b. 'Taemin-sunbaenim! Why are you stealing all the attention form me!'")
print("c. 'Why are you in here Taemin-sunbaenim? I never see you around here.'")
value = str(input("Pick a, b, or c: "))
if input == "a" or "b":
    print('')
    print("Taemin only responds with a glare, one that showed the confidence only found in a Kpop star.")
    print("Taemin then challenges you to a dance battle. Get Ready!")
else:
    print('')
    print("Taemin smiles at you, seemingly thankful. It leaves you breathless and for an unknown reason somewhat turned on.")
    print("To make sense of your emotions, you challenge Taemin to a dance battle. Get Ready!")
def Taemin_Dance_Battle():
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    