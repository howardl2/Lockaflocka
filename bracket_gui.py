import tkinter
import bracket_logic
from team_class import *
import math

class Bracket:
        def __init__(self, num_teams:int, tournament_type:int , teams:list):
                self.teams = teams
                self.num_teams = num_teams
                self.tournament_type = tournament_type
                
                self.window = tkinter.Tk()
                self._canvas = tkinter.Canvas(self.window, width = 1000, height = 700)

                
                self.cols = 1
                if math.log(num_teams)/math.log(num_teams) != 0:
                        self.cols += 1 ##bye round 1

                self.rows = (self.num_teams * 2) + 1
                power = 2
                while(power <= self.num_teams):
                        power = power*2
                        self.cols +=1
                
                self._canvas.pack()

                canvas_width = self._canvas.winfo_reqwidth()
                canvas_height = self._canvas.winfo_reqheight()
                print(canvas_width, canvas_height)
        
       
            


        def draw_grid(self):
                canvas_width = self._canvas.winfo_reqwidth()
                canvas_height = self._canvas.winfo_reqheight()
                
                for i in range(self.rows):
                    self._canvas.create_line(
                        canvas_width * (i/self.rows), canvas_height * 0,
                        canvas_width * (i/self.rows), canvas_height * 1)
                    
                for i in range(self.cols):
                    self._canvas.create_line(
                        canvas_width * 0, canvas_height * (i/self.cols),
                        canvas_width * 1, canvas_height * (i/self.cols))

        def draw_rekt(self, row, col):
                
                canvas_width = self._canvas.winfo_reqwidth()
                canvas_height = self._canvas.winfo_reqheight()
                
                self._canvas.create_rectangle(
                    (canvas_width * (row /self.rows)) +5,
                    (canvas_height * (col /self.cols)) +5 + ((canvas_height/self.cols))/2,
                    (canvas_width * ((row + 1) /self.rows))-5,
                    (canvas_height * ((col + 1)/self.cols))-5,
                    fill = 'black')
 ##               self._canvas.create_line(
                
        
         
        def start(self):
                
                logic = bracket_logic.bracket_logic(self.num_teams,self.teams, self.tournament_type)
                logic.pairings()


                first_round = logic.current_round
                

                
                self._canvas.pack()

                canvas_width = self._canvas.winfo_reqwidth()
                canvas_height = self._canvas.winfo_reqheight()
                print(canvas_width, canvas_height)

                current_board = logic.bracket_split(logic.current_round, logic.contenders, "gui")
                print([i.team_to_str() for i in current_board])
                print("first_round", [i.team_to_str() for i in logic.current_round])

                for i in range(len(current_board)):
                        if current_board[i] in first_round:
                                print("BRO")
                                self.draw_rekt(2*i+1, self.cols-1)
                        else:
                                self.draw_rekt(2*i+1, self.cols-2)

                rounds = 3
                teams_remaining = int(len(current_board)/2)
                if teams_remaining % 2 == 1:
                        teams_remaining -= 1

                print("teams remaining: ", teams_remaining)
                
                while(teams_remaining >= 1):
                        print("teams remaining: ", teams_remaining)
                        for i in range(int(teams_remaining)):
                                self.draw_rekt( i * int(self.rows/ teams_remaining ) + int(self.rows/ teams_remaining /2) , self.cols- rounds)
                        print(self.rows)
                                
                        rounds+=1
                        teams_remaining = int(teams_remaining / 2)

                        print("teams remaining: ", teams_remaining)

                

        def update(self):
                pass
        


                

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

        contenders = [Team1, Team2, Team3, Team4, Team5, Team6, Team7]#, Team8, Team9, Team10, Team11,Team12,Team13,Team14,Team15,Team16,Team17,Team18,Team19,Team20]

        b = Bracket(7, 'asf' , contenders)
        b.start()
 ##  b.draw_grid()




