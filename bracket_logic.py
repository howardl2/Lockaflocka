##BRACKET LOGIC
from collections import namedtuple
from random import shuffle
from team_class import *




        

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
            self.current_round = self.bracket_split(temp, self.contenders, "logic")
            self.bye_round = False
                
        
        elif len(self.contenders) == len(self.teams): ##first round
            print("ROUND 1")
            shuffle(self.contenders)
            
            while(power < len(self.contenders)):
                power = power*2
            byes = power - len(self.contenders)

            for i in range(len(self.contenders) - byes):
                self.current_round.append(self.contenders[i])

            self.bye_round = True


        else: ##all other rounds
            for i in range(len(self.contenders) - byes):
                print('current', [i.team_to_str() for i in self.current_round])
                self.current_round.append(self.contenders[i])
                
        for i in range(len(self.current_round)): ##assign opponents
            print("hello")
            try:
                self.current_round[i].opponent = self.current_round[i+1]
            except:
                self.current_round[i].opponent = self.current_round[i-1]

    def update(self, winner:Team , score: tuple):
        if winner in self.contenders and winner.opponent in self.contenders:
            self.contenders[self.contenders.index(winner)].wins +=1
            self.losers.append(winner.opponent)
            self.current_round.remove(winner.opponent)
            self.contenders.remove(winner.opponent)
        else:
            print('Team no longer applicable')

    def get_team(self, team:str):
        for i in self.teams:
            if team == i.name:
                return i

    def gui_format(self, current: list, contenders: list):
        current_gui = self.bracket_split(self.current_round, self.contenders, "gui")
        

    def gui_pairing(self, current: list, contenders: list):
        byes = 0
        power = 2
        temp = list(current)
        temp = temp[::2]

        for i in range(len(temp)): ##assign opponents
            try:
                temp[i].opponent = temp[i+1]
            except:
                temp[i].opponent = temp[i-1]
        return temp

    def bracket_split(self, current: list, contenders: list, split_type: str):
        
        temp = list(current)
        print("temp:", [i.team_to_str() for i in temp])
        bye_teams = [team for team in contenders if team not in current]
        
        left_byes = bye_teams[:int(len(bye_teams)/2)]
        right_byes = bye_teams[int(len(bye_teams)/2):]

        round2_left = []
        round2_right = []

        while(len(temp)!=0):
            if len(bye_teams) < 2:
                return temp + bye_teams
            round2_left.append(left_byes.pop(0))
            round2_left.append(temp.pop(0))

            if split_type == "gui":
                round2_left.append(temp.pop(0)) ##to get its round 1 pair

            round2_right.append(right_byes.pop(0))

            try:
                round2_right.append(temp.pop(0))
                if split_type == "gui":
                    round2_right.append(temp.pop(0))
            except:
                pass

            
        for i in left_byes:
            round2_left.append(i)
        for i in right_byes:
            round2_right.append(i)


            
            
        return (round2_left + round2_right)
    
        
        
    

        
        


if __name__ == '__main__':
    
    test = bracket_logic(4, contenders, 'single elimination')
    
    print("teams", [i.team_to_str() for i in test.teams])
    test.pairings()
    print("gui level: SHOULD NOT AFFECT ROUND 1:", [i.team_to_str() for i in test.bracket_split(test.current_round, test.contenders, "gui")])
    for i in test.teams:
        test.update(i, (3, 2))

    print("current", [i.team_to_str() for i in test.current_round])
    print("contenders", [i.team_to_str() for i in test.contenders])

    
    while(len(test.contenders) !=1):

        print("Looped")
   
        test.pairings()

        test.teams.reverse()
        teams = len(test.current_round)
        
        while(len(test.current_round) > teams):
            winner = input("Please type the name of the team that won: ")
            record = input("Please type the record of the matches (Ex: (3, 2)) ")
            if (test.get_team(winner) not in test.current_round):
                winner = input("Please type the name of the team that won: ")

            test.update(winner, record)


    
