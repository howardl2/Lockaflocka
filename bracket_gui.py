import tkinter
import bracket_logic
from team_class import *
import math

class Bracket:
        def __init__(self, num_teams:int, tournament_type:str , teams:list):
                self.teams = teams
                self.num_teams = num_teams
                self.tournament_type = tournament_type
                
                self.window = tkinter.Tk()
                self._canvas = tkinter.Canvas(self.window, width = 1000, height = 700)
                self.rectangle_data = [] #store rectangle data to draw lines

                
                self.cols = 1
                if math.log(num_teams)/math.log(num_teams) != 0:
                        self.cols += 1 ##bye round 1

                self.rows = (self.num_teams * 2) + 1
                power = 2
                while(power <= self.num_teams):
                        power = power*2
                        self.cols +=1
                
                self._canvas.pack()

                self.logic = None
                self.round = None
                self.round_number = 0
                
                self.canvas_width = self._canvas.winfo_reqwidth()
                self.canvas_height = self._canvas.winfo_reqheight()
                print(self.canvas_width, self.canvas_height)
        
       
            


        def draw_grid(self):
                
                for i in range(self.rows):
                    self._canvas.create_line(
                        self.canvas_width * (i/self.rows), self.canvas_height * 0,
                        self.canvas_width * (i/self.rows), self.canvas_height * 1)
                    
                for i in range(self.cols):
                    self._canvas.create_line(
                        self.canvas_width * 0, self.canvas_height * (i/self.cols),
                        self.canvas_width * 1, self.canvas_height * (i/self.cols))

        def draw_rekt(self, row, col, Team):
                
                
                self._canvas.create_rectangle(
                    (self.canvas_width * (row /self.rows)) +5,
                    (self.canvas_height * (col /self.cols)) +5 + ((self.canvas_height/self.cols))/2,
                    (self.canvas_width * ((row + 1) /self.rows))-5,
                    (self.canvas_height * ((col + 1)/self.cols))-5,
                    fill = 'light blue')
                self._canvas.create_text((self.canvas_width * (row /self.rows)) +5,
                                         (self.canvas_height * (col /self.cols)) +5 + ((self.canvas_height/self.cols))/2,
                                         anchor = "nw", text = Team.name)
                                         
                midpoint = (self.canvas_width * (row/self.rows) +5 + self.canvas_width * ((row + 1) /self.rows)-5)/2
                top = (self.canvas_height * (col /self.cols)) +5 + ((self.canvas_height/self.cols))/2

                for i in self.rectangle_data:
                        if i[2] == Team:
                                
                                self.rectangle_data.insert(self.rectangle_data.index(i), [midpoint, top, Team, row, col])
                                self.rectangle_data.remove(i)
                                return

                self.rectangle_data.append([midpoint, top, Team, row, col])
                

  ##              self._canvas.create_line(midpoint, top, midpoint, top-75)

        def draw_linez(self):
                k = self.round_number
                for i in self.rectangle_data:
                        for j in self.logic.current_round:
                                if i[2] == j:
                                        print(j.name, j.opponent.name)
                                        
                                        midpointX =(i[0] + self.rectangle_data[self.rectangle_data.index(i)+k][0] )/2
                                        
                                        self._canvas.create_line(i[0],i[1], midpointX, i[1] - self.canvas_height/(self.cols+3))
                                        k = -k
                                        
                        





                
##                for rec_data in self.rectangle_data:
##                        if rec_data[2] == '':
##                                try:
##                                        midpointX = (rec_data[0] + self.rectangle_data[self.rectangle_data.index(rec_data) + 1][0]) /2
##                                except:
##                                        break
##                        else:
##                                midpointX = (rec_data[0] + [rec[0] for rec in self.rectangle_data if rec_data[2].opponent in rec][0])/2
##                                
##                        print("Previous midpoint:" + str(int(rec_data[0])) + " new midpoint: " + str(int(midpointX)))
##                        self._canvas.create_line(rec_data[0], rec_data[1], midpointX, rec_data[1] - self.canvas_height/(self.cols+3) )## - distance between rows                
        
         
        def start(self):
                
                self.logic = bracket_logic.bracket_logic(self.num_teams,self.teams, self.tournament_type)
                self.logic.pairings()
                self.round_number +=1


                self.round = list(self.logic.current_round)
                
                
                self._canvas.pack()

                print(self.canvas_width, self.canvas_height)

                current_board = self.logic.bracket_split(self.logic.current_round, self.logic.contenders, "gui")
                print([i.team_to_str() for i in current_board])
                print("first_round", [i.team_to_str() for i in self.logic.current_round])

                for i in range(len(current_board)):
                        if current_board[i] in self.round:
                                self.draw_rekt(2*i+1, self.cols-1, current_board[i])
                        else:
                                self.draw_rekt(2*i+1, self.cols-2, current_board[i])
                                

                rounds = 3
                teams_remaining = int(len(current_board)/2)
                if teams_remaining % 2 == 1:
                        teams_remaining -= 1

                print("teams remaining: ", teams_remaining)
                
##                while(teams_remaining >= 1):
##                        print("teams remaining: ", teams_remaining)
##                        for i in range(int(teams_remaining)):
##                                self.draw_rekt( i * int(self.rows/ teams_remaining ) + int(self.rows/ teams_remaining /2) , self.cols- rounds, '')
##                        print(self.rows)
##                                
##                        rounds+=1
##                        teams_remaining = int(teams_remaining / 2)
##
##                        print("teams remaining: ", teams_remaining)
                self.draw_linez()

        

                

        def update(self, winner, score):
                data = None
                for i in self.rectangle_data:
                        if winner == i[2]:
                                data = i
                                print(data)

                k = 1
                if self.round.index(winner)%2 == 1:
                        k = -k
                self.logic.update(winner, score)
                print(data[3], data[4]-1)
                self.draw_rekt(data[3] + k ,data[4] -1 , winner)
                
                if len(self.logic.current_round) == (len(self.round)/2) :
                        self.logic.pairings()
                        self.round = list(self.logic.current_round)
                        self.draw_linez()
                        self.round_number +=1
        


                

if __name__ == '__main__':

        
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
        Team11 = Team('Team11', '', [], '', 0, 0)
        Team12 = Team('Team12', '', [], '', 0, 0)
        Team13 = Team('Team13', '', [], '', 0, 0)
        Team14 = Team('Team14', '', [], '', 0, 0)
        Team15 = Team('Team15', '', [], '', 0, 0)
        Team16 = Team('Team16', '', [], '', 0, 0)
        Team17 = Team('Team17', '', [], '', 0, 0)
        Team18 = Team('Team18', '', [], '', 0, 0)
        Team19 = Team('Team19', '', [], '', 0, 0)
        Team20 = Team('Team20', '', [], '', 0, 0)

        contenders = [Team1, Team2, Team3, Team4, Team5, Team6, Team7, Team8]#, Team9, Team10, Team11,Team12,Team13,Team14,Team15,Team16,Team17,Team18,Team19,Team20]

        b = Bracket(8, 'asf' , contenders)
        b.start()
 ##  b.draw_grid()




