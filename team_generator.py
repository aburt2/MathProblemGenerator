# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 12:38:03 2017

@author: Albert niyonsenga
"""

#List generator
#Make teams of size x from a list of people

import random
def getinput():
    #Get the amount of players and teams
    while True:
        response1 = input('How many people are playing? ')
        try:
            if 0 < int(response1) < 100:   
                team_members = int(response1)
                break
            else:
                print("Please enter a value between 0 and 100")
        except ValueError:
            print("Please enter an integer")
    
    #enters name of participants
    player = 1
    participants = []
    while player <= team_members:
        response4 = input('Enter the name of the player '+str(player)+'? ' )
        participants.append(response4)
        player += 1
    
    
    #find out how many teams
    while True:
        response2 = input('How many teams are there? ')
        try:
            if 0 < int(response2) < team_members:   
                team_number = int(response2)
                break
            else:
                print("Please enter a value between 0 and "+str(team_members)+'? ')
        except ValueError:
            print("Please enter an integer") 
    
    #creates team sizes
    team_size = get_team_sizes(team_members,team_number)
    while True:
        if type(team_size) == list:
            if sum(team_size) != team_members:
                print('\nSum of the players in each team does not match player total'+'\nPlease reenter team sizes')
                team_size = get_team_sizes(team_members,team_number)
            else:
                break
        else:
            break
    
    return team_members,participants,team_number,team_size

def get_team_sizes(team_members,team_number):
    even_check = team_members//team_number * team_number
    if even_check != team_members:
        team = 1
        team_size = []
        while team <= team_number:
            while True:
                response3 = input('How many members are in team '+str(team)+'? ')
                try:
                    if 0 < int(response3) < team_members:   
                        team_size.append(int(response3))
                        break
                    else:
                        print("Please enter a value between 0 and "+str(team_members))
                except ValueError:
                    print("Please enter an integer") 
            team += 1
    else:
        team_size = int(team_members/team_number)
    return team_size

def generate_teams(team_members,participants,team_number,team_size):
    random_list = random.sample(participants,team_members)
    #same number of people per team
    if type(team_size) == int:
        index= 0
        team = []
        team_list = []
        while index<len(random_list):
            team.append(random_list[index])
            if len(team) == team_size:
                team_list.append(team)
                team = []
            index += 1
        
    #different amount of people per team
    else:
        index1 = 0
        index2 = 0
        team = []
        team_list = []
        while index1<len(random_list):
            number_of_players = team_size[index2]
            team.append(random_list[index1])
            if len(team) == number_of_players:
                team_list.append(team)
                team=[]
                index2 +=1
            index1 += 1
    
    return team_list
        
team_members,participants,team_number,team_size = getinput()              
team_list = generate_teams(team_members,participants,team_number,team_size)  
print('\n**********************************')
for value in range(team_number):
    print('Team '+str(value+1)+' is: ',team_list[value],'\n' )
          
            
