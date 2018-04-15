# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:59:54 2018

@author: aniyo
"""
import random
participants = ["Dad","Mom","Aline","Alison","Alix","Albert"]

#Total amount of people
team_members = 6

##Randomize the order of the list
random_list = random.sample(participants,team_members)

#Generate teams
team_1 = random_list[0:3]
team_2 = random_list[3:6]

#Print out teams
print("Team 1 is:", team_1, "Team 2 is:", team_2)


