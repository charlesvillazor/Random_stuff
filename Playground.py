#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a temporary file to play with python functions
Copy anything here into another file then save.
Have fun!
"""
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
        print()
        print("Dance: "+str(self.dan))
        print("Vocal: "+str(self.voz))
        print("Rhythm: "+str(self.rhy))
        return ("Visuals: "+str(self.vis))
    def __add__(self, other):
        dan_add = self.dan + other.dan
        voz_add = self.voz + other.voz
        rhy_add = self.rhy + other.rhy
        vis_add = self.vis + other.vis
        stat_add_list = list()
        stat_add_list.append(dan_add)
        stat_add_list.append(voz_add)
        stat_add_list.append(rhy_add)
        stat_add_list.append(vis_add)
        return stat_add_list

trainee_1 = person(3, 4, 5, 6)
a = person(4, 5, 6, 7)
print(trainee_1 + a)