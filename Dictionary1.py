#!/usr/bin/env python
# coding: utf-8

# In[2]:


#create a dictionary key is year value
year  = 1903 

wsDict ={}
twDict = {} 

infile = open("WorldSeriesWinnersFixed.txt","r")

for line in infile:
    #key is year value is line
    line=line.strip("\n")
    wsDict[year]=line
    year+=1

for line in infile:
    
    year, team = line.strip("\n")
    year = int(year)
    
    year_winners[year] = team
    
    if team in team_wins:
        team_wins[team] += 1
    else:
        team_wins[team] = 1

#prompt user for a year
year = int(input("Enter a year between 1903 and 2008: "))

#look up the winning team for the year
team = year[year]

#look up the number of wins for the team
wins = team_wins[team]


print(f"The {team} won the World Series in {year}, and have won {wins} times.")


# In[5]:


print(wsDict)


# In[ ]:




