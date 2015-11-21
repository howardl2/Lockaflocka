##BRACKET LOGIC
from collections import namedtuple
from random import shuffle
from team_class import *


Team1 = Team('Team1', '', [], '', 0, 0)
Team2 = Team('Team2', '', [], '', 0, 0)
Team3 = Team('Team3', '', [], '', 0, 0)
Team4 = Team('Team4', '', [], '', 0, 0)
Team5 = Team('Team5', '', [], '', 0, 0)
Team6 = Team('Team6', '', [], '', 0, 0)

contenders = [Team1, Team2, Team3, Team4, Team5, Team6]



        

class bracket_logic():
    def __init__(self, num_teams:int , teams:list , tournament_type:str ):
                  self.tournament_type = tournament_type
                  self.num_teams = num_teams
                  self.teams = list(teams)
                  self.contenders = teams
                  self.losers = []
                  self.current_round = []

##sets the people in the current round

                  
    def pairings(self):
        byes = 0
        power = 2
        self.current_round = []
##if seedings then sort
##if none then shuffle
        
        if(len(self.contenders) == len(self.teams)):       
            shuffle(self.contenders)
            
            while(power <= len(self.contenders)):
                power = power*2
                byes = power - len(self.contenders)
        
        for i in range(len(self.contenders) - byes):
            self.current_round.append(self.contenders[-i])
            
        for i in range(len(self.current_round)):
            if i % 2 == 0:
                self.current_round[i].opponent = self.current_round[i+1]
            else:
                self.current_round[i].opponent = self.current_round[i-1]

    def update(self, winner:Team , score: str):
        if winner in self.contenders and winner.opponent in self.contenders:
            self.contenders[self.contenders.index(winner)].wins +=1
            self.losers.append(winner.opponent)
            self.current_round.remove(winner.opponent)
            self.contenders.remove(winner.opponent)
        else:
            print('ya fucked up')

    def get_team(self, team:str):
        for i in self.teams:
            if team == i.name:
                return i

        
        


if __name__ == '__main__':
    test = bracket(6, contenders, 'single elimination')
    print([i.team_to_str() for i in test.teams])
    while(len(test.contenders) !=1):
        print([i.team_to_str() for i in test.current_round])
        print([i.team_to_str() for i in test.contenders])
        test.pairings()
        test.update(test.get_team('Team1'), '3-2')
        test.update(test.get_team('Team2'), '3-2')
        test.update(test.get_team('Team3'), '3-2')
        test.update(test.get_team('Team4'), '3-2')
        test.update(test.get_team('Team5'), '3-2')
        test.update(test.get_team('Team6'), '3-2')
        print([i.team_to_str() for i in test.current_round])
        print([i.team_to_str() for i in test.contenders])
        
 
    
    
