import tkinter
import bracket_logic
from team_class import *

class Bracket:
        def __init__(self, num_teams:int, tournament_type:int , teams:list):
                self.teams = teams
                self.num_teams = num_teams
                self.tournament_type = tournament_type
                
                self.window = tkinter.Tk()
                self._canvas = tkinter.Canvas(self.window, width = 1000, height = 500)
                
                
                self.cols = 1
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

                print(logic.team_to_str(i) for i in logic.contenders)
                
                self._canvas.pack()

                canvas_width = self._canvas.winfo_reqwidth()
                canvas_height = self._canvas.winfo_reqheight()
                print(canvas_width, canvas_height)

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

        contenders = [Team1, Team2, Team3, Team4, Team5, Team6, Team7, Team8, Team9, Team10]

        b = Bracket(10, 'asf' , contenders)
 ##  b.draw_grid()




