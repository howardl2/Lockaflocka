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
Team7 = Team('Team7', '', [], '', 0, 0)
Team8 = Team('Team8', '', [], '', 0, 0)
Team9 = Team('Team9', '', [], '', 0, 0)
Team10 = Team('Team10', '', [], '', 0, 0)

contenders = [Team1, Team2, Team3, Team4, Team5, Team6, Team7, Team8, Team9, Team10]



        

class bracket_logic():
    def __init__(self, num_teams:int , teams:list , tournament_type:str ):
                  self.tournament_type = tournament_type
                  self.num_teams = num_teams
                  self.teams = list(teams)
                  self.contenders = teams
                  self.losers = []
                  self.current_round = []
                  self.bye_round = False

##sets the people in the current round

                  
    def pairings(self):
        byes = 0
        power = 2
        temp = list(self.current_round)
        
        self.current_round = []
        
##if seedings then sort
##if none then shuffle
        print(self.bye_round)
        if self.bye_round: ##bye round (2)
            print("ROUND 2")
            bye_teams = [team for team in self.contenders if team not in temp]
            left_byes = bye_teams[:len(bye_teams)/2]
            right_byes = bye_teams[len(bye_teams)/2:]
            
            print("temp:", [i.team_to_str() for i in temp])
            
            count = 0
            round2_left = []
            round2_right = []
            
            while(len(temp) !=0):
                round2_left.append(left_byes.pop[0])
                round2_left.append(temp.pop[0])

                round2_right.append(right_byes.pop[0])

                try:
                    round2_right.append(temp.pop[0])
                except:
                    pass

            self.current_round = round2_left + round2_right
                
                
            for i in temp2:
                self.current_round.append(i)

            self.bye_round = False

                
        
        elif len(self.contenders) == len(self.teams): ##first round
            print("ROUND 1")
            shuffle(self.contenders)
            
            while(power <= len(self.contenders)):
                power = power*2
                byes = power - len(self.contenders)

            for i in range(len(self.contenders) - byes):
                print([i.team_to_str() for i in test.current_round])
                self.current_round.append(self.contenders[i])

            self.bye_round = True


        else: ##all other rounds
            for i in range(len(self.contenders) - byes):
                print([i.team_to_str() for i in test.current_round])
                self.current_round.append(self.contenders[i])
                
        for i in range(len(self.current_round)): ##assign opponents
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
    
    test = bracket_logic(10, contenders, 'single elimination')
    
    print("teams", [i.team_to_str() for i in test.teams])
    while(len(test.contenders) !=1):
        
        print("current", [i.team_to_str() for i in test.current_round])
        print("contenders", [i.team_to_str() for i in test.contenders])
        
        test.pairings()
        
        print("current", [i.team_to_str() for i in test.current_round])
        print("contenders", [i.team_to_str() for i in test.contenders])
        
        for i in test.teams:
            test.update( i , '3-2')

##        test.update(test.get_team("Team1"),'3-2')
##        test.update(test.get_team("Team2"),'3-2')
##        test.update(test.get_team("Team3"),'3-2')
##        test.update(test.get_team("Team4"),'3-2')
##        test.update(test.get_team("Team5"),'3-2')
##        test.update(test.get_team("Team6"),'3-2')

        
        print("current", [i.team_to_str() for i in test.current_round])
        print("contenders", [i.team_to_str() for i in test.contenders])
        
 
    
    
